import chromadb

client = chromadb.EphemeralClient()
collection = client.create_collection(name="vector_write_test")

print("STEP 1: Adding vector...", flush=True)

collection.add(
    ids=["vector1"],
    embeddings=[[1.0, 0.0, 0.0]]
)

print("STEP 2: Vector added!", flush=True)
print("Total records:", collection.count(), flush=True)