import streamlit as st
import requests

st.title("🖨️ Remote Print to My Local Printer")

# Input for Printer Bridge URL
st.subheader("🔗 Configure Printer Bridge URL")
printer_bridge_url = st.text_input(
    "Enter your local printer bridge URL (e.g. https://xxxx.trycloudflare.com/print):",
    placeholder="https://your-url.com/print"
)

# Input for Printer Name
st.subheader("🖨️ Printer Name")
printer_name = st.text_input(
    "Enter your printer name (e.g. PDF, HP_LaserJet, etc.):",
    placeholder="PDF"
)

# Input text to print
st.subheader("📝 Text to Print")
text_to_print = st.text_area("Enter the text you want to send to your printer:")

# Submit
if st.button("🖨️ Print"):
    if not printer_bridge_url.strip():
        st.error("Please enter your printer bridge URL.")
    elif not printer_name.strip():
        st.error("Please enter your printer name.")
    elif not text_to_print.strip():
        st.warning("Please enter some text to print.")
    else:
        try:
            response = requests.post(
                printer_bridge_url,
                json={
                    "text": text_to_print,
                    "printer": printer_name
                },
                timeout=5
            )
            if response.ok:
                st.success("✅ Sent to your local printer successfully!")
            else:
                st.error(f"❌ Printer error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"🚫 Failed to connect to the printer bridge.\n\n{e}")
