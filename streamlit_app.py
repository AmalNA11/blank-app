import streamlit as st
from streamlit_javascript import st_javascript

st.title("🔍 Detect Your Local IP (Private IP)")

st.info("Trying to detect your device's private/local IP using JavaScript + WebRTC.")

local_ip = st_javascript(
    """
    async () => {
        return await new Promise((resolve, reject) => {
            const pc = new RTCPeerConnection({iceServers: []});
            pc.createDataChannel("");
            pc.createOffer().then(offer => pc.setLocalDescription(offer));

            pc.onicecandidate = event => {
                if (!event || !event.candidate) return;
                const ipRegex = /([0-9]{1,3}(\\.[0-9]{1,3}){3})/;
                const ipMatch = event.candidate.candidate.match(ipRegex);
                if (ipMatch) {
                    resolve(ipMatch[1]);
                    pc.close();
                }
            };

            setTimeout(() => resolve(null), 3000); // Fallback timeout
        });
    }
    """
)

if local_ip:
    st.success(f"Your Local IP Address is: {local_ip}")
else:
    st.warning("Could not detect local IP. Try a different browser or local deployment.")
