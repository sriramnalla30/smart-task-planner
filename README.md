# Smart Task Planner 🎯

AI-powered task planning service that breaks down goals into actionable tasks with timelines using LLM reasoning.

## 📋 Project Overview

**Objective**: Break user goals into actionable tasks with timelines using AI reasoning.

**Scope:**

- **Input**: Goal text (e.g., "Launch a product in 2 weeks")
- **Output**: Task breakdown, dependencies, estimated timelines
- **Optional frontend**: Submit goals & view plans with visualizations

## 🏗️ Technical Implementation

### Backend API (FastAPI)

- `POST /plan` - Processes goal and generates structured task plan
- `GET /health` - Service health check
- Full input validation with Pydantic schemas
- Async execution for optimal performance

### LLM Integration (Google Gemini)

- **Model**: Gemini 2.0 Flash (configurable)
- **Prompt Engineering**: Structured JSON output with task dependencies
- **Fallback**: Mock planner for development without API key
- **Features**:
  - Dependency-aware task generation
  - Confidence scoring per task
  - Planning strategy explanation
  - **Reference links** - Helpful tutorials, docs, and resources for each task

### Optional Frontend

- Clean, responsive UI with Tailwind CSS
- Interactive Gantt chart visualization (Mermaid)
- Real-time plan generation
- Mobile-friendly design

### Validation Engine

- Dependency cycle detection (prevents circular references)
- Timeline conflict resolution
- Ensures tasks fit within planning horizon

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10+
- Google Gemini API key ([Get free key](https://aistudio.google.com/app/apikey))

### Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 3. Start server
uvicorn app.main:app --reload
```

**Server URL**: http://127.0.0.1:8000

## 📖 Usage

### Option 1: Interactive Frontend

Open `frontend/index.html` in your browser and fill in:

- Goal description
- Target date or planning horizon
- Optional guidance (constraints, team size, etc.)

### Option 2: API (Swagger UI)

Visit http://127.0.0.1:8000/docs and use the interactive interface

### Option 3: Python Script

```python
from app.services.plan_service import PlanService
from app.schemas import PlanRequest
import asyncio

async def main():
    service = PlanService()
    request = PlanRequest(
        goal="Launch a mobile app in 3 weeks",
        target_date="2025-11-03",
        guidance="Team of 2 developers, MVP focus"
    )
    response = await service.generate(request)

    print(f"Generated {len(response.tasks)} tasks")
    for task in response.tasks:
        print(f"- {task.title} ({task.start_date} → {task.due_date})")

asyncio.run(main())
```

### Option 4: cURL

```bash
curl -X POST "http://127.0.0.1:8000/plan" \
  -H "Content-Type: application/json" \
  -d '{"goal": "Prepare for technical interview", "horizon_days": 14}'
```

## 📂 Project Structure

```
smart-task-planner/
├── app/
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── schemas.py           # Pydantic models
│   ├── llm/
│   │   ├── provider.py      # LLM provider interface
│   │   └── gemini.py        # Gemini implementation
│   ├── services/
│   │   └── plan_service.py  # Core planning logic
│   └── utils/
│       ├── timeline.py      # Date backfilling
│       └── validation.py    # Dependency validation
├── frontend/
│   └── index.html           # Web UI (optional)
├── tests/
│   └── test_plan_service.py # Unit tests
├── test_api.py              # Integration test
├── requirements.txt         # Dependencies
├── .env                     # Configuration (git-ignored)
└── README.md                # This file
```

## 🎨 Example Output

**Input:**

```json
{
  "goal": "Launch a productivity app in 2 weeks",
  "target_date": "2025-10-27",
  "guidance": "Team of 3 engineers, tight budget, prioritize MVP"
}
```

**Output:**

```json
{
  "metadata": {
    "goal": "Launch a productivity app in 2 weeks",
    "planning_strategy": "Prioritize MVP features, parallelize development...",
    "assumptions": ["Team of 3 engineers", "Budget is tight"],
    "horizon_days": 14
  },
  "tasks": [
    {
      "id": "T1",
      "title": "Define MVP Features & Tech Stack",
      "description": "Finalize essential features...",
      "start_date": "2025-10-13",
      "due_date": "2025-10-13",
      "depends_on": [],
      "confidence": 0.95
    },
    {
      "id": "T2",
      "title": "Set up Development Environment",
      "start_date": "2025-10-13",
      "due_date": "2025-10-14",
      "depends_on": ["T1"],
      "confidence": 0.9
    }
    // ... 7 more tasks with dependencies
  ]
}
```

## 🧪 Testing

```bash
# Run integration test
python test_api.py

# Run unit tests (if pytest installed)
pytest tests/ -v
```

## 🔧 Configuration

Environment variables (`.env` file):

| Variable                  | Default                | Description                    |
| ------------------------- | ---------------------- | ------------------------------ |
| `GEMINI_API_KEY`          | None                   | Your Gemini API key (required) |
| `GEMINI_MODEL`            | `gemini-2.0-flash-exp` | Model to use                   |
| `SMART_TASK_PLANNER_MOCK` | `false`                | Use mock mode (no API calls)   |

## 📊 Key Features

### LLM Usage

- **Prompt Strategy**: "Break down this goal into actionable tasks with suggested deadlines and dependencies"
- **Output Format**: Structured JSON with metadata and task array
- **Task Fields**: ID, title, description, owner, dates, duration, dependencies, confidence, **reference_links**
- **Resource Recommendations**: AI provides helpful tutorials, documentation, and guides for each task

### Task Completeness

- Generates 5-10 meaningful tasks covering complete goal scope
- Each task includes actionable title and detailed description
- Suggested owner roles when applicable
- **Reference links** to official docs, tutorials, and tools

### Timeline Logic

- Realistic date assignments based on target deadline or horizon
- Respects task dependencies in scheduling
- Backfills missing dates intelligently
- Validates timeline conflicts

### Code & API Design

- Clean, modular architecture with type hints
- Async/await for non-blocking execution
- Comprehensive error handling
- OpenAPI/Swagger documentation
- CORS support for frontend integration

## 🎯 Evaluation Criteria

✅ **Task Completeness** - Comprehensive breakdown with all necessary steps  
✅ **Timeline Logic** - Realistic, dependency-aware scheduling  
✅ **LLM Reasoning** - Intelligent task generation with explanations  
✅ **Code Quality** - Clean, modular, well-documented  
✅ **API Design** - RESTful, validated, documented

## 📺 Demo Video

A demo video showcasing:

1. Installation and configuration
2. API usage via Swagger UI
3. Frontend workflow with visualization
4. Generated plan with dependencies and timelines

**[Recording coming soon]**

## 🤝 Contributing

Future enhancements:

- Database persistence for plan storage
- Additional LLM providers (OpenAI, Anthropic)
- Export formats (CSV, PDF)
- Integration with project management tools
**
sample test runs**
<img width="1067" height="792" alt="image" src="https://github.com/user-attachments/assets/4d366c63-31c2-47d1-80b1-27e09ad20433" />

<img width="969" height="404" alt="image" src="https://github.com/user-attachments/assets/12ac5539-509d-4bbc-b11c-6bcc2b76680a" />

<img width="914" height="162" alt="image" src="https://github.com/user-attachments/assets/a69e2e2e-a5e7-4592-b735-0366b48e7381" />

<img width="915" height="804" alt="image" src="https://github.com/user-attachments/assets/d8e135cd-872e-4d7e-bfee-a95aedc2e01d" />

<img width="924" height="854" alt="image" src="https://github.com/user-attachments/assets/3f4809d7-db44-477b-8025-1212c1c4d42d" />

<img width="922" height="841" alt="image" src="https://github.com/user-attachments/assets/ddd020e5-fbef-4868-9c7b-239ec62105fc" />

<img width="915" height="353" alt="image" src="https://github.com/user-attachments/assets/05e21ad8-11c4-4f0e-bf10-0eadb31a720d" />

**Built with FastAPI, Google Gemini AI, and modern web technologies**
