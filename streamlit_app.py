import streamlit as st
import requests

st.title("Client IP Finder")

# Fetch the client's IP using a third-party service
try:
    ip = requests.get('https://api.ipify.org').text
    st.write(f"Your public IP address is: {ip}")
    ip2 = ip = requests.get("https://ipinfo.io/ip").text.strip()
    st.write(f"IP using ipinfo: {ip2}")

except Exception as e:
    st.error(f"Could not get IP address: {e}")
