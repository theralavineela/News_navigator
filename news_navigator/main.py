from fastapi import FastAPI
from pydantic import BaseModel

from news_navigator.news_service import fetch_news
from news_navigator.ai_service import generate_briefing
from news_navigator.db_service import save_search_result, get_recent_searches

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

    save_search_result(topic, result)

    return {"text": result}

@app.get("/history")
async def history():
    return {"history": get_recent_searches()}

@app.get("/")
def home():
    return {"message": "News Navigator Backend Running 🚀"}