
---

#  `architecture.md`

```markdown
#  System Architecture – News Navigator AI

---

##  Overview
The system is designed as a modular AI-powered pipeline that integrates real-time data with language models to generate structured insights.

---

##  Components

### 1. Frontend (Streamlit)
- Accepts user input (topic)
- Displays structured output
- Provides interactive UI

---

### 2. Backend (FastAPI)
- Handles API requests
- Routes data between services
- Ensures smooth communication

---

### 3. News Service
- Fetches real-time articles using NewsAPI
- Filters and formats relevant data

---

### 4. AI Service
- Uses Groq LLM for processing
- Converts raw news into structured insights

---

##  Workflow

User Input  
↓  
Frontend (Streamlit)  
↓  
Backend API (FastAPI)  
↓  
News API Fetch  
↓  
AI Processing (LLM)  
↓  
Structured Output  
↓  
Frontend Display  

---

##  Communication
- REST APIs (JSON-based)
- Stateless architecture
- Modular service design

---

##  Error Handling Strategy
- API failure → fallback to AI-only response
- Empty news data → default message
- Timeout handling for external APIs

---

##  Scalability Considerations
- Replace APIs with enterprise-grade sources
- Deploy backend on cloud (AWS/GCP)
- Add caching for frequent queries
- Integrate database for history tracking

---

##  Reliability
- Fault-tolerant design
- Graceful degradation
- Consistent user experience
