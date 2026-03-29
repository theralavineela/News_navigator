##  Installation & Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-navigator-ai.git
cd news-navigator-ai
### 2. Backend Setup
cd backend
pip install -r requirements.txt
### 3. Add Environment Variables

Create a .env file inside the backend/ folder:

GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_newsapi_key
 ###4. Run Backend Server
uvicorn main:app --reload

Backend will start at:

http://127.0.0.1:8000
###5. Verify Backend

Open in browser:

http://127.0.0.1:8000/docs
Swagger UI will open
Test the /analyze endpoint
Use sample input:
{
  "text": "AI in healthcare"
}
###6. Frontend Setup

Open a new terminal:

cd frontend
pip install streamlit requests
###7. Run Frontend
streamlit run app.py
###8. Use the Application
Open browser (if not auto-opened):
http://localhost:8501
Enter a topic (e.g., AI in healthcare, India economy)
Click Analyze
View structured AI-generated insights
