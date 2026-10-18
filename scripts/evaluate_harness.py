import os
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DoubtgateEvaluator:
    def __init__(self, chunks_path="data/processed/chunks.json"):
        if not os.path.exists(chunks_path):
            raise FileNotFoundError(f"[!] Chunks file not found at {chunks_path}. Run Stage 3 first.")
            
        with open(chunks_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)
            
        print(f"[*] Loaded {len(self.chunks)} chunks into evaluation engine.")
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.chunk_texts = [chunk["text"] for chunk in self.chunks]
        self.tfidf_matrix = self.vectorizer.fit_transform(self.chunk_texts)

    def retrieve(self, query, top_k=3):
        """Retrieves top_k most relevant chunks for a given query."""
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = similarities.argsort()[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            chunk = self.chunks[idx]
            results.append({
                "id": chunk["id"],
                "topic": chunk["topic"],
                "score": float(similarities[idx]),
                "text": chunk["text"]
            })
        return results

def run_benchmark():
    evaluator = DoubtgateEvaluator()
    
    # Core Quantum Mechanics Benchmark Test Suite
    benchmark_queries = [
        {
            "id": "q1",
            "query": "What is the physical significance of the wave function in quantum mechanics?",
            "expected_topic": "Wave function"
        },
        {
            "id": "q2",
            "query": "Explain Heisenberg's uncertainty principle regarding position and momentum.",
            "expected_topic": "Uncertainty principle"
        },
        {
            "id": "q3",
            "query": "How does the time-independent Schrödinger equation describe quantum states?",
            "expected_topic": "Schrödinger equation"
        },
        {
            "id": "q4",
            "query": "What is quantum tunnelling and how do particles pass through potential barriers?",
            "expected_topic": "Quantum tunnelling"
        },
        {
            "id": "q5",
            "query": "State the Pauli exclusion principle for fermions.",
            "expected_topic": "Pauli exclusion principle"
        }
    ]

    print("\n--- Running Doubtgate Benchmark Suite ---")
    correct_retrievals = 0
    
    for item in benchmark_queries:
        print(f"\n[Test {item['id']}] Query: \"{item['query']}\"")
        retrieved = evaluator.retrieve(item['query'], top_k=1)
        
        if retrieved:
            top_match = retrieved[0]
            is_match = top_match['topic'].lower() == item['expected_topic'].lower()
            if is_match:
                correct_retrievals += 1
                
            print(f"  -> Retrieved Topic: {top_match['topic']} (Score: {top_match['score']:.4f})")
            print(f"  -> Match Status: {'✅ PASS' if is_match else '❌ FAIL'}")
            print(f"  -> Snippet: {top_match['text'][:150]}...")

    accuracy = (correct_retrievals / len(benchmark_queries)) * 100
    print(f"\n========================================")
    print(f"[+] Benchmark Complete! Retrieval Accuracy: {accuracy:.1f}% ({correct_retrievals}/{len(benchmark_queries)})")
    print(f"========================================")

if __name__ == "__main__":
    run_benchmark()