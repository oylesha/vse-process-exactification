# Public Evidence Status

**Author:** Antyshev — ORCID 0009-0002-2082-5563  
**Audit date:** 2026-10-07

This file distinguishes a public priority claim from the amount of reproducibility evidence currently present in this curated repository.

| Area | Public claim status | Public evidence status | Note |
|---|---|---|---|
| State / event / lineage separation | COMPUTATIONAL | INCLUDED | Migration audit is public. |
| Finite future-profile collision audit | COMPUTATIONAL | INCLUDED | Migration audit is public. |
| Labeled cyclic cross-Gram recovery | EXACT | INCLUDED | The theorem and computational cross-check are public. |
| q5/q7 native cross-block → M5 | COMPUTATIONAL + STANDARD EXACT THEOREM | PARTIAL | The algebra theorem and project statement are public; the direct raw generator-native bridge artifact is not yet promoted. |
| Internal pole-ray candidates | COMPUTATIONAL | INCLUDED, SCOPED | Public registry and frame-stripped transport audit include explicit non-particle guards. |
| Full D2 SQLite / Archive-7 raw data | PRIVATE | NOT PUBLIC | Preserved for private archival upload through Git LFS. |
| RH / P vs NP / physical Monster / first-principles constants | OPEN / CONDITIONAL | NOT A SOLVED CLAIM | These are not asserted as solved. |

## Language policy

The curated public layer is English-first. The historical research record may remain in Russian inside the private archive. Translation is an editorial layer and must not rewrite historical provenance.

## Release gate

Before creating the immutable GitHub release `v0.1-priority`:
1. complete this evidence audit;
2. verify all public files are English-first except intentional project names;
3. ensure every claim points to its public evidence or is explicitly marked PARTIAL;
4. regenerate the release archive and SHA-256 manifest from the final public tree;
5. only then create the GitHub Release and DOI deposit.
