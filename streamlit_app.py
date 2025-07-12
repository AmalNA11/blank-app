import streamlit as st
import subprocess
import os

# Use GitHub token to clone a private repo
token = st.secrets["GITHUB_TOKEN"]
username = "AmalNA11"
repo_name = "blank-app"
repo_path = f"/tmp/{repo_name}"

if not os.path.exists(repo_path):
    private_repo_url = f"https://{token}:x-oauth-basic@github.com/{username}/{repo_name}.git"
    # subprocess.run(["git", "clone", private_repo_url, repo_path], check=True)
    st.success(f"Cloned private repo `{repo_name}` successfully.")
else:
    st.info(f"Repo `{repo_name}` already exists.")

# Optional: Display file list
st.write("Contents:", os.listdir(repo_path))
