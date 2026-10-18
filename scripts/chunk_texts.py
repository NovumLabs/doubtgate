import os
import json
import glob

def chunk_text(text, chunk_size=1000, overlap=200):
    """Splits text into overlapping chunks of approximately chunk_size characters."""
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        # Try to find a natural boundary (period or newline) if not at the end
        if end < text_length:
            next_period = text.find('.', end - 100, min(end + 100, text_length))
            if next_period != -1:
                end = next_period + 1
        
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        start = end - overlap
        if start < 0:
            start = 0
        if end == text_length:
            break
            
    return chunks

def main():
    clean_dir = "data/clean"
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(clean_dir):
        print(f"[!] Clean directory not found at {clean_dir}. Run parse_articles.py first.")
        return

    print("Starting text chunking process...")
    all_chunks = []
    
    for filepath in glob.glob(os.path.join(clean_dir, "*.txt")):
        filename = os.path.basename(filepath)
        topic_name = filename.replace(".txt", "").replace("_", " ")
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        chunks = chunk_text(content, chunk_size=1000, overlap=200)
        print(f"[*] {topic_name}: Created {len(chunks)} chunks")
        
        for idx, chunk in enumerate(chunks):
            chunk_record = {
                "id": f"{filename}_chunk_{idx:03d}",
                "topic": topic_name,
                "source_file": filename,
                "chunk_index": idx,
                "text": chunk,
                "char_length": len(chunk)
            }
            all_chunks.append(chunk_record)
            
    output_file = os.path.join(output_dir, "chunks.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
        
    print(f"\n[+] Successfully saved {len(all_chunks)} total chunks to {output_file}")
    print("Stage 3 Chunking Complete!")

if __name__ == "__main__":
    main()