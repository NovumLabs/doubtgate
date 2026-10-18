import os
import re

def clean_wikitext(text):
    """Simple regex-based cleaner for Wikipedia wikitext to extract readable prose."""
    # Remove comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    # Remove ref tags and their contents
    text = re.sub(r'<ref.*?>.*?</ref>', '', text, flags=re.DOTALL)
    text = re.sub(r'<ref.*?/>', '', text)
    
    # Remove other HTML tags
    text = re.sub(r'</?[a-zA-Z0-9]+.*?>', '', text)
    
    # Remove file/image links
    text = re.sub(r'\[\[(?:File|Image):.*?\]\]', '', text, flags=re.IGNORECASE)
    
    # Simplify internal links [[Target|Label]] -> Label, or [[Target]] -> Target
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)
    
    # Remove basic templates / infoboxes
    text = re.sub(r'\{\{([^{}]*)\}\}', '', text)
    
    # Remove external links
    text = re.sub(r'\[https?://[^\s\]]+ ([^\]]+)\]', r'\1', text)
    text = re.sub(r'\[https?://[^\s\]]+\]', '', text)
    
    # Clean up multiple newlines or spaces
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def main():
    raw_dir = "data/raw"
    clean_dir = "data/clean"
    os.makedirs(clean_dir, exist_ok=True)
    
    if not os.path.exists(raw_dir):
        print(f"[!] Raw directory not found at {raw_dir}. Run fetch_articles.py first.")
        return

    print("Starting data parsing and cleaning...")
    for filename in os.listdir(raw_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(raw_dir, filename)
            output_path = os.path.join(clean_dir, filename)
            
            with open(input_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
            
            cleaned_content = clean_wikitext(raw_content)
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(cleaned_content)
                
            print(f"[+] Cleaned and saved: {filename}")

    print("\nStage 2 Data Parsing Complete!")

if __name__ == "__main__":
    main()