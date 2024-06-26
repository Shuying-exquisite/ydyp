import streamlit as st
with open("Operationdocument.md", "r", encoding="utf-8") as file:
    markdown_text = file.read()
st.markdown(markdown_text)
