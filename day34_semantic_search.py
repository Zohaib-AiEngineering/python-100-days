
from pypdf import PdfReader

def split_text(text, chunk_size=500, chunk_overlap=50):
    if chunk_overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks


print("STEP 1: Starting PDF reader")

reader = PdfReader("sample.pdf")
print("STEP 2: PDF opened")

all_text = []

for page in reader.pages:
    text = page.extract_text() or ""
    if text.strip():
        all_text.append(text)

full_text = "\n".join(all_text)
print("STEP 3: PDF text extracted")
print("Total characters:", len(full_text))

chunks = split_text(full_text)

print("STEP 4: Chunking completed")
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3], start=1):
    print(f"\n--- CHUNK {i} ---")
    print(chunk)

# STEP 1: Simple keyword search in PDF chunks

query = input("Apna search question likho: ").lower()

print("\nSearch Results:\n")

found = False

for i, chunk in enumerate(chunks):
    if any(word in chunk.lower() for word in query.split()):
        print(f"Chunk {i + 1}:")
        print(chunk)
        print("-" * 40)
        found = True

if not found:
    print("Koi matching chunk nahi mila.")
