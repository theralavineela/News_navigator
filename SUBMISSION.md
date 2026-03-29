# ET GEN AI Hackathon Submission: News Navigator AI 🧭

## Project Overview
**News Navigator AI** is an intelligent news aggregation and analysis platform designed to combat information overload. It converts real-time news into structured, actionable insights using cutting-edge Generative AI.

## 🔗 Project Links
- **Live Application**: [https://news-navigator-ai.vercel.app](https://news-navigator-ai.vercel.app)
- **GitHub Repository**: [https://github.com/theralavineela/News_navigator](https://github.com/theralavineela/News_navigator)

## 💡 The Problem
In today's fast-paced world, news is fragmented across multiple sources. This leads to:
- Information overload.
- Exposure to biased perspectives.
- Time-consuming analysis for market or economic impact.

## ✨ Our Solution
News Navigator AI fetches real-time data and uses the Groq LLM to generate:
- **Concise Summaries**: A quick grasp of the latest developments.
- **Key Highlights**: Critical points for fast consumption.
- **Multi-Perspective Analysis**: Highlighting different viewpoints (experts, fans, financial analysts, etc.).
- **Market Impact**: Identifying economic and business consequences.
- **Interactive Engagement**: Generating follow-up questions for deeper critical thinking.

## 🛠️ Tech Stack
- **AI Engine**: Groq API (High-performance inference with Llama 3 models).
- **Backend**: FastAPI (Python).
- **Frontend**: Premium HTML/JS Web UI + Streamlit (for local/custom use).
- **Database**: Supabase (PostgreSQL) for search history and persistence.
- **Data Source**: NewsAPI for real-time aggregation.
- **Deployment**: Vercel.

## 🚀 Setup & Installation
1. **Clone the Repo**:
   ```bash
   git clone https://github.com/theralavineela/News_navigator.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Environment Variables**:
   Access the `.env` file or Vercel dashboard and add:
   - `NEWS_API_KEY`, `GROQ_API_KEY`, `SUPABASE_URL`, `SUPABASE_KEY`.
4. **Database Table**:
   Run the SQL provided in the repository to create the `news_searches` table in Supabase.

---
**Developed by**: Therala Vineela & Gade Mallikarjun
