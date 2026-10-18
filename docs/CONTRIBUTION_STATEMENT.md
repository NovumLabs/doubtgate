# Contribution statement and pre-specified hypotheses

Written 2026-10-18, before any experiments. Commit this file before running anything, and do not edit it afterwards except by dated amendment.

## Contribution (draft; refine after reading the related work)

Unlike prior selective-refusal benchmarks that perturb context in general-domain QA, we study a small physics knowledge base with human-verified labels, and measure (1) near-miss questions matched to the wrong stored question, and (2) planted factual and numeric errors in the knowledge base, using CPU-only retrieval baselines and a SymPy numeric verifier.

## Say / do not say

| Say | Do not say |
|---|---|
| "We extend selective-refusal evaluation to..." | "First benchmark for..." |
| "Reduces confident errors on our benchmark at the cost of X% coverage" | "Solves hallucination" |
| "On a physics KB with human-verified labels" | "General-purpose RAG safety" |

## Hypotheses

- **H1:** Hybrid retrieval beats TF-IDF on reworded questions.
- **H2:** A margin-based or learned abstention rule beats a fixed score threshold on near-miss questions, at equal coverage.
- **H3:** A question-match check reduces answers given to the wrong stored question.
- **H4:** A SymPy numeric verifier catches planted numeric errors with few false alarms.

## Metrics (fixed in advance)

Recall@k and MRR; false-accept rate (answered when it should have refused); refusal precision and recall; risk-coverage curve and its area; faithfulness on a human-checked sample; CPU latency.

## Protocol rules

- Tune only on the dev split. Touch the test split once.
- Keep benchmark text out of every knowledge base, except answerable items held out by design.
- Report failures, confidence intervals and limitations. Report all configurations, not only the best.

## Amendments

(none yet)
