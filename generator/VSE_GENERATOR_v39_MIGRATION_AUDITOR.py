#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VSE v39 migration auditor.
Reads a source-preserving VSE SQLite store and audits why structural state identity
must be separated from process/event identity and why finite future hashes are not
safe physical quotient certificates.
"""
from pathlib import Path
import sqlite3, json, argparse

def audit(db_path: str):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    nodes = cur.execute("select count(*) from nodes").fetchone()[0]
    transitions = cur.execute("select count(*) from transitions").fetchone()[0]
    status = dict(cur.execute(
        "select status,count(*) from transitions group by status"
    ).fetchall())
    incoming = cur.execute("""
      SELECT child,COUNT(*),COUNT(DISTINCT parent),COUNT(DISTINCT filling_json),
             COUNT(DISTINCT source_json),COUNT(DISTINCT q_to_parent_json)
      FROM transitions WHERE child IS NOT NULL GROUP BY child
    """).fetchall()
    multi = [r for r in incoming if r[1] > 1]
    collisions = cur.execute("""
      SELECT profile_hash,COUNT(*) FROM response_profiles
      WHERE depth=0 AND complete=1
      GROUP BY profile_hash HAVING COUNT(*)>1
    """).fetchall()
    profile_stats = cur.execute("""
      SELECT depth,complete,COUNT(*),COUNT(DISTINCT profile_hash)
      FROM response_profiles GROUP BY depth,complete ORDER BY depth,complete
    """).fetchall()
    return {
      "version":"VSE_v39_migration_audit",
      "nodes":nodes,
      "transitions":transitions,
      "transition_status":status,
      "state_vs_event":{
        "states_with_multiple_incoming_events":len(multi),
        "fraction_nonroot":len(multi)/max(1,nodes-1),
        "extra_incoming_histories":sum(r[1]-1 for r in multi),
        "states_with_multiple_parents":sum(r[2]>1 for r in incoming),
        "states_with_multiple_recovery_maps":sum(r[5]>1 for r in incoming),
        "max_incoming_events":max(r[1] for r in incoming)
      },
      "future_profile":{
        "depth0_collision_groups":len(collisions),
        "depth0_excess_exact_states":sum(r[1]-1 for r in collisions),
        "depth0_largest_collision":max(r[1] for r in collisions),
        "stats":[
          {"depth":d,"complete":bool(c),"rows":n,"distinct_hashes":h}
          for d,c,n,h in profile_stats
        ]
      },
      "rule":"STATE_ID != EVENT_ID. No physical quotient from finite profile equality "
             "without completeness + recovery + no-late-separator."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("db")
    ap.add_argument("--out",default="VSE_v39_migration_audit.json")
    args=ap.parse_args()
    result=audit(args.db)
    Path(args.out).write_text(
        json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8"
    )
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()