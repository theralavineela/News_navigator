import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_briefing(topic, news_data):
    prompt = f"""
You are News Navigator AI.

Topic: {topic}

Latest News:
{news_data}

Create:

1. Summary
2. Key Points
3. Different Perspectives
4. Economic / Market Impact
5. 3 Questions for user

Make it crisp, insightful, and structured.
"""

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI Error: {str(e)}"