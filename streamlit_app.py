import streamlit as st
import subprocess

st.title("Print to Virtual PDF Printer")

def print_text(text):
    subprocess.run(['lp', '-d', 'Virtual_PDF'], input=text.encode())

text_to_print = st.text_area("Enter text to print")

if st.button("Print"):
    if text_to_print.strip():
        print_text(text_to_print)
        st.success("Sent to Virtual_PDF printer!")
    else:
        st.warning("Please enter some text first.")
