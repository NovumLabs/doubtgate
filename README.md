# DoubtGate

**A Doubt-Aware Retrieval-Augmented Generation (RAG) QA Toolkit & Benchmark**
*When should a system answer, flag, or refuse?*

*(Tagline: संशय / সংশয় — Hindi/Bengali for "doubt".)*

[![Release](https://img.shields.io/github/v/release/NovumLabs/doubtgate?label=release&color=blue)](https://github.com/NovumLabs/doubtgate/releases)
[![Benchmark Accuracy](https://img.shields.io/badge/benchmark_accuracy-100%25-brightgreen)](#-benchmark--evaluation)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Benchmark & Evaluation](#-benchmark--evaluation)
- [The DoubtGate-QM Corpus](#-the-doubtgate-qm-corpus)
- [How the Answer / Flag / Refuse Decision Works](#-how-the-answer--flag--refuse-decision-works)
- [Project Structure](#-project-structure)
- [Integration & CI/CD](#-integration--cicd)
- [Limitations](#-limitations)
- [Roadmap](#-roadmap)
- [Release History](#-release-history)
- [Contributing](#-contributing)
- [License & Contact](#-license--contact)

---

## Overview

**DoubtGate** (`NovumLabs/doubtgate`) is an open-source evaluation benchmark and retrieval toolkit that targets hallucination, overconfidence, and ungrounded retrieval in RAG pipelines.

Most RAG systems are built to always produce an answer. DoubtGate asks a different question: **should the system answer at all?** For every query, the toolkit helps decide whether to:

| Outcome | Meaning |
|---------|---------|
| ✅ **Answer** | Retrieved context strongly supports the query. |
| ⚠️ **Flag** | Context is partial or ambiguous; respond with an explicit uncertainty warning. |
| 🛑 **Refuse** | The query is out-of-scope or ungrounded; do not generate an answer. |

The current release focuses on a controlled **Quantum Mechanics (DoubtGate-QM)** domain and pairs CPU-optimized vector retrieval with rule-based abstention logic. The **v2.0 release** introduces a unified CLI entry point (`doubtgate.py`), a 5/5 pass rate on the ground-truth benchmark over 417 indexed quantum chunks, and standardized cross-platform environment support.

---

## Key Features

- **Dual-Mode CLI (`doubtgate.py`)** — Run the automated ground-truth evaluation suite or execute interactive top-*k* context retrieval queries from a single entry point.
- **CPU-Lightweight Retrieval** — A `scikit-learn` TF-IDF vectorizer with cosine-similarity scoring delivers fast retrieval with zero GPU requirements.
- **Selective Refusal & Abstention Engine** — Rule-based logic measures retrieval confidence to prevent ungrounded generation on out-of-scope or ambiguous physics queries.
- **DoubtGate-QM Corpus** — 417 human-verified, chunked quantum mechanics knowledge units covering wave mechanics, operators, the uncertainty principle, Schrödinger equations, and the exclusion principle.
- **Deterministic Evaluation Harness** — A modular, self-contained `DoubtgateEvaluator` class designed for reproducible runs and CI/CD verification workflows.
- **Cross-Platform Support** — Standardized paths and environment setup for Windows (PowerShell), macOS, and Linux.

---

## System Architecture

```text
                       ┌───────────────────────────┐
                       │     User Input / Query    │
                       └─────────────┬─────────────┘
                                     │
                                     ▼
                       ┌───────────────────────────┐
                       │    CLI (`doubtgate.py`)   │
                       └──────┬─────────────┬──────┘
                              │             │
        ┌─────────────────────┘             └─────────────────────┐
        ▼                                                         ▼
  [--benchmark Mode]                                       [--query Mode]
┌────────────────────────────────────┐        ┌────────────────────────────────────┐
│  scripts/evaluate_harness.py       │        │  TF-IDF Vectorizer & Cosine Match  │
├────────────────────────────────────┤        ├────────────────────────────────────┤
│ 1. Loads 417 indexed QM chunks     │        │ 1. Vectorizes query string         │
│ 2. Runs ground-truth test suite    │        │ 2. Computes cosine similarities    │
│ 3. Computes precision & pass rate  │        │ 3. Returns top-k ranked contexts   │
└─────────────────┬──────────────────┘        └─────────────────┬──────────────────┘
                  │                                             │
                  ▼                                             ▼
        [100% Verified Report]                       [Context Output Terminal]
```

---

## Quick Start

### Prerequisites

- Python **3.9+**
- `pip` (or any compatible package manager)
- No GPU required

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/NovumLabs/doubtgate.git
cd doubtgate

# 2. (Recommended) Create a virtual environment
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Usage

`doubtgate.py` is the single entry point and supports two modes.

### Mode 1 — Benchmark

Run the full ground-truth evaluation suite against the indexed corpus:

```bash
python doubtgate.py --benchmark
```

This loads the 417 QM chunks, executes the ground-truth tests via `scripts/evaluate_harness.py`, and prints precision and pass-rate results.

### Mode 2 — Interactive Query

Retrieve the top-*k* most relevant context chunks for a question:

```bash
python doubtgate.py --query "What does the Heisenberg uncertainty principle state?"
```

The CLI vectorizes the query with TF-IDF, scores every chunk by cosine similarity, and prints the ranked contexts to the terminal.

> **Tip:** Run `python doubtgate.py --help` to see all available options for your installed version.

### Programmatic Use

```python
from scripts.evaluate_harness import DoubtgateEvaluator

evaluator = DoubtgateEvaluator()
results = evaluator.run()
print(results)
```

> The exact `DoubtgateEvaluator` constructor arguments and return structure may vary by release; consult the class docstrings in `scripts/evaluate_harness.py`.

---

## Benchmark & Evaluation

The evaluation harness runs a deterministic ground-truth suite over the DoubtGate-QM corpus.

| Metric | v2.0 Result |
|--------|-------------|
| Indexed corpus size | 417 chunks |
| Ground-truth tests passed | **5 / 5** |
| Benchmark accuracy | **100%** |
| Hardware | CPU only |

Because the harness is deterministic (TF-IDF + cosine similarity, no sampling), identical inputs produce identical outputs — making it suitable for regression testing.

---

## The DoubtGate-QM Corpus

A controlled, human-verified knowledge base of **417 chunked units** drawn from foundational quantum mechanics, including:

- Wave mechanics and wave-particle duality
- Operators and observables
- The Heisenberg uncertainty principle
- The time-dependent and time-independent Schrödinger equations
- The Pauli exclusion principle

A narrow, controlled domain makes it possible to define clear boundaries for what is *in scope* — which is essential for evaluating when a system ought to refuse.

---

## How the Answer / Flag / Refuse Decision Works

DoubtGate treats **retrieval confidence as the primary signal** for whether a response is grounded.

1. **Retrieve** — The query is vectorized and matched against all corpus chunks using cosine similarity.
2. **Score** — The similarity of the top-ranked chunk(s) is used as a confidence measure.
3. **Decide** — Rule-based thresholds map confidence to an outcome:
   - **High confidence** → *Answer* using the retrieved context.
   - **Moderate confidence** → *Flag* the response as uncertain or partially supported.
   - **Low confidence / out-of-scope** → *Refuse* rather than generate an ungrounded answer.

This keeps the abstention logic transparent, auditable, and easy to tune — no black-box classifier involved.

---

## Project Structure

```text
doubtgate/
├── doubtgate.py              # Unified CLI entry point (v2.0)
├── scripts/
│   └── evaluate_harness.py   # DoubtgateEvaluator & ground-truth suite
├── data/                     # DoubtGate-QM corpus and index (417 chunks)
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md
```

> Directory names above reflect the intended layout; adjust to match your checkout if it differs.

---

## Integration & CI/CD

The benchmark mode can gate pull requests or releases. Example GitHub Actions workflow:

```yaml
name: DoubtGate Benchmark

on: [push, pull_request]

jobs:
  benchmark:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python doubtgate.py --benchmark
```

---

## Limitations

Being transparent about scope is in the spirit of the project:

- **Small ground-truth suite.** The 100% result reflects 5/5 tests; it demonstrates correctness on the defined suite, not broad generalization.
- **Lexical retrieval.** TF-IDF matches on term overlap and can miss paraphrases or semantic similarity that dense embeddings would catch.
- **Single domain.** The corpus covers quantum mechanics only; behavior on other domains is untested.
- **Rule-based abstention.** Thresholds are hand-set and may need recalibration for new corpora.
- **Retrieval, not generation.** The toolkit decides *whether* to answer and surfaces context; it does not ship a built-in language model.

---

## Roadmap

- [ ] Expand the ground-truth suite with more answer / flag / refuse cases
- [ ] Add dense-embedding retrieval as an optional backend
- [ ] Calibrated confidence thresholds with reported precision/recall per outcome
- [ ] Additional domain corpora beyond quantum mechanics
- [ ] Optional LLM generation layer gated by the abstention engine

---

## Release History

| Version | Title | Summary of Changes |
|---------|-------|--------------------|
| **v2.0** | Finalized CLI & Production Release | Unified CLI entry point (`doubtgate.py`), PowerShell path standardization, and 100% benchmark verification pass rate. |
| **v1.5** | Retrieval Engine & Evaluation Harness | Stage 4 vector retrieval engine (`scripts/evaluate_harness.py`) and ground-truth evaluation target suite. |
| **v1.4 – v1.3** | Corpus Parsing & Ingestion | Data parsing pipeline, text chunking, and index setup for 417 quantum mechanics units. |

See the [Releases page](https://github.com/NovumLabs/doubtgate/releases) for full notes.

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please run `python doubtgate.py --benchmark` before submitting to confirm the suite still passes.

---

## 📄 License & Contact

- **License:** Released under the [MIT License](LICENSE).
- **Maintained by:** Novum Labs Pvt. Ltd.
- **Address:** Basanta Villas, Lane No - 2, Rani Park, Badu Road, Madhyamgram, West Bengal, 700129, India
- **Phone:** +919007639350
