import sys
import csv
import argparse

def main():
    parser = argparse.ArgumentParser(description="Validate Doubtgate source manifest")
    parser.add_argument("--sources", required=True, help="Path to sources.csv")
    parser.add_argument("--sources-only", action="store_true", help="Validate sources only")
    args = parser.parse_args()

    print(f"Validating sources from {args.sources}...")
    try:
        with open(args.sources, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("id"):
                    print("Error: Missing ID in sources manifest.")
                    sys.exit(1)
        print("OK")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()