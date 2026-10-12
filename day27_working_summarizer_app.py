
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_article_text(url):
    """Extract readable text from a public article webpage."""

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        raise ValueError("Please enter a valid HTTP or HTTPS URL.")

    # Fetch webpage HTML
    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    # Parse HTML
        # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove irrelevant page elements
    for element in soup([
        "script", "style", "nav", "footer",
        "header", "aside", "form"
    ]):
        element.decompose()

    # Try common article-content containers
    article = (
        soup.find("article")
        or soup.find("main")
        or soup.find(attrs={"itemprop": "articleBody"})
    )

    if article:
        text = article.get_text(separator=" ", strip=True)
    else:
        paragraphs = soup.find_all("p")
        text = " ".join(
            p.get_text(" ", strip=True)
            for p in paragraphs
        )

    if len(text) < 100:
        raise ValueError(
            "Not enough readable text found. "
            "The page may require JavaScript or login."
        )

    return text


# 1. Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# 2. Configure the app
st.set_page_config(
    page_title="AI Article Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Article Summarizer")
st.write("Paste an article and generate an AI-powered summary.")

# 3. Check API key
if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

# 4. Create Gemini client
client = genai.Client(api_key=api_key)

st.subheader("Choose Your Article Source")

input_method = st.radio(
    "How would you like to provide the article?",
    ["Paste Text", "Article URL"]
)

article = ""

if input_method == "Paste Text":
    article = st.text_area(
        "Paste your article here",
        height=250,
        placeholder="Paste a news article or blog post..."
    )

else:
    article_url = st.text_input(
        "Enter article URL",
        placeholder="https://example.com/article"
    )

    if st.button("Extract Article"):
        try:
            with st.spinner("Extracting article text..."):
                extracted_text = extract_article_text(article_url)

            st.session_state["extracted_article"] = extracted_text
            st.success("Article extracted successfully!")

        except (requests.RequestException, ValueError) as e:
            st.error(f"Could not extract article: {e}")

    article = st.session_state.get("extracted_article", "")
    if article:
        st.text_area(
            "Extracted article preview",
            value=article,
            height=200,
            disabled=True
        )


# 5. Get article from the user
article = st.text_area(
    "Paste your article here",
    height=250,
    placeholder="Paste a news article, blog post, or other text..."
)

# 6. Let the user select summary length
summary_length = st.selectbox(
    "Choose summary length",
    ["Short", "Medium", "Detailed"]
)

# 7. Let the user select output language
language = st.selectbox(
    "Choose output language",
    ["English", "Urdu", "Roman Urdu"]
)

# 8. Generate summary
if st.button("Generate Summary", type="primary"):

    if not article.strip():
        st.warning("Please paste an article first.")

    else:
        length_instructions = {
            "Short": "Write 3 concise bullet points.",
            "Medium": "Write a short paragraph and 5 key points.",
            "Detailed": "Write a detailed summary and 7 key points."
        }

        prompt = f"""
You are a professional article summarization assistant.

TASK:
Summarize the article provided below.

INSTRUCTIONS:
1. Use simple, clear language.
2. Preserve the important facts and main ideas.
3. Do not invent facts or unsupported information.
4. Avoid unnecessary repetition.
5. If information is unclear, do not guess.
6. Write the output in {language}.
7. {length_instructions[summary_length]}

OUTPUT FORMAT:
## Summary
Provide the summary here.

## Key Points
Provide the key points here.

ARTICLE:
<article>
{article}
</article>
"""

        try:
            with st.spinner("Generating your summary..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            if response.text:
                st.subheader("Your Summary")
                st.markdown(response.text)
            else:
                st.warning("The model returned an empty response.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
