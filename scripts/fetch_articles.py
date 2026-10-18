import csv
import os
import json
import urllib.request
import urllib.parse

def fetch_wikipedia_text(page_title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content|ids",
        "titles": page_title,
        "format": "json",
        "redirects": "1"
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Doubtgate-QuantumMechanics-Bot/1.0 (Educational Project)"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for page_id, page_data in pages.items():
                if page_id == "-1":
                    print(f"[-] Page not found: {page_title}")
                    return None
                revisions = page_data.get("revisions", [])
                if revisions:
                    return revisions[0].get("*")
    except Exception as e:
        print(f"[!] Error fetching {page_title}: {e}")
    return None

def main():
    sources_path = "data/sources.csv"
    raw_dir = "data/raw"
    os.makedirs(raw_dir, exist_ok=True)
    if not os.path.exists(sources_path):
        print(f"[!] Manifest not found at {sources_path}. Run generate_manifest.py first.")
        return
    print(f"Reading sources from {sources_path}...")
    with open(sources_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Explicitly remove BOM character and whitespace
            title = row["title"].replace("\ufeff", "").strip()
            filename_safe = "".join(c if c.isalnum() or c in (" ", "_", "-") else "_" for c in title).strip().replace(" ", "_")
            output_file = os.path.join(raw_dir, f"{filename_safe}.txt")
            print(f"[*] Fetching content for: {title}...")
            content = fetch_wikipedia_text(title)
            if content:
                with open(output_file, mode="w", encoding="utf-8") as out:
                    out.write(content)
                print(f"[+] Saved to {output_file}")
            else:
                print(f"[-] Failed to retrieve content for {title}")
    print("\nStage 1B Article Acquisition Complete!")

if __name__ == "__main__":
    main()