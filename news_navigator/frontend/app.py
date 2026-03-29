import streamlit as st
import requests

st.set_page_config(page_title="News Navigator AI")

st.title("🧭 News Navigator AI")

topic = st.text_input("Enter a topic:")

if st.button("Analyze"):
    if topic:
        with st.spinner("Fetching insights..."):

            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"text": topic}
            )

            result = response.json()

            st.write(result["text"])
    else:
        st.warning("Please enter a topic")