import streamlit as st
import os
import requests

def save_uploaded_file(uploaded_file):
    # Create a directory to save uploaded files if it doesn't exist
    if not os.path.exists('uploaded_files'):
        os.makedirs('uploaded_files')
    
    # Save the file to the specified directory
    file_path = os.path.join('uploaded_files', uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def hit_api(file_path):
    api_url = 'http://127.0.0.1:3000/sentimentAnalysis'
    with open(file_path, 'r') as f:
        files = {'file': f}
        response = requests.post(api_url, files=files)
    return response.json()

st.title("File Upload and API Call")

# File upload
uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
    # Read file content
    file_content = uploaded_file.read().decode("utf-8")
    
    # Save the uploaded file and get the path
    file_path = save_uploaded_file(uploaded_file)
    
    # Button to hit the API
    if st.button("Hit API"):
        response = hit_api(file_path)
        
        # Display API response
        st.write("API Response:")
        st.json(response)
