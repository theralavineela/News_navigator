import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(topic):
    try:
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}&language=en&pageSize=5"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") != "ok":
            return "No latest news available."

        articles = []
        for article in data.get("articles", []):
            title = article.get("title", "")
            desc = article.get("description", "")
            articles.append(f"{title} - {desc}")

        if not articles:
            return "No relevant news found."

        return "\n".join(articles)

    except:
        return "News service unavailable."