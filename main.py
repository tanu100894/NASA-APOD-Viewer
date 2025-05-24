# Import required libraries
import streamlit as st
import requests, os
from dotenv import load_dotenv

# Load environment variable from .env file
load_dotenv()

# Retrieve NASA API key from environment variables
api_key = os.getenv("api_key")

# Make an API request to NASA's Astronomy Picture of the Day (APOD)
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
request = requests.get(url)
content = request.json() # Parse JSON response

# Set Streamlit page layout and display data
st.set_page_config("wide")          # Use wide layout
st.header(content["title"])         # Display image title
st.image(content["hdurl"])          # Display high-definition image
st.text(content["explanation"])     # Show the image explanation


