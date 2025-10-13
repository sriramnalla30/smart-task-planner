# 🚀 QUICK START GUIDE - Smart Task Planner

This guide will get you up and running in **3 minutes**!

---

## ⚡ Step-by-Step Instructions

### Step 1: Start the Server (30 seconds)

Open PowerShell in VS Code and run:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

✅ You should see:

```
INFO: Uvicorn running on http://127.0.0.1:8000
INFO: Application startup complete.
```

**Leave this terminal running!**

---

### Step 2: Open the Frontend (10 seconds)

**Option A: Double-click the file**

- Navigate to: `d:\gitcode\Projects\Unthinkable\frontend\index.html`
- Double-click to open in your browser

**Option B: Use a local server (recommended)**
Open a NEW terminal and run:

```powershell
cd frontend
python -m http.server 3000
```

Then open: http://localhost:3000

---

### Step 3: Generate Your First Plan (1 minute)

1. In the web interface, enter a goal:

   ```
   Launch a SaaS product in 30 days
   ```

2. Set target date or horizon:

   ```
   Target Date: 2025-11-12
   ```

3. Add optional guidance:

   ```
   Team of 2 developers, $5k budget, focus on MVP
   ```

4. Click **"✨ Generate Task Plan"**

5. Wait 3-5 seconds for AI magic! ✨

6. View your generated:
   - Task breakdown with dependencies
   - Timeline with dates
   - Gantt chart visualization
   - AI strategy explanation

---

## 🎯 Try These Example Goals

### Software Development

```
Goal: Build a portfolio website in 1 week
Guidance: Solo developer, use React and Tailwind CSS
```

### Career Planning

```
Goal: Prepare for a technical interview at Google
Horizon: 14 days
Guidance: Focus on algorithms, system design, and behavioral questions
```

### Product Launch

```
Goal: Launch an online course on Python
Target Date: 2025-11-01
Guidance: Need to create videos, write scripts, set up platform
```

### Business

```
Goal: Open a coffee shop in 60 days
Guidance: Already have location, need permits, equipment, staff
```

---

## 🔧 Testing the API Directly

### Via Swagger UI

1. Go to: http://127.0.0.1:8000/docs
2. Click on **POST /plan**
3. Click **"Try it out"**
4. Paste this JSON:

```json
{
  "goal": "Write a book in 3 months",
  "horizon_days": 90,
  "guidance": "Non-fiction, self-help genre, aim for 50k words"
}
```

5. Click **"Execute"**
6. See the response below!

### Via Python Script

```powershell
python test_api.py
```

### Via cURL

```powershell
curl -X POST "http://127.0.0.1:8000/plan" -H "Content-Type: application/json" -d "{\"goal\": \"Learn machine learning in 30 days\", \"horizon_days\": 30}"
```

---

## 📊 What You'll See

### Task Plan Structure

Each plan includes:

- **Metadata**: Goal, strategy, assumptions, horizon
- **Tasks**: 5-10 actionable items with:
  - Unique ID (T1, T2, T3...)
  - Title and description
  - Start and due dates
  - Dependencies (which tasks must finish first)
  - Confidence score (0-100%)
  - Suggested owner/role

### Timeline Visualization

- Beautiful Gantt chart
- Color-coded tasks
- Dependency lines
- Interactive interface

---

## 🎬 Recording Demo Video

### What to Show (5 minutes total)

**Minute 1: Introduction**

- Show the PDF requirements
- Explain the project goal

**Minute 2: Code Walkthrough**

- Show project structure
- Highlight key files (main.py, gemini.py, schemas.py)
- Show the frontend HTML

**Minute 3: Configuration**

- Show .env file (blur API key!)
- Explain model selection

**Minute 4: Live Demo**

- Start the server
- Open frontend
- Enter a goal
- Generate plan
- Show results and Gantt chart

**Minute 5: API Testing**

- Open /docs
- Test via Swagger
- Show JSON response
- Highlight key features (dependencies, confidence, validation)

### Screen Recording Tools

- **OBS Studio** (Free, powerful)
- **Loom** (Easy, cloud-based)
- **ShareX** (Free, lightweight)
- **Windows Game Bar** (Built-in: Win + G)

---

## 🐛 Troubleshooting

### Server won't start

```powershell
# Make sure you're in the right directory
cd d:\gitcode\Projects\Unthinkable

# Activate venv
.\.venv\Scripts\Activate.ps1

# Check if port 8000 is free
netstat -ano | findstr :8000

# Kill process if needed
taskkill /PID <process_id> /F
```

### API returns 502 error

- Check your .env file has `GEMINI_API_KEY`
- Verify API key is valid at https://aistudio.google.com/app/apikey
- Check internet connection

### Frontend can't connect to API

- Make sure server is running on http://127.0.0.1:8000
- Check browser console for CORS errors
- Try opening frontend via local server instead of file://

### No tasks generated

- Check server logs for errors
- Try with mock mode: set `SMART_TASK_PLANNER_MOCK=true` in .env
- Verify your goal is clear and specific

---

## 📚 Documentation

- **README.md** - Full project documentation
- **PROJECT_SUMMARY.md** - Completion status and features
- **DOCS_APPENDIX.md** - Additional technical details
- **API Docs** - http://127.0.0.1:8000/docs (when server running)

---

## 🎉 You're All Set!

The Smart Task Planner is now running and ready to use!

**Next Steps:**

1. ✅ Test with various goals
2. ✅ Explore the Swagger API docs
3. ✅ Record your demo video
4. ✅ Push to GitHub
5. ✅ Share with the world!

---

**Need Help?**

- Check the logs in the terminal
- Read PROJECT_SUMMARY.md for detailed info
- Review the code comments
- Test with mock mode if API issues

**Happy Planning! 🎯✨**
