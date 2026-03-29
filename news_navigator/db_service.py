import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

def get_supabase_client() -> Client:
    if not URL or not KEY:
        return None
    return create_client(URL, KEY)

def save_search_result(topic: str, result: str):
    supabase = get_supabase_client()
    if supabase:
        try:
            data = {
                "topic": topic,
                "briefing": result
            }
            supabase.table("news_searches").insert(data).execute()
        except Exception as e:
            print(f"Database Error: {e}")
    else:
        print("Supabase credentials not configured.")

def get_recent_searches(limit: int = 5):
    supabase = get_supabase_client()
    if supabase:
        try:
            response = supabase.table("news_searches").select("*").order("created_at", desc=True).limit(limit).execute()
            return response.data
        except Exception as e:
            print(f"Database Error: {e}")
            return []
    return []
