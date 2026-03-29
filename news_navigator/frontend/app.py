import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Backend URL - Use local as default, override via env var
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="News Navigator AI")

st.title("🧭 News Navigator AI")

topic = st.text_input("Enter a topic:")

if st.button("Analyze"):
    if topic:
        with st.spinner("Fetching insights..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/analyze",
                    json={"text": topic}
                )
                result = response.json()
                st.write(result["text"])
            except Exception as e:
                st.error(f"Error connecting to backend: {e}")
    else:
        st.warning("Please enter a topic")

# History Section
st.divider()
st.subheader("🕑 Recent History")
if st.button("Load Recent History"):
    try:
        response = requests.get(f"{BACKEND_URL}/history")
        history_data = response.json().get("history", [])
        if history_data:
            for item in history_data:
                # topic and created_at are columns in the Supabase table
                with st.expander(f"{item.get('topic', 'N/A')} ({item.get('created_at', 'N/A')})"):
                    st.write(item.get('briefing', 'N/A'))
        else:
            st.info("No history found.")
    except Exception as e:
        st.error(f"Error fetching history: {e}")