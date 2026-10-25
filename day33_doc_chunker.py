
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("Total pages:", len(documents))

# Step 2: Create text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

# Step 3: Split PDF documents into chunks
chunks = splitter.split_documents(documents)

print("Total chunks:", len(chunks))

# Step 4: Display chunks
for i, chunk in enumerate(chunks, start=1):
    page = chunk.metadata.get("page")

    print(f"\nChunk {i}")
    print("Page:", page + 1 if page is not None else "Unknown")
    print(chunk.page_content)
