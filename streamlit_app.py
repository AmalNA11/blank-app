import streamlit as st
import streamlit.components.v1 as components
import db
from datetime import datetime

st.title("Client IP Logger")

# Inject JavaScript to fetch client IP from browser
components.html("""
    <script>
        fetch("https://api.ipify.org?format=json")
            .then(response => response.json())
            .then(data => {
                const ip = data.ip;
                window.parent.postMessage({ type: 'IP_ADDRESS', ip: ip }, "*");
            });
    </script>
""", height=0)

# Placeholder to display and store IP
ip = st.empty()

# Read IP from frontend
js_ip_key = "client_ip"
if js_ip_key not in st.session_state:
    st.session_state[js_ip_key] = None

# Receive IP from frontend message
message = st.experimental_get_query_params()
if "ip" in message:
    st.session_state[js_ip_key] = message["ip"][0]

# Callback to receive posted message from JavaScript
def on_ip_received():
    import streamlit_javascript as stj
    events = stj.streamlit_js_events()
    if "ip" in events.get("IP_ADDRESS", {}):
        st.session_state[js_ip_key] = events["IP_ADDRESS"]["ip"]

# Show IP and log it
if st.session_state[js_ip_key]:
    ip_address = st.session_state[js_ip_key]
    st.success(f"Your real IP: {ip_address}")
    db.log_ip(ip_address)
else:
    st.info("Waiting for your real IP...")

# Optional: Show log
if st.checkbox("Show visitor log"):
    logs = db.get_logs()
    for row in logs:
        st.write(f"{row[0]} at {row[1]}")
