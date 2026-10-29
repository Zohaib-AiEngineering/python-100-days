from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Sample documents
documents = [
    Document(page_content="Python is a programming language."),
    Document(page_content="Embeddings represent text as numerical vectors."),
    Document(page_content="FastAPI is used to build APIs.")
]

# Create Chroma vector database
vectorstore = Chroma(
    collection_name="day37_rag_demo",
    embedding_function=embeddings
)

# Store documents in the database
vectorstore.add_documents(documents)

# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# Test retriever
question = "What is Python?"
results = retriever.invoke(question)

print("\nRelevant documents:")
for doc in results:
    print("-", doc.page_content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
""")

print("Prompt template created successfully!")
