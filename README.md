# DoubtGate

*A Doubt-Aware Retrieval-Augmented Generation (RAG) QA Toolkit & Benchmark*  
*When should a system answer, flag, or refuse?*  
*(Tagline: संशय / সংশয় — Bengali/Hindi for "doubt".)*

[![Release](https://img.shields.io/github/v/release/NovumLabs/doubtgate?label=release&color=blue)](https://github.com/NovumLabs/doubtgate/releases)
[![Benchmark Pass Rate](https://img.shields.io/badge/benchmark_accuracy-100%25-brightgreen)](#-benchmark--evaluation-suite)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Executive Overview

**DoubtGate** (`NovumLabs/doubtgate`) is an open-source evaluation benchmark and retrieval toolkit built to address hallucination, overconfidence, and ungrounded retrieval in RAG pipelines. Focusing on a controlled **Quantum Mechanics (DoubtGate-QM)** domain, the framework provides CPU-optimized vector retrieval engines alongside rule-based abstention mechanisms to determine whether a query should be **answered**, **flagged for uncertainty**, or **refused entirely**.

The `v2.0` release introduces a production-ready, unified CLI entry point (`doubtgate.py`), full 5/5 ground-truth benchmark accuracy over 417 indexed quantum chunks, and standardized cross-platform environment support.

---

## Key Features & Theoretical Foundations

* **Dual-Mode CLI Interface (`doubtgate.py`)**: Seamlessly switch between running automated ground-truth evaluation suites and executing interactive top-$k$ context retrieval queries.
* **CPU-Lightweight Vector Retrieval**: Uses a scikit-learn TF-IDF vectorizer coupled with cosine similarity scoring to execute fast, zero-GPU retrieval over indexed corpus units.
* **Selective Refusal & Abstention Engine**: Implements rules to measure retrieval confidence and prevent ungrounded generation on out-of-scope or ambiguous physics queries.
* **DoubtGate-QM Corpus**: 417 human-verified, chunked quantum mechanics knowledge units covering foundational principles (wave mechanics, operators, uncertainty, Schrödinger equations, and exclusion principles).
* **Deterministic Evaluation Harness**: Modular, self-contained `DoubtgateEvaluator` class designed for integration into CI/CD verification workflows.

---

## System Architecture

```text
                               ┌───────────────────────────┐
                               │   User Input / Query      │
                               └─────────────┬─────────────┘
                                             │
                                             ▼
                               ┌───────────────────────────┐
                               │    CLI (`doubtgate.py`)   │
                               └──────┬─────────────┬──────┘
                                      │             │
                ┌─────────────────────┘             └──────────────────────┐
                ▼                                                          ▼
  [--benchmark Mode]                                               [--query Mode]
┌──────────────────────────────────────┐                ┌──────────────────────────────────────┐
│  `scripts/evaluate_harness.py`       │                │ TF-IDF Vectorizer & Cosine Matcher   │
├──────────────────────────────────────┤                ├──────────────────────────────────────┤
│ 1. Loads 417 Indexed QM Chunks       │                │ 1. Vectorizes Query String           │
│ 2. Runs Ground-Truth Test Suite      │                │ 2. Calculates Cosine Distances       │
│ 3. Computes Precision & Pass Rate    │                │ 3. Returns Top-k Ranked Contexts     │
└──────────────────┬───────────────────┘                └──────────────────┬───────────────────┘
                   │                                                       │
                   ▼                                                       ▼
      [100% Verified Report]                                  [Context Output Terminal]

## Release History
v2.0: Finalized CLI entry point (doubtgate.py), PowerShell path standardization, and 100% benchmark verification pass rate.

v1.5: Stage 4 vector retrieval engine and evaluation harness.

v1.4 - v1.3: Data parsing pipeline and chunk indexing setup.

## License & Contact
Code: MIT (see LICENSE)

## Maintained by: Novum Labs Pvt. Ltd.
