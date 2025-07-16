import streamlit as st
import streamlit.components.v1 as components
import db

st.set_page_config(page_title="IP Logger", page_icon="🌐")
st.title("🌐 Your Public IP")

# Inject JavaScript to get IP from client
components.html("""
    <script>
        fetch("https://api.ipify.org?format=json")
            .then(res => res.json())
            .then(data => {
                const ip = data.ip;
                const queryString = new URLSearchParams({ ip }).toString();
                const newUrl = window.location.pathname + "?" + queryString;
                window.location.href = newUrl;
            });
    </script>
""", height=0)

# Get IP from query parameters (uses updated API)
params = st.query_params
client_ip = params.get("ip", None)

if client_ip:
    st.success(f"Your IP address is: `{client_ip}`")

    if "ip_logged" not in st.session_state:
        db.log_ip(client_ip)
        st.session_state.ip_logged = True
else:
    st.info("Fetching your IP...")

# Show log (optional)
if st.checkbox("Show IP log"):
    logs = db.get_logs()
    st.write("### IP Log")
    for ip, ts in logs:
        st.write(f"`{ip}` at *{ts}*")
