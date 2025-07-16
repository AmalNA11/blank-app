import streamlit as st
import streamlit.components.v1 as components

st.title("🔍 Detect Your Local IP (LAN)")

st.info("This attempts to detect your private/local IP address using WebRTC. May not work on all browsers.")

# JavaScript code to extract local IP using WebRTC
components.html(
    """
    <script>
    async function getLocalIP() {
        const pc = new RTCPeerConnection({iceServers: []});
        pc.createDataChannel("");
        pc.createOffer().then(offer => pc.setLocalDescription(offer));

        pc.onicecandidate = event => {
            if (!event || !event.candidate) return;
            const ipRegex = /([0-9]{1,3}(\\.[0-9]{1,3}){3})/;
            const ipMatch = event.candidate.candidate.match(ipRegex);
            if (ipMatch) {
                const ip = ipMatch[1];
                document.body.innerHTML = `<h3>Your Local IP: <code>${ip}</code></h3>`;
                // You could also pass this back via Streamlit query params or other bridge if needed
                pc.close();
            }
        };
    }

    getLocalIP();
    </script>
    """,
    height=100,
)
