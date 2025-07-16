import streamlit as st
import requests

st.title("Remote Print to My Local Printer")

# Replace this with your ngrok URL
PRINTER_BRIDGE_URL = "http://192.168.228.55:5000/print"

text_to_print = st.text_area("Enter text to print")

if st.button("Print"):
    if text_to_print.strip():
        try:
            response = requests.post(
                PRINTER_BRIDGE_URL,
                json={"text": text_to_print},
                timeout=5
            )
            if response.ok:
                st.success("Sent to your local printer successfully!")
            else:
                st.error(f"Printer error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to local printer bridge.\n\n{e}")
    else:
        st.warning("Please enter some text first.")
