import streamlit as st
import requests
import db

st.title("Log My IP")

# Initialize database
db.init_db()

# Button to fetch and log IP
if st.button("Get and Log My IP"):
    try:
        ip = requests.get("https://ipinfo.io/ip").text.strip()
        db.log_ip(ip)
        st.success(f"Your IP has been logged: {ip}")
    except Exception as e:
        st.error(f"Error getting IP: {e}")

# Optional: View logs
if st.checkbox("Show visitor log"):
    logs = db.get_logs()
    for ip, ts in logs:
        st.write(f"{ip} at {ts}")
