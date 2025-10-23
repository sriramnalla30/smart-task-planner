# Smart Task Planner - Setup Instructions

## 📋 Quick Start Guide

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key ([Get free key here](https://aistudio.google.com/app/apikey))

### Installation Steps

1. **Extract the project files**
   ```bash
   # Navigate to the project folder
   cd smart-task-planner
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - Windows (PowerShell):
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - Windows (Command Prompt):
     ```bash
     .venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure API Key**
   
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   
   Or set environment variable:
   - Windows:
     ```bash
     $env:GEMINI_API_KEY="your_api_key_here"
     ```
   - Linux/Mac:
     ```bash
     export GEMINI_API_KEY="your_api_key_here"
     ```

6. **Start the backend server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Open the frontend**
   
   Open `frontend/index.html` in your web browser, or navigate to:
   ```
   http://localhost:8000/
   ```

## 🧪 Testing the API

### Option 1: Using the Frontend
1. Open `frontend/index.html` in your browser
2. Enter a goal (e.g., "Build a portfolio website in 1 week")
3. Set timeline and context
4. Click "Generate My Action Plan"

### Option 2: Using cURL
```bash
curl -X POST "http://127.0.0.1:8000/plan" \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "Launch a mobile app in 3 weeks",
    "horizon_days": 21,
    "guidance": "Team of 2 developers, MVP focus"
  }'
```

### Option 3: Using Python Script
```bash
python test_api.py
```

## 📂 Project Structure

```
smart-task-planner/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── schemas.py           # Pydantic models
│   ├── llm/
│   │   ├── gemini.py        # Gemini AI integration
│   │   └── provider.py      # LLM provider interface
│   ├── services/
│   │   └── plan_service.py  # Core planning logic
│   └── utils/
│       ├── timeline.py      # Date handling
│       └── validation.py    # Dependency validation
├── frontend/
│   └── index.html           # Web UI
├── tests/
│   └── test_plan_service.py # Unit tests
├── .env                     # API key (create this)
├── .gitignore
├── requirements.txt         # Python dependencies
├── test_api.py             # Integration test
└── README.md               # This file
```

## 🎯 Features Implemented

✅ **Input:** Accepts goal text (e.g., "Launch a product in 2 weeks")  
✅ **Output:** Task breakdown with dependencies and timelines  
✅ **Backend API:** FastAPI with POST /plan endpoint  
✅ **LLM Integration:** Google Gemini 2.0 for reasoning  
✅ **Prompt:** "Break down this goal into actionable tasks with suggested deadlines and dependencies"  
✅ **Frontend:** Optional web UI for goal submission and plan visualization  
✅ **Validation:** Dependency cycle detection and timeline conflict checking  
✅ **Reference Links:** AI provides helpful tutorials/docs for each task  

## 🔧 Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### API key errors
Ensure your `.env` file exists with:
```
GEMINI_API_KEY=your_actual_key_here
```

### Port already in use
Change the port:
```bash
uvicorn app.main:app --reload --port 8001
```

## 📚 Documentation

- **README.md** - This file
- **QUICKSTART.md** - 3-minute setup guide
- **PROJECT_SUMMARY.md** - Detailed project overview
- **RECRUITER_GUIDE.md** - Non-technical explanation
- **UI_IMPROVEMENTS.md** - Frontend enhancements
- **VISUAL_ENHANCEMENTS.md** - Visualization features
- **REFERENCE_LINKS_FEATURE.md** - AI resource links

## 🌐 API Endpoints

### POST /plan
Generate a task plan from a goal.

**Request:**
```json
{
  "goal": "Build a portfolio website",
  "target_date": "2025-11-01",
  "guidance": "Solo developer, use React"
}
```

**Response:**
```json
{
  "metadata": {
    "goal": "Build a portfolio website",
    "planning_strategy": "Sequential development approach",
    "assumptions": ["Solo developer", "1 week timeline"],
    "horizon_days": 7
  },
  "tasks": [
    {
      "id": "T1",
      "title": "Set up development environment",
      "description": "Install Node.js, React, and configure tools",
      "start_date": "2025-10-25",
      "due_date": "2025-10-26",
      "duration_days": 1,
      "depends_on": [],
      "confidence": 0.95,
      "reference_links": [
        "https://react.dev/learn/start-a-new-react-project"
      ]
    }
  ]
}
```

### GET /health
Check service health.

**Response:**
```json
{
  "status": "healthy",
  "provider": "GeminiPlanner"
}
```

## 👤 Author

**Name:** Nalla Sri Ram  
**Reg No:** 22BCT0310  
**Email:** sriramnalla30@gmail.com  
**GitHub:** https://github.com/sriramnalla30/smart-task-planner

## 📄 License

This project is submitted as part of an academic assignment.
