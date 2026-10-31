
import math
import hashlib
import time
import os
from io import BytesIO

import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

# =====================================
# PREMIUM UI DESIGN
# =====================================

st.set_page_config(
    page_title="Smart Doc-Talker",
    page_icon="📄",
    layout="wide"
)


st.markdown("""
<style>

/* =================================
   STREAMLIT HEADER
================================= */

header[data-testid="stHeader"] {
    background: transparent !important;
}

/* =================================
   MAIN BACKGROUND
================================= */

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background:
        radial-gradient(ellipse at 15% 20%, rgba(0, 180, 255, 0.16), transparent 35%),
        radial-gradient(ellipse at 85% 75%, rgba(145, 40, 255, 0.18), transparent 35%),
        linear-gradient(135deg, #050b20, #080d27 55%, #100b2c) !important;
    color: #f0f4ff;
}

/* =================================
   MAIN CONTENT WIDTH
================================= */

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* =================================
   HEADINGS
================================= */

h1, h2, h3 {
    color: #eaf4ff !important;
    font-weight: 750 !important;
}

/* =================================
   HERO SECTION
================================= */

.hero {
    text-align: center;
    padding: 25px 15px 30px;
    margin-bottom: 20px;
}

.hero-icon {
    font-size: 48px;
    filter: drop-shadow(0 0 12px #00eaff);
}

.hero-title {
    font-size: 42px;
    font-weight: 850;
    letter-spacing: -1px;
    background: linear-gradient(90deg, #ffffff, #7eeaff, #c9a0ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 8px 0;
}

.hero-subtitle {
    color: #aabbd8;
    font-size: 16px;
}

/* =================================
   PDF UPLOADER
================================= */

div[data-testid="stFileUploader"] {
    background: rgba(15, 30, 65, 0.65);
    border: 1px solid rgba(0, 220, 255, 0.55);
    border-radius: 18px;
    padding: 18px;
    box-shadow:
        0 0 15px rgba(0, 220, 255, 0.12),
        inset 0 0 20px rgba(80, 80, 255, 0.08);
    color: #eaf4ff;
}

div[data-testid="stFileUploaderDropzone"] {
    background: rgba(10, 20, 48, 0.95) !important;
    border: 1px dashed #00d9ff;
    border-radius: 14px;
}

div[data-testid="stFileUploaderDropzone"] * {
    color: #eaf4ff !important;
}

/* =================================
   BUTTONS
================================= */

.stButton > button {
    background: linear-gradient(110deg, #087cff, #8c35ed);
    color: white !important;
    border: 1px solid rgba(130, 220, 255, 0.6);
    border-radius: 12px;
    padding: 9px 22px;
    font-weight: 700;
    box-shadow: 0 0 15px rgba(0, 180, 255, 0.25);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    border-color: #00eeff;
    box-shadow: 0 0 24px rgba(0, 220, 255, 0.55);
    transform: translateY(-2px);
}

/* =================================
   CHAT INPUT
================================= */

div[data-testid="stBottom"] {
    background: #080e25 !important;
}

div[data-testid="stChatInput"] {
    border: 1px solid rgba(0, 220, 255, 0.65);
    border-radius: 15px;
    background: rgba(15, 30, 65, 0.95);
    box-shadow: 0 0 16px rgba(0, 180, 255, 0.18);
}

div[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: white !important;
}

/* =================================
   CHAT MESSAGES
================================= */

div[data-testid="stChatMessage"] {
    background: rgba(20, 35, 75, 0.55);
    border: 1px solid rgba(100, 160, 255, 0.18);
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 12px;
}

/* =================================
   EXPANDERS
================================= */

div[data-testid="stExpander"] {
    background: rgba(15, 25, 58, 0.65);
    border: 1px solid rgba(100, 150, 255, 0.3);
    border-radius: 13px;
}

/* =================================
   ALERTS
================================= */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* =================================
   GENERAL TEXT
================================= */

p, label, span {
    color: #d5e3fa;
}

/* =================================
   DIVIDERS
================================= */

hr {
    border-color: rgba(0, 210, 255, 0.25);
}

/* Force dark uploader background */
div[data-testid="stFileUploader"] section,
div[data-testid="stFileUploader"] section > div,
div[data-testid="stFileUploaderDropzone"],
div[data-testid="stFileUploaderDropzone"] > div {
    background: #101d40 !important;
    color: #eaf4ff !important;
}

/* Uploader buttons and text */
div[data-testid="stFileUploader"] button {
    background: #172b52 !important;
    color: #ffffff !important;
    border: 1px solid #00d9ff !important;
}

/* Remove white chat footer background */
[data-testid="stBottom"],
[data-testid="stBottom"] > div,
[data-testid="stBottom"] > div > div {
    background: #080e25 !important;
}

/* Chat input */
[data-testid="stChatInput"] {
    background: #101d40 !important;
    border: 1px solid #00d9ff !important;
    border-radius: 15px !important;
}

[data-testid="stChatInput"] textarea {
    color: white !important;
    background: transparent !important;
}

/* Statistics dashboard cards */

.stats-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin: 22px 0;
}

.stat-card {
    background: linear-gradient(
        145deg,
        rgba(15, 35, 75, 0.95),
        rgba(30, 20, 70, 0.9)
    );
    border: 1px solid rgba(0, 220, 255, 0.5);
    border-radius: 16px;
    padding: 22px 12px;
    text-align: center;
    box-shadow: 0 0 18px rgba(0, 200, 255, 0.12);
    transition: 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(0, 220, 255, 0.35);
}

.stat-icon {
    font-size: 28px;
    margin-bottom: 8px;
}

.stat-value {
    font-size: 30px;
    font-weight: 800;
    color: #72eaff;
    text-shadow: 0 0 12px rgba(0, 220, 255, 0.5);
}

.stat-label {
    color: #b7c9e8;
    font-size: 14px;
    margin-top: 6px;
}

@media (max-width: 650px) {
    .stats-container {
        grid-template-columns: 1fr;
    }
}




/* Keep app content above the animation */
.stApp [data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 1;
}

/* =====================================
   FUTURISTIC MOVING NEURAL NETWORK
===================================== */

/* Keep background layers transparent */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: transparent !important;
}

/* Base background */
.stApp {
    background:
        linear-gradient(135deg, #050b20, #080d27 55%, #100b2c) !important;
    position: relative;
}

/* Animated neuron network */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;

    background-image:
        radial-gradient(circle, #00eaff 2px, transparent 3px),
        radial-gradient(circle, #a855f7 2px, transparent 3px),
        radial-gradient(circle, #00eaff 3px, transparent 4px),
        linear-gradient(45deg, transparent 49.7%, rgba(0,220,255,.4) 50%, transparent 50.3%),
        linear-gradient(-45deg, transparent 49.7%, rgba(168,85,247,.35) 50%, transparent 50.3%);

    background-size:
        100px 100px,
        150px 150px,
        220px 220px,
        100px 100px,
        150px 150px;

    background-position:
        0 0, 50px 50px, 100px 100px, 0 0, 50px 50px;

    animation: neuronTravel 18s linear infinite;
    opacity: 0.65;
}

/* Glowing neuron light */
.stApp::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;

    background:
        radial-gradient(circle at 20% 30%, rgba(0,234,255,.2), transparent 20%),
        radial-gradient(circle at 80% 60%, rgba(168,85,247,.2), transparent 22%),
        radial-gradient(circle at 50% 90%, rgba(0,150,255,.15), transparent 20%);

    animation: neuronPulse 5s ease-in-out infinite alternate;
}

/* Keep app content above animation */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    position: relative;
    z-index: 1;
}

@keyframes neuronTravel {
    from {
        background-position:
            0 0, 50px 50px, 100px 100px, 0 0, 50px 50px;
    }

    to {
        background-position:
            300px 300px, -250px 250px, 400px -300px,
            300px 300px, -250px 250px;
    }
}

@keyframes neuronPulse {
    from { opacity: 0.3; }
    to { opacity: 1; }
}


</style>
""", unsafe_allow_html=True)

# =====================================
# 1. Configuration
# =====================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found. Check your .env file.")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)


# =====================================
# 2. Cosine Similarity
# =====================================

def cosine_similarity(a, b):

    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


# =====================================
# 3. Initialize Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "active_pdf_id" not in st.session_state:
    st.session_state.active_pdf_id = None


# =====================================
# 4. Streamlit Interface
# =====================================
st.markdown("""
<div class="hero">
    <div class="hero-icon">📄</div>
    <div class="hero-title">Smart Doc-Talker</div>
    <div class="hero-subtitle">
        Your Intelligent AI PDF Assistant
        <br>
        Upload • Understand • Ask • Discover
    </div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


# =====================================
# 5. PDF Processing
# =====================================

if uploaded_file:

    # Validate file size
    if uploaded_file.size == 0:
        st.error("Uploaded PDF is empty.")
        st.stop()

    if uploaded_file.size > 10 * 1024 * 1024:
        st.error("PDF size must be less than 10 MB.")
        st.stop()

    # Detect PDF changes
    current_file_id = hashlib.md5(
        uploaded_file.getvalue()
    ).hexdigest()

    if st.session_state.active_pdf_id != current_file_id:

        st.session_state.messages = []

        st.session_state.active_pdf_id = current_file_id

        # Clear previous PDF data
        st.session_state.pop("pdf_file_id", None)
        st.session_state.pop("pdf_chunks", None)
        st.session_state.pop("chunk_vectors", None)

        st.info("New PDF detected. Previous data cleared.")

    # Extract PDF text
    try:

        pdf_bytes = BytesIO(uploaded_file.getvalue())
        reader = PdfReader(pdf_bytes)

        if reader.is_encrypted:
            st.error("This PDF is password protected.")
            st.stop()

        full_text = ""

        for page_number, page in enumerate(
            reader.pages, start=1
        ):

            page_text = page.extract_text()

            if page_text:
                full_text += page_text + "\n"

    except Exception as e:

        st.error(f"PDF processing failed: {e}")
        st.stop()

    # Check extracted content
    if not full_text.strip():

        st.warning(
            "No readable text found. This may be a scanned PDF."
        )
        st.stop()

    st.success("PDF text extracted successfully!")

    # =====================================
    # 6. Split PDF into Chunks
    # =====================================

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(full_text)

    if not chunks:
        st.warning("No text chunks were generated.")
        st.stop()

    
    st.subheader("PDF Text Chunks")


    st.subheader("PDF Text Chunks")

    file_size_mb = uploaded_file.size / (1024 * 1024)

    stats_html = f"""
<div class="stats-container">
<div class="stat-card">
<div class="stat-icon">📑</div>
<div class="stat-value">{len(reader.pages)}</div>
<div class="stat-label">PDF Pages</div>
</div>
<div class="stat-card">
<div class="stat-icon">🧩</div>
<div class="stat-value">{len(chunks)}</div>
<div class="stat-label">Total Chunks</div>
</div>
<div class="stat-card">
<div class="stat-icon">💾</div>
<div class="stat-value">{file_size_mb:.2f} MB</div>
<div class="stat-label">File Size</div>
</div>
</div>
"""

    st.markdown(stats_html, unsafe_allow_html=True)

    with st.expander("View Text Chunks"):

        for i, chunk in enumerate(chunks):

            st.write(f"Chunk {i + 1}")
            st.write(chunk)
            st.divider()

    st.write("File Name:", uploaded_file.name)

    with st.expander("View PDF Text"):

        st.text_area(
            "Extracted Content",
            full_text,
            height=200
        )

    # =====================================
    # 7. Generate PDF Embeddings
    # =====================================

    if st.session_state.get("pdf_file_id") != current_file_id:

        with st.spinner("Creating PDF embeddings..."):

            try:

                chunk_vectors = embeddings.embed_documents(
                    chunks
                )

                st.session_state.pdf_chunks = chunks
                st.session_state.chunk_vectors = chunk_vectors
                st.session_state.pdf_file_id = current_file_id

                st.success("PDF embeddings created successfully!")

            except Exception as e:

                st.error(f"Embedding error: {e}")
                st.stop()

    # =====================================
    # 8. Chat Interface
    # =====================================

    st.subheader("Chat with your PDF")

    if st.button("Clear Chat"):

        st.session_state.messages = []
        st.rerun()

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User question
    question = st.chat_input(
        "Ask another question about your PDF..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        # =====================================
        # 9. Semantic Search + Gemini
        # =====================================

        with st.spinner("AI is thinking..."):

            try:

                # Convert question into embedding
                question_vector = embeddings.embed_query(
                    question
                )

                # Compare question with PDF chunks
                scores = []

                for i, chunk_vector in enumerate(
                    st.session_state.chunk_vectors
                ):

                    score = cosine_similarity(
                        question_vector,
                        chunk_vector
                    )

                    scores.append((score, i))

                # Sort by similarity
                scores.sort(reverse=True)

                # Select top 2 relevant chunks
                top_chunks = [
                    st.session_state.pdf_chunks[i]
                    for score, i in scores[:2]
                ]

                context = "\n\n".join(top_chunks)

                # Create prompt
                prompt = f"""
                Answer the user's question using only
                the PDF context below.

                PDF CONTEXT:
                {context}

                USER QUESTION:
                {question}

                If the answer is not available in the
                context, clearly say that the PDF does
                not contain this information.
                """

                # =====================================
                # 10. Gemini Retry System
                # =====================================

                ai_answer = None

                for attempt in range(3):

                    try:

                        response = llm.invoke(prompt)
                        ai_answer = response.text
                        break

                    except Exception as e:

                        error_message = str(e)

                        if (
                            "503" in error_message
                            or "UNAVAILABLE" in error_message
                        ):

                            if attempt < 2:

                                wait_time = 2 ** (attempt + 1)

                                st.warning(
                                    f"Gemini is busy. "
                                    f"Retrying in {wait_time} seconds..."
                                )

                                time.sleep(wait_time)

                            else:

                                st.error(
                                    "Gemini server is busy. "
                                    "Please try again later."
                                )

                        else:
                            raise

                # Save answer
                if ai_answer:

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": ai_answer
                    })

                    st.rerun()

            except Exception as e:

                st.error(f"Error while generating answer: {e}")

else:

    st.info("Please upload a PDF to start chatting.")
