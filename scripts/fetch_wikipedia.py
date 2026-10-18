import sys
import requests
import os

def fetch_article(title):
    print(f"Fetching Wikipedia article: {title}")
    headers = {"User-Agent": "DoubtgateProject/0.1.0 (contact@novumlabs.com)"}
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=ids&titles={title}&format=json"
    try:
        res = requests.get(url, headers=headers)
        data = res.json()
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if page_id == "-1":
                print(f"Warning: Article '{title}' not found on Wikipedia.")
            else:
                print(f"Success: Found '{title}' (Page ID: {page_id})")
    except Exception as e:
        print(f"Error fetching {title}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for title in sys.argv[1:]:
            fetch_article(title)
    else:
        print("Usage: python scripts\fetch_wikipedia.py 'Article Title'")