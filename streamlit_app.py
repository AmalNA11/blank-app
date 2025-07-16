import streamlit as st
import requests

st.title("Client IP Finder")

# Fetch the client's IP using a third-party service
try:
    ip = requests.get('https://api.ipify.org').text
    st.write(f"Your public IP address is: {ip}")
except Exception as e:
    st.error(f"Could not get IP address: {e}")
