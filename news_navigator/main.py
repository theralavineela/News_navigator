from fastapi import FastAPI
from pydantic import BaseModel

from news_service import fetch_news
from ai_service import generate_briefing

app = FastAPI()

class UserInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(input: UserInput):
    topic = input.text

    if not topic:
        return {"text": "Please enter a topic."}

    news_data = fetch_news(topic)

    # fallback safety
    if "unavailable" in news_data.lower():
        news_data = f"General context about {topic}"

    result = generate_briefing(topic, news_data)

    return {"text": result}

@app.get("/")
def home():
    return {"message": "News Navigator Backend Running 🚀"}