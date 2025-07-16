import streamlit as st
import requests
import db

st.title("Log My IP")

# Initialize database
db.init_db()

# Button to fetch and log IP
if st.button("Log My IP"):
    try:
        ip = requests.get("https://ipinfo.io/ip", timeout=3).text.strip()
        st.success(f"Your IP is: {ip}")
        db.log_ip(ip)
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please check your internet connection.")
    except Exception as e:
        st.error(f"Error: {e}")

# Optional: View logs
if st.checkbox("Show visitor log"):
    logs = db.get_logs()
    for ip, ts in logs:
        st.write(f"{ip} at {ts}")
