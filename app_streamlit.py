import streamlit as st
from summariser import summarise_text_local

st.title("Summarisation Agent 📝")

st.write("Enter your text below to get a concise summary and key points.")

# Input box
input_text = st.text_area("Input Text", height=200)

if st.button("Summarise"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarise_text_local(input_text)
        st.success("Here is your summary:")
        st.write(summary)
