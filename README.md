# VSE / Theory “ВСЕ” — Recoverable Process Exactification

**Primary human author / research program originator:** **Antyshev**  
**ORCID:** https://orcid.org/0009-0002-2082-5563  
**Priority snapshot version:** v0.1-priority — 2026-10-07  
**Immutable GitHub Release:** pending final public audit  
**Publication language:** English (original research history is preserved separately in Russian)

This repository is the **public, curated priority record** for the VSE research program and its project-specific results.

> The complete research archive is intentionally kept private. This public repository contains only reviewed material that is safe and useful to disclose.

## Start here

- [Scientific significance](SCIENTIFIC_SIGNIFICANCE.md)
- [Publication scope and non-claims](PUBLICATION_SCOPE.md)
- [Authorship and priority statement](AUTHORSHIP_AND_PRIORITY.md)
- [Claims ledger](CLAIMS_LEDGER.md)
- [Public evidence status](PUBLIC_EVIDENCE_STATUS.md)
- [Publication roadmap](PUBLICATION_ROADMAP.md)
- [Paper 1 outline](PAPER1_OUTLINE.md)
- [Disclosure matrix](DISCLOSURE_MATRIX.md)
- [Citation metadata](CITATION.cff)
- [AI assistance disclosure](AI_DISCLOSURE.md)

## Core technical contribution

The current exactification pipeline is

$$
\mathrm{FULL} \to \mathrm{SATURATE} \to \mathrm{JOINT} \to \mathrm{TRANSFORM}
\to \mathrm{RECOVER\_TEST} \to \mathrm{SAFE\_QUOTIENT}
\to \mathrm{FACTOR} \to \mathrm{RESIDUAL} \to \mathrm{REIFY/CLASSIFY}.
$$

The central identity distinction is

$$
\mathrm{STATE} \ne \mathrm{EVENT} \ne \mathrm{LINEAGE} \ne \mathrm{MACROOBJECT} \ne \mathrm{WORLD}.
$$

Operational rules:

$$
\mathrm{SATURATE}\;\text{before}\;\mathrm{TRANSFORM},
$$

$$
\mathrm{JOINT}\;\text{before}\;\mathrm{MARGINAL},
$$

$$
\mathrm{RECOVER}\;\text{before}\;\mathrm{QUOTIENT}.
$$

## Public evidence currently included

### Theory
- [Canonical act v4.1](theory/CANONICAL_ACT_v4_1_JOINT_SATURATION_CROSSBLOCK.md)

### Generator
- [v39 architecture specification](generator/VSE_FUTURE_PHYSICS_GENERATOR_v39_SPEC.json)
- [v39 migration auditor](generator/VSE_GENERATOR_v39_MIGRATION_AUDITOR.py)
- [q5/q7 finite cross-block verifier](generator/VSE_Q5_Q7_NATIVE_BRIDGE_VERIFY.py)

### Certificates
- [Joint cross-block certificate](certificates/VSE_JOINT_CROSSBLOCK_CERTIFICATE_031.json)
- [Generator migration audit](certificates/VSE_GENERATOR_v39_MIGRATION_AUDIT.json)
- [D2 negative-control reproducer](reproducibility/d2_negative_control/README.md)
- [q5/q7 native cross-block certificate](certificates/VSE_Q5_Q7_NATIVE_CROSSBLOCK_CERTIFICATE_009.json)
- [Internal pole-ray registry](certificates/VSE_INTERNAL_POLE_RAY_REGISTRY_018.json)
- [Frame-stripped transport audit](certificates/VSE_FRAME_STRIPPED_TRANSPORT_AUDIT_018.json)

### Research note
- [Route 031 — Cross-Gram / recovery / cross-block](research-notes/ROUTE_031_CROSSGRAM_PETZ_DILATION_CROSSBLOCK.md)

## Priority claims in this release

1. Target-faithful process exactification with saturation, joint relations, explicit recovery, and safe quotienting.
2. Explicit separation of structural state identity from event/process identity in the source-preserving generator.
3. A labeled joint-relation/cross-block passport retained before destructive quotient.
4. Project-specific q5/q7 generated complex sectors with a native nonzero cross-block whose finite *-algebraic closure is $M_5(\mathbb C)$, with a bounded public finite certificate and verifier.
5. Source-preserving finite-generator audits and recurrent internal spectral/pole structures within their declared computational scope.

## Important non-claims

This repository does **not** currently claim:
- a completed physical Theory of Everything;
- a proof of the Riemann hypothesis;
- a proof of P vs NP;
- experimentally established particle identifications;
- Monster symmetry as a forced symmetry of our universe.

## Authorship

The research program, its conceptual direction, problem selection, project-specific hypotheses, generator architecture, computational experiments, and interpretation of the included VSE results are attributed in this release to **Antyshev**.

AI systems were used as research assistants for literature search, symbolic/numerical checking, code generation, adversarial audit, and drafting. AI tools are **not authors** of this release.

## Citation

Please cite this repository/release using [CITATION.cff](CITATION.cff).

**Antyshev** — ORCID **0009-0002-2082-5563**.

## Version integrity

Historical releases must not be silently overwritten. Each release will be tied to:
- Git commit SHA;
- release tag;
- SHA-256 manifest;
- DOI / archival identifiers when assigned.

See [AUTHORSHIP_AND_PRIORITY.md](AUTHORSHIP_AND_PRIORITY.md), [CLAIMS_LEDGER.md](CLAIMS_LEDGER.md), [PUBLIC_EVIDENCE_STATUS.md](PUBLIC_EVIDENCE_STATUS.md), and [CHANGELOG.md](CHANGELOG.md).
