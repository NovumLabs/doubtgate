import sys
import argparse
from scripts.evaluate_harness import DoubtgateEvaluator, run_benchmark

def main():
    parser = argparse.ArgumentParser(description="doubtgate: Automated Quantum Mechanics Benchmark and Retrieval System")
    parser.add_argument("-q", "--query", type=str, help="Query to retrieve context for")
    parser.add_argument("-k", "--top_k", type=int, default=3, help="Number of chunks")
    parser.add_argument("--benchmark", action="store_true", help="Run benchmark")
    
    args = parser.parse_args()
    print("[+] Initializing DoubtgateEvaluator...")
    evaluator = DoubtgateEvaluator()

    if args.benchmark:
        print("[+] Running Benchmark Suite...")
        run_benchmark()
    elif args.query:
        print(f"\n[+] Querying corpus for: \"{args.query}\" (top_k={args.top_k})")
        results = evaluator.retrieve(args.query, top_k=args.top_k)
        if not results:
            print("[-] No matching chunks found.")
        for i, res in enumerate(results, 1):
            print(f"\n[{i}] Topic: {res.get('topic', 'N/A')} (Score: {res.get('score', 0.0):.4f})")
            print(f"    Snippet: {res.get('text', '')[:200]}...")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
