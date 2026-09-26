import io
import re
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# 1. Page Configuration (Wide Layout)
st.set_page_config(
    page_title="ResumeOptimizer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS to Match the Exact Design
st.markdown("""
<style>
    /* Base styling and background */
    .stApp {
        background-color: #f4f7fc;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Hide default Streamlit headers to use our custom navbar */
    header[data-testid="stHeader"] {
        display: none;
    }
    .block-container {
        padding-top: 0rem !important;
        max-width: 1200px;
    }

    /* Top Dark Navbar */
    .custom-navbar {
        background-color: #0d132a;
        color: white;
        padding: 12px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        z-index: 99999;
    }
    .nav-logo { font-size: 1.2rem; font-weight: 700; display: flex; align-items: center; gap: 8px;}
    .nav-tagline { font-size: 0.85rem; color: #a1a1aa; margin-left: 30px;}
    .nav-right { display: flex; align-items: center; gap: 15px; }
    .ai-badge { background: linear-gradient(90deg, #4f46e5, #9333ea); padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;}

    /* Space below absolute navbar */
    .spacer { height: 100px; }

    /* Main Title Section */
    .hero-section { text-align: center; margin-bottom: 2rem; position: relative;}
    .hero-badge { display: inline-block; background: #e0e7ff; color: #4338ca; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; margin-bottom: 10px;}
    .main-title { 
        font-size: 2.2rem; 
        font-weight: 800; 
        background: linear-gradient(90deg, #1e3a8a, #7e22ce); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title { color: #64748b; font-size: 0.95rem; }
    
    /* Features Row */
    .features-row {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .feature-item { display: flex; align-items: center; gap: 10px; text-align: left;}
    .f-icon { width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 1.1rem; }
    .f-icon.blue { background: #e0e7ff; color: #4338ca; }
    .f-icon.green { background: #dcfce7; color: #15803d; }
    .f-icon.purple { background: #f3e8ff; color: #7e22ce; }
    .f-icon.red { background: #fee2e2; color: #b91c1c; }
    .f-text-title { font-size: 0.85rem; font-weight: 700; color: #1e293b; margin:0;}
    .f-text-sub { font-size: 0.75rem; color: #64748b; margin:0;}

    /* Unified White Card Container */
    .main-card {
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        padding: 30px;
        border: 1px solid #f1f5f9;
    }

    /* Column Headers */
    .col-header-container { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;}
    .col-header-left { display: flex; align-items: center; gap: 10px; }
    .circle-num { background: #4f46e5; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 0.9rem; font-weight: bold;}
    .col-title { font-weight: 700; color: #0f172a; margin: 0; font-size: 1rem;}
    .col-subtitle { color: #64748b; font-size: 0.75rem; margin: 0;}
    .col-icon { color: #4f46e5; background: #e0e7ff; padding: 6px; border-radius: 6px;}

    /* Info Boxes */
    .info-box { border-radius: 8px; padding: 12px 15px; display: flex; align-items: flex-start; gap: 10px; margin-top: 15px; }
    .info-box.green { background: #f0fdf4; border: 1px solid #bbf7d0; }
    .info-box.blue { background: #eff6ff; border: 1px solid #bfdbfe; }
    .info-box-title { font-size: 0.85rem; font-weight: 700; margin: 0;}
    .info-box-green-title { color: #166534; }
    .info-box-blue-title { color: #1e40af; }
    .info-box-text { font-size: 0.75rem; color: #475569; margin: 0;}

    /* Streamlit Button Override (Full width Gradient) */
    div.stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #3b82f6, #9333ea) !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 12px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(147, 51, 234, 0.3) !important;
        margin-top: 20px !important;
        transition: opacity 0.2s;
    }
    div.stButton > button:hover {
        opacity: 0.9 !important;
    }

    /* Style Streamlit Inputs to match design */
    div[data-testid="stFileUploader"] {
        border: 2px dashed #cbd5e1;
        border-radius: 12px;
        padding: 15px;
        background: #f8fafc;
        text-align: center;
    }
    div[data-baseweb="textarea"] > div {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# 3. HTML Navbar injected absolutely
st.markdown("""
<div class="custom-navbar">
    <div style="display: flex; align-items: center;">
        <div class="nav-logo">📑 ResumeOptimizer</div>
        <div class="nav-tagline">Smarter Resumes. Better Opportunities.</div>
    </div>
    <div class="nav-right">
        <div class="ai-badge">🚀 AI Powered</div>
        <div style="font-size: 1.2rem;">⚙️</div>
    </div>
</div>
<div class="spacer"></div>
""", unsafe_allow_html=True)

# 4. Hero Section & Features
# 4. Hero Section & Features
st.markdown("""
<div class="hero-section">
<div class="hero-badge">✨ AI Resume Analysis</div>
<div class="main-title">🎯 Smart Resume Matcher & ATS Optimizer</div>
<div class="sub-title">Compare your CV against job requirements using enterprise TF-IDF natural language processing.</div>
<div class="features-row">
<div class="feature-item">
<div class="f-icon blue">⚡</div>
<div><p class="f-text-title">AI-Powered Analysis</p><p class="f-text-sub">Smart matching & scoring</p></div>
</div>
<div class="feature-item">
<div class="f-icon green">🛡️</div>
<div><p class="f-text-title">ATS Friendly</p><p class="f-text-sub">Beats Applicant Tracking Systems</p></div>
</div>
<div class="feature-item">
<div class="f-icon purple">📄</div>
<div><p class="f-text-title">Detailed Insights</p><p class="f-text-sub">Know what to improve</p></div>
</div>
<div class="feature-item">
<div class="f-icon red">🎯</div>
<div><p class="f-text-title">Get Hired Faster</p><p class="f-text-sub">Tailored for your dream job</p></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# 5. Helper Functions for Logic
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# 6. Main White Card Container (Simulated with Columns)
st.markdown('<div class="main-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="col-header-container">
        <div class="col-header-left">
            <div class="circle-num">1</div>
            <div><p class="col-title">Candidate Resume</p><p class="col-subtitle">Upload your CV in PDF format</p></div>
        </div>
        <div class="col-icon">📄</div>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
    
    st.markdown("""
    <div class="info-box green">
        <div style="font-size: 1.2rem; color: #166534;">✅</div>
        <div>
            <p class="info-box-title info-box-green-title">Ready to upload your resume</p>
            <p class="info-box-text">Your file will be securely processed and analyzed.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="col-header-container">
        <div class="col-header-left">
            <div class="circle-num">2</div>
            <div><p class="col-title">Target Job Description</p><p class="col-subtitle">Paste the job requirements below</p></div>
        </div>
        <div class="col-icon">📋</div>
    </div>
    """, unsafe_allow_html=True)
    
    job_desc = st.text_area("", height=210, placeholder="Paste responsibilities, qualifications, and required tech stack...", label_visibility="collapsed")
    
    st.markdown("""
    <div class="info-box blue">
        <div style="font-size: 1.2rem; color: #1e40af;">💡</div>
        <div>
            <p class="info-box-title info-box-blue-title">Pro Tip</p>
            <p class="info-box-text">Include key skills, experience, and job details for more accurate matching.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Full Width Button Logic
if st.button("🚀 Analyze Compatibility Score →"):
    if uploaded_file and job_desc.strip():
        with st.spinner("Processing NLP Embeddings..."):
            resume_raw_text = extract_text_from_pdf(uploaded_file)
            resume_clean = clean_text(resume_raw_text)
            job_clean = clean_text(job_desc)

            vectorizer = TfidfVectorizer(stop_words="english")
            tfidf_matrix = vectorizer.fit_transform([resume_clean, job_clean])
            similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            match_score = float(similarity_matrix[0][0]) * 100
            
            st.success(f"### 🎉 Compatibility Score: {match_score:.1f}%")
            st.progress(int(match_score))
    else:
        st.error("Please provide both Resume and Job Description!")

st.markdown('</div>', unsafe_allow_html=True)