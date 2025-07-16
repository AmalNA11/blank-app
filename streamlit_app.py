# import streamlit as st
# import requests
#
# st.title("Client IP Finder")
#
# # Fetch the client's IP using a third-party service
# try:
#     ip = requests.get('https://api.ipify.org').text
#     st.write(f"Your public IP address is: {ip}")
#     ip2 = ip = requests.get("https://ipinfo.io/ip").text.strip()
#     st.write(f"IP using ipinfo: {ip2}")
#
# except Exception as e:
#     st.error(f"Could not get IP address: {e}")
import streamlit as st
import requests
import db

st.title("IP Logger App")

# Initialize DB on first run
db.init_db()

# Get IP
try:
    ip = requests.get("https://ipinfo.io/ip").text.strip()
except:
    ip = "Unknown"

# Log IP
db.log_ip(ip)
st.success(f"Your IP: {ip}")

# Optional: Show logs
if st.checkbox("Show visitor logs"):
    logs = db.get_logs()
    for row in logs:
        st.write(f"{row[0]} at {row[1]}")
