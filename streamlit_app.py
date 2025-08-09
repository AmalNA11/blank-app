import streamlit as st
import random
import time

st.title("Random Stranger Chat 🗨️")

# Mock database of rooms (in real life, store in Firebase or server)
if "rooms" not in st.session_state:
    st.session_state.rooms = {}
if "room_id" not in st.session_state:
    st.session_state.room_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Match user to random room
if st.button("Find Stranger"):
    room_id = random.randint(1000, 9999)
    st.session_state.room_id = room_id
    st.session_state.messages = []
    st.success(f"Connected to stranger in room {room_id}")

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# Chat input
if st.session_state.room_id:
    if prompt := st.chat_input("Say something..."):
        st.session_state.messages.append({"role": "user", "text": prompt})
        st.session_state.messages.append({"role": "assistant", "text": "👋 Stranger replies: Hi there!"})  # Mock reply
