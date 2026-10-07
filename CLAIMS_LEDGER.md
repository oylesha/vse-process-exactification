# Claims Ledger

**Primary author:** Antyshev — ORCID 0009-0002-2082-5563

Each public claim receives a stable ID. Claims must never be silently rewritten. Scientific status and public-evidence status are tracked separately.

| Claim ID | Claim | First public date | Scientific status | Public evidence status | Evidence / dependency |
|---|---|---|---|---|---|
| VSE-C001 | Structural state identity and literal process/event identity must be represented separately in the current source-preserving generator. | 2026-10-07 | COMPUTATIONAL | INCLUDED | [Generator migration audit](certificates/VSE_GENERATOR_v39_MIGRATION_AUDIT.json) + [D2 negative control](reproducibility/d2_negative_control/README.md) |
| VSE-C002 | The canonical project runtime requires saturation, joint relation retention, recovery testing, and safe quotienting before destructive identification. | 2026-10-07 | FRAMEWORK | INCLUDED | [Canonical act v4.1](theory/CANONICAL_ACT_v4_1_JOINT_SATURATION_CROSSBLOCK.md) |
| VSE-C003 | A full labeled joint Gram can retain cyclic phase information that is lost by diagonal magnitude or unlabeled spectrum. | 2026-10-07 | EXACT | INCLUDED | [Joint cross-block certificate](certificates/VSE_JOINT_CROSSBLOCK_CERTIFICATE_031.json) + canonical act |
| VSE-C004 | The project-specific q5/q7 generated sectors possess a native nonzero cross-block; together with full diagonal matrix algebras this closes to M5(C) in the declared finite coat. | 2026-10-07 | COMPUTATIONAL + EXACT | INCLUDED, SCOPED | [Native cross-block certificate](certificates/VSE_Q5_Q7_NATIVE_CROSSBLOCK_CERTIFICATE_009.json) + [public verifier](generator/VSE_Q5_Q7_NATIVE_BRIDGE_VERIFY.py) + standard matrix-algebra theorem. |
| VSE-C005 | Current Archive-7 scans exhibit recurrent internal pole-ray structures and frame-stripped residual invariance within the declared scanned finite coat. | 2026-10-07 | COMPUTATIONAL | INCLUDED, SCOPED | [Pole-ray registry](certificates/VSE_INTERNAL_POLE_RAY_REGISTRY_018.json) + [frame-stripped transport audit](certificates/VSE_FRAME_STRIPPED_TRANSPORT_AUDIT_018.json); explicit non-particle guards apply. |
| VSE-C006 | Finite future-profile equality does not by itself authorize physical identity in the current generator without completeness/theorem sufficiency, recovery, and no-late-separator certification. | 2026-10-07 | COMPUTATIONAL + LOGICAL | INCLUDED | [Generator migration audit](certificates/VSE_GENERATOR_v39_MIGRATION_AUDIT.json) |

## Status vocabulary

- EXACT — mathematical theorem/proof in the declared coat.
- COMPUTATIONAL — reproduced by the declared code/data or machine artifact.
- CONDITIONAL — true under explicit gates.
- FRAMEWORK — formal architecture/definition, with consequences tested separately.
- PROGRAM — proposed research route.
- OPEN — unresolved.
- FAIL — explicit negative witness.
- EXTERNAL — imported known theorem with citation.

## Public evidence vocabulary

- INCLUDED — the public repository contains the relevant bounded artifact.
- INCLUDED, SCOPED — evidence is public but proves only the explicitly stated finite/computational scope.
- PARTIAL — the priority claim is timestamped, but a direct reproducibility artifact still remains to be promoted after review.
- PRIVATE — supporting material remains in the private archive and is not part of the public evidence package.

See [PUBLIC_EVIDENCE_STATUS.md](PUBLIC_EVIDENCE_STATUS.md).

## Update rule

When a claim changes:
1. preserve the old claim in Git history;
2. mark the changed scientific status explicitly;
3. add a corrected claim/version rather than silently broadening it;
4. document the change in CHANGELOG.md.
