#!/usr/bin/env python3
"""Verify the public D2 late-separator witness.

Usage:
  python generator/VSE_D2_LATE_SEPARATOR_VERIFY.py
  python generator/VSE_D2_LATE_SEPARATOR_VERIFY.py /path/to/VSE_SOURCE_PRESERVING_D2_v1_3_2026-10-06.sqlite

Without a database path, this checks the bounded public certificate.
With a database path, it also verifies the certificate directly against the
source-preserving SQLite database and its SHA-256.
"""
from __future__ import annotations
import hashlib, json, sqlite3, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "certificates" / "VSE_D2_LATE_SEPARATOR_CERTIFICATE_007.json"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def check_certificate(c: dict) -> dict:
    ps = list(c["passports"])
    if len(ps) != 2:
        raise AssertionError("expected exactly two witness passports")
    a, b = (c["passports"][p] for p in ps)
    checks = {
        "same_step": a["step"] == b["step"],
        "same_parent": a["parent"] == b["parent"],
        "depth0_complete_both": a["depth0"]["complete"] and b["depth0"]["complete"],
        "same_depth0_profile_hash": a["depth0"]["profile_hash"] == b["depth0"]["profile_hash"],
        "depth1_complete_both": a["depth1"]["complete"] and b["depth1"]["complete"],
        "different_depth1_profile_hash": a["depth1"]["profile_hash"] != b["depth1"]["profile_hash"],
        "same_depth1_arrow_count": a["depth1"]["arrow_count"] == b["depth1"]["arrow_count"],
        "different_depth1_child_classes": a["depth1"]["child_classes"] != b["depth1"]["child_classes"],
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks

def db_record(conn: sqlite3.Connection, passport: str) -> dict:
    n = conn.execute(
        "select step,parent,state_json,qroot_json from nodes where passport=?", (passport,)
    ).fetchone()
    if n is None:
        raise AssertionError(f"missing node {passport}")
    out = {
        "step": n[0],
        "parent": n[1],
        "state": json.loads(n[2]),
        "qroot": json.loads(n[3]),
    }
    for depth in (0, 1):
        r = conn.execute(
            """select profile_hash,current_signature,child_classes,arrow_count,complete
               from response_profiles
               where passport=? and depth=? and target_version=?""",
            (passport, depth, "PHYS_ROOT_FESHBACH_RIESZ_HODGE_v1"),
        ).fetchone()
        if r is None:
            raise AssertionError(f"missing depth-{depth} profile for {passport}")
        out[f"depth{depth}"] = {
            "profile_hash": r[0],
            "current_signature": r[1],
            "child_classes": r[2],
            "arrow_count": r[3],
            "complete": bool(r[4]),
        }
    return out

def main() -> int:
    cert = json.loads(CERT_PATH.read_text())
    result = {"certificate_checks": check_certificate(cert), "database_checked": False}
    if len(sys.argv) > 1:
        db = Path(sys.argv[1]).expanduser().resolve()
        actual_sha = sha256(db)
        if actual_sha != cert["source_database_sha256"]:
            raise AssertionError({"database_sha256": actual_sha, "expected": cert["source_database_sha256"]})
        conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        for passport, expected in cert["passports"].items():
            actual = db_record(conn, passport)
            if actual != {k: expected[k] for k in ("step","parent","state","qroot","depth0","depth1")}:
                raise AssertionError({"passport": passport, "actual": actual, "expected": expected})
        result["database_checked"] = True
        result["database_sha256"] = actual_sha
    result["pass"] = True
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
