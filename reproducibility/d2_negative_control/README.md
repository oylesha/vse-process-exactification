# D2 negative-control reproducer

This small public package provides two bounded counterexamples to naive quotienting in the source-preserving D2 dataset used in Paper 1.

## Control A — structural identity is not event identity

One exact structural child passport is reached by **three literal events**. The three events have different:
- parents;
- recovery-to-parent maps;
- fillings/source choices.

A structural-only store keeps one child state and therefore cannot, by itself, reconstruct which incoming event occurred. A target that retains provenance or recovery distinguishes the events immediately.

## Control B — a finite response signature is not exact-state identity

Two distinct exact structural passports, with distinct exact state matrices, share the same complete depth-0 response-profile hash. Equality of this bounded readout signature therefore does not authorize an absolute quotient.

## Fixture-only verification

```bash
python3 VSE_D2_NEGATIVE_CONTROL_VERIFY.py
```

No third-party Python packages are required.

## Verification against the full SQLite dataset

```bash
python3 VSE_D2_NEGATIVE_CONTROL_VERIFY.py --db /path/to/VSE_SOURCE_PRESERVING_D2_v1_3_2026-10-06.sqlite
```

Expected database SHA-256:

`89a3d33dc30949de26e58ae9ab082366b9005ddd8ddede14ac823a20a6f5c575`

In full-database mode the verifier recomputes the headline D2 counts, the finite-profile collision counts, and confirms that both bounded counterexamples occur literally in the exact database.

## Scope guard

These are finite computational counterexamples. They show that the tested structural-only and finite-readout quotients are unsafe for targets that retain the erased information. They do **not** prove a unique universal physical identity relation or a cofinal quotient theorem.
