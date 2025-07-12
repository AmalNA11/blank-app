import streamlit as st
import subprocess
import os

st.title("🎈 My new app.........")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Clone private repo using the GitHub token
token = st.secrets["GITHUB_TOKEN"]
username = "AmalNA11"
repo = "blank-app"
clone_url = f"https://{token}:x-oauth-basic@github.com/{username}/{repo}.git"

# Clone into /tmp so it's writable in Streamlit Cloud
repo_path = f"/tmp/{repo}"

if not os.path.exists(repo_path):
    subprocess.run(["git", "clone", clone_url, repo_path], check=True)
    st.success("Private repo cloned successfully!")
else:
    st.info("Repo already cloned.")

# Optional: list files to confirm
files = os.listdir(repo_path)
st.write("Files in repo:", files)
