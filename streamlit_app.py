import streamlit as st
import requests

st.title("🌍 Detect Public IP")

if st.button("Get My Public IP"):
    try:
        ip = requests.get("https://api.ipify.org").text.strip()
        st.success(f"Your public IP is: {ip}")
    except:
        st.error("Could not fetch public IP.")
