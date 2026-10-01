import streamlit as st
import requests

st.title("My Full-Stack Python App")

st.write("Streamlit Frontend → FastAPI Backend")

name = st.text_input("Enter your name")

if st.button("Send to FastAPI"):

    if name == "":
        st.warning("Please enter your name.")

    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/greet",
                json={"name": name}
            )

            if response.status_code == 200:
                data = response.json()
                st.success(data["message"])

            else:
                st.error(
                    f"API Error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to FastAPI server.")