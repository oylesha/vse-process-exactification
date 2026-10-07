#!/usr/bin/env python3
"""Public verifier for two bounded D2 negative controls.

Default: verify the compact public fixture.
Optional --db: verify the fixture and aggregate counts against the exact full D2 SQLite database.
No third-party packages are required.
"""
from __future__ import annotations
import argparse, hashlib, json, sqlite3
from pathlib import Path

DB_SHA = "89a3d33dc30949de26e58ae9ab082366b9005ddd8ddede14ac823a20a6f5c575"
EXPECTED = {
    "nodes":29311,"transitions":35637,"multi_incoming_states":6235,
    "multi_parent_states":5807,"multi_qmaps_states":5352,"extra_incoming_histories":6327,
    "depth0_rows":29311,"depth0_distinct_hashes":23703,
    "depth0_collision_groups":2044,"depth0_largest_collision":51,
    "depth1_rows":81,"depth1_distinct_hashes":80,
}
HERE=Path(__file__).resolve().parent
DEFAULT=HERE/"VSE_D2_NEGATIVE_CONTROL_FIXTURE.json"

def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"))

def verify_fixture(d):
    a=d["control_A"]; ev=a["events"]
    b=d["control_B"]; st=b["states"]
    out={
        "A_event_count":len(ev),
        "A_distinct_parents":len({x["parent"] for x in ev}),
        "A_distinct_recovery_maps":len({canon(x["q_to_parent"]) for x in ev}),
        "A_distinct_fillings":len({canon(x["filling"]) for x in ev}),
        "B_state_count":len(st),
        "B_distinct_passports":len({x["passport"] for x in st}),
        "B_distinct_state_matrices":len({canon(x["state"]) for x in st}),
    }
    out["pass"]=(out["A_event_count"]==3 and out["A_distinct_parents"]==3 and
                 out["A_distinct_recovery_maps"]==3 and out["A_distinct_fillings"]==3 and
                 out["B_state_count"]==2 and out["B_distinct_passports"]==2 and
                 out["B_distinct_state_matrices"]==2)
    return out

def counts(con):
    q={
      "nodes":"SELECT COUNT(*) FROM nodes",
      "transitions":"SELECT COUNT(*) FROM transitions",
      "multi_incoming_states":"SELECT COUNT(*) FROM (SELECT child,COUNT(*) c FROM transitions WHERE child IS NOT NULL GROUP BY child HAVING c>1)",
      "multi_parent_states":"SELECT COUNT(*) FROM (SELECT child,COUNT(DISTINCT parent) c FROM transitions WHERE child IS NOT NULL GROUP BY child HAVING c>1)",
      "multi_qmaps_states":"SELECT COUNT(*) FROM (SELECT child,COUNT(DISTINCT q_to_parent_json) c FROM transitions WHERE child IS NOT NULL GROUP BY child HAVING c>1)",
      "extra_incoming_histories":"SELECT SUM(c-1) FROM (SELECT child,COUNT(*) c FROM transitions WHERE child IS NOT NULL GROUP BY child HAVING COUNT(*)>1)",
      "depth0_rows":"SELECT COUNT(*) FROM response_profiles WHERE depth=0 AND complete=1",
      "depth0_distinct_hashes":"SELECT COUNT(DISTINCT profile_hash) FROM response_profiles WHERE depth=0 AND complete=1",
      "depth0_collision_groups":"SELECT COUNT(*) FROM (SELECT profile_hash,COUNT(*) c FROM response_profiles WHERE depth=0 AND complete=1 GROUP BY profile_hash HAVING c>1)",
      "depth0_largest_collision":"SELECT MAX(c) FROM (SELECT profile_hash,COUNT(*) c FROM response_profiles WHERE depth=0 AND complete=1 GROUP BY profile_hash)",
      "depth1_rows":"SELECT COUNT(*) FROM response_profiles WHERE depth=1 AND complete=1",
      "depth1_distinct_hashes":"SELECT COUNT(DISTINCT profile_hash) FROM response_profiles WHERE depth=1 AND complete=1",
    }
    return {k:con.execute(v).fetchone()[0] for k,v in q.items()}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--fixture",type=Path,default=DEFAULT)
    ap.add_argument("--db",type=Path)
    a=ap.parse_args()
    d=json.loads(a.fixture.read_text())
    out={"fixture_sha256":sha256(a.fixture),"fixture":verify_fixture(d)}
    if a.db:
        h=sha256(a.db); db={"sha256":h,"expected_sha256":DB_SHA}
        if h!=DB_SHA:
            db["pass"]=False; out["database"]=db; out["pass"]=False
            print(json.dumps(out,indent=2)); return 2
        con=sqlite3.connect(a.db); c=counts(con)
        checks={k:(c[k]==v) for k,v in EXPECTED.items()}
        child=d["control_A"]["child_passport"]
        ids=[r[0] for r in con.execute("SELECT arrow_id FROM transitions WHERE child=? ORDER BY arrow_id",(child,))]
        fixture_ids=sorted(x["arrow_id"] for x in d["control_A"]["events"])
        h0=d["control_B"]["profile_hash"]
        passports=[r[0] for r in con.execute("SELECT passport FROM response_profiles WHERE depth=0 AND complete=1 AND profile_hash=? ORDER BY passport",(h0,))]
        fixture_passports=sorted(x["passport"] for x in d["control_B"]["states"])
        db.update({"counts":c,"count_checks":checks,"control_A_matches_db":ids==fixture_ids,"control_B_matches_db":passports==fixture_passports})
        db["pass"]=all(checks.values()) and db["control_A_matches_db"] and db["control_B_matches_db"]
        out["database"]=db
    out["pass"]=out["fixture"]["pass"] and (not a.db or out["database"]["pass"])
    print(json.dumps(out,indent=2))
    return 0 if out["pass"] else 1

if __name__=="__main__":
    raise SystemExit(main())
