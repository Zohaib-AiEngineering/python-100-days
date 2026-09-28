import streamlit as st
import pandas as pd

st.title("CSV Data Viewer")

st.write("Upload a CSV file and view its data.")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file:
    st.write("File uploaded successfully!")

    df = pd.read_csv(uploaded_file)

    st.dataframe(df)