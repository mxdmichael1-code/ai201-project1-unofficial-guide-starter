from pathlib import Path
import json
import re

DOCUMENTS_DIR = Path("documents")
OUTPUT_PATH = Path("chunks.json")

CHUNK_SIZE = 500
OVERLAP = 100
MIN_LENGTH = 100


def clean_text(text):
    # Basic cleanup only: remove weird spacing and repeated blank lines
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_text(text, source):
    """
    Paragraph-aware fixed-size chunking.

    Instead of cutting blindly every 550 characters, this tries to keep
    paragraphs together until the chunk is around CHUNK_SIZE.
    """
    chunks = []
    chunk_id = 0

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    current_chunk = ""

    for paragraph in paragraphs:
        # If the current chunk is empty, start it with this paragraph
        if not current_chunk:
            current_chunk = paragraph
            continue

        # Try adding the next paragraph
        candidate = current_chunk + "\n\n" + paragraph

        # If still within chunk size, keep building the chunk
        if len(candidate) <= CHUNK_SIZE:
            current_chunk = candidate

        # If too long, save current chunk and start a new one with overlap
        else:
            if len(current_chunk) >= MIN_LENGTH:
                chunks.append({
                    "id": f"{source.replace('.txt', '')}_{chunk_id}",
                    "source": source,
                    "text": current_chunk
                })
                chunk_id += 1

            # Add overlap from the previous chunk to preserve context
            overlap_text = current_chunk[-OVERLAP:] if len(current_chunk) > OVERLAP else current_chunk
            current_chunk = overlap_text + "\n\n" + paragraph

    # Save the last chunk
    if len(current_chunk.strip()) >= MIN_LENGTH:
        chunks.append({
            "id": f"{source.replace('.txt', '')}_{chunk_id}",
            "source": source,
            "text": current_chunk.strip()
        })

    return chunks


def main():
    all_chunks = []

    txt_files = sorted(DOCUMENTS_DIR.glob("*.txt"))

    print(f"Found {len(txt_files)} txt files.")

    for file_path in txt_files:
        raw_text = file_path.read_text(encoding="utf-8")
        cleaned_text = clean_text(raw_text)

        chunks = chunk_text(cleaned_text, file_path.name)
        all_chunks.extend(chunks)

        print(f"{file_path.name}: {len(chunks)} chunks")

    OUTPUT_PATH.write_text(
        json.dumps(all_chunks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"\nSaved {len(all_chunks)} chunks to {OUTPUT_PATH}")

    print("\n=== SAMPLE CHUNKS ===")
    for chunk in all_chunks[:5]:
        print("\n---")
        print(f"ID: {chunk['id']}")
        print(f"Source: {chunk['source']}")
        print(f"Length: {len(chunk['text'])}")
        print(chunk["text"][:600])


if __name__ == "__main__":
    main()