
import chromadb

# 1. Create an in-memory ChromaDB client
client = chromadb.Client()

# 2. Create a collection
collection = client.create_collection(
    name="ai_learning"
)

# 3. Add documents, IDs, and metadata
collection.add(
    ids=["doc1", "doc2", "doc3"],
    documents=[
        "Python is useful for AI.",
        "Machine learning learns from data.",
        "Neural networks learn complex patterns."
    ],
    metadatas=[
        {"topic": "Python", "level": "beginner"},
        {"topic": "ML", "level": "beginner"},
        {"topic": "Deep Learning", "level": "advanced"}
    ]
)


# Check whether documents were added
print("Total documents:", collection.count())

# Check stored documents and metadata
print("Stored data:", collection.get())

# Run the query
results = collection.query(
    query_texts=["How can I start learning AI?"],
    n_results=2,
    where={"level": "beginner"}
)

# Inspect the complete result
print("Full query result:", results)
print("Retrieved documents:", results["documents"])

# Print documents safely
for group in results["documents"]:
    for document in group:
        print("-", document)
