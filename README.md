# DoubtGate

*A doubt-aware retrieval-augmented QA toolkit and benchmark: when should a system **answer**, **flag**, or **refuse**?*
(Hindi/Bengali tagline: संशय / সংশয় — "doubt".)

**Status: pre-alpha. Planning stage. There are no results yet.** Nothing in this repository should be read as a validated system.

## What this project is

An honest, careful extension of existing selective-refusal work to a narrow domain:
a small quantum-mechanics knowledge base with human-verified labels, CPU-only retrieval baselines
(TF-IDF, BM25, one open embedding model, hybrid fusion), three abstention rules, and a SymPy numeric verifier.
The benchmark is called **DoubtGate-QM**.

See `docs/CONTRIBUTION_STATEMENT.md` for exactly what we claim and what we do not,
and `docs/RELATED_WORK.md` for the prior work this builds on.

## Planned layout

```
src/        toolkit code (retrievers, abstention rules, verifier)
data/       benchmark items and labels (source texts referenced by ID, not redistributed)
tests/      unit tests
docs/       contribution statement, related work, name check
```

## Licences

- Code: MIT (see `LICENSE`).
- Benchmark labels and our own written questions: planned CC BY 4.0. Source texts keep their own licences (see `DATA_LICENSES.md`).

## Cite

See `CITATION.cff`.

## Disclaimer

Research prototype. It can be wrong. Not for assessment of real students, and not for medical, legal or safety decisions.

## Contact

Novum Labs Pvt. Ltd.
