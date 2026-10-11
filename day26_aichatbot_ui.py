import streamlit as st
from google import genai 
from dotenv import load_dotenv

import os
load_dotenv(dotenv_path=".env", override=True)
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= api_key)
st.title("MY AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
question = st.chat_input("Ask me anything:")

if question:
    # Show and save user's question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    try:
        with st.spinner("AI is thinking..."):
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=question
            )

        answer = response.text

        # Save and display AI's answer
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.write(answer)

    except Exception:
        st.error(
            "AI server is temporarily unavailable. "
            "Please try again in a few seconds."
        )
