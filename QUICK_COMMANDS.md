⚡ QUICK COMMANDS & CHEAT SHEET
===============================

## 🚀 START HERE (3 EASY OPTIONS):

### OPTION 1: WEB API + Interactive Docs (RECOMMENDED)
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
uvicorn src.api:app --reload
# Then open: http://127.0.0.1:8000/docs
```

### OPTION 2: CLI Tool (Command Line)
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python src\run.py
# Type queries and press Enter
```

### OPTION 3: Web Frontend
```powershell
# 1. Start API (see OPTION 1)
# 2. Open in browser: frontend/index.html
```

---

## 📋 COPY-PASTE COMMANDS

### Check Everything Works
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -c "import langchain, openai, chromadb, fastapi; print('✅ All packages OK')"
```

### Test Data Loading
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -c "from ingest import load_pdfs; text = load_pdfs(); print(f'✅ Loaded {len(text)} characters')"
```

### Start API (Default Port 8000)
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
uvicorn src.api:app --reload
```

### Start API (Different Port)
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
uvicorn src.api:app --port 8001 --reload
```

### Run CLI Tool
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python src\run.py
```

### Install/Update Packages
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
pip install -r requirements.txt --upgrade
```

### Clean Cache
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
Remove-Item .chroma -Recurse -Force -ErrorAction Ignore
Remove-Item src/__pycache__ -Recurse -Force -ErrorAction Ignore
```

### Check Python Version
```powershell
python --version
# Should be 3.9+ (3.9, 3.10, 3.11, 3.12)
```

### Verify API Key Set
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -c "from dotenv import load_dotenv; import os; load_dotenv(); key = os.getenv('OPENAI_API_KEY'); print('✅ API Key Set' if key else '❌ NO KEY')"
```

---

## 🔗 CURL COMMANDS FOR TESTING

### Health Check
```bash
curl http://127.0.0.1:8000/
```

### Analyze Ingredient (Windows PowerShell)
```powershell
$body = @{query = "Is sodium lauryl sulfate safe?"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:8000/analyze" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

### Analyze Ingredient (Windows CMD/Bash)
```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"Is sodium lauryl sulfate safe?\"}"
```

---

## 🧪 TEST QUERIES TO TRY

### Easy Queries (Test First)
```
"Is glycerin safe?"
"What's niacinamide?"
"Tell me about retinol"
"Are parabens safe?"
```

### Medium Queries
```
"Is sodium lauryl sulfate safe in shampoo?"
"What ingredients should I avoid?"
"Analyze the ingredients: water, glycerin, fragrance"
```

### Advanced Queries
```
"What are endocrine disruptors in cosmetics?"
"Is retinol safe during pregnancy?"
"Compare parabens vs phenoxyethanol"
"Recommend safer alternatives to fragrance"
```

---

## 📂 FILE LOCATIONS

| Component | Location |
|-----------|----------|
| Project Root | `c:\Users\sowmi\Desktop\healthyvenus_ai` |
| Source Code | `src/` |
| Data | `data/sample_ingredients.txt` |
| Frontend | `frontend/index.html` |
| API Key | `.env` |
| Config | `requirements.txt`, `render.yaml` |
| Docs | `QUICK_START.md`, `SETUP_COMPLETE.md` |

---

## 🔗 URLS WHEN RUNNING LOCALLY

| URL | Purpose |
|-----|---------|
| `http://127.0.0.1:8000/` | API health check |
| `http://127.0.0.1:8000/docs` | Interactive API docs (Swagger) |
| `http://127.0.0.1:8000/redoc` | Alternative API docs (ReDoc) |
| `frontend/index.html` | Web UI (open in browser after API starts) |

---

## 🐛 EMERGENCY FIXES

### API Won't Start
```powershell
# Kill any running processes on port 8000
Get-Process | Where-Object {$_.ProcessName -match "python"} | Stop-Process -Force
# Then try again
cd c:\Users\sowmi\Desktop\healthyvenus_ai
uvicorn src.api:app --port 8001 --reload
```

### Module Import Error
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
pip install -r requirements.txt --force-reinstall
```

### No Data Loading
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
# Verify data exists
Get-ChildItem data/
# Should show: sample_ingredients.txt
# If missing, run:
# Create file data/sample_ingredients.txt with ingredient data
```

### API Key Error
```powershell
# Edit .env file and verify it has:
# OPENAI_API_KEY=sk-proj-[your actual key here]
# Then restart API
```

---

## 📊 MONITORING COMMANDS

### Check CPU/Memory Usage (API Running)
```powershell
Get-Process python | Select-Object Name, CPU, Memory
```

### View Last API Logs
```powershell
# If saved to file, check last 50 lines
Get-Content api.log -Tail 50
```

### Monitor Real-time (if you add logging)
```powershell
# Start with debug logging
uvicorn src.api:app --reload --log-level debug --access-log
```

---

## 🎯 WORKFLOW EXAMPLES

### Complete Testing Workflow
```powershell
# 1. Check setup
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -c "import sys; sys.path.insert(0, 'src'); import ingest, rag, agents; print('✅ All modules OK')"

# 2. Check data
python -c "from ingest import load_pdfs; print(f'Data: {len(load_pdfs())} chars')"

# 3. Start API
uvicorn src.api:app --reload

# 4. In another terminal, test
curl http://127.0.0.1:8000/docs
```

### Deploy to Render Workflow
```powershell
# 1. Push to GitHub
git add .
git commit -m "HealthyVenus.AI setup"
git push

# 2. Connect GitHub to Render.com
# 3. Add environment variable: OPENAI_API_KEY
# 4. Deploy
# 5. Your API: https://healthyvenus-api.onrender.com/analyze
```

---

## 🚀 PERFORMANCE TIPS

### Speed Up First Run
```powershell
# Vector store is built on first run (~10s)
# To pre-warm:
python -c "from ingest import load_pdfs; from rag import chunk_text, build_vectorstore; print('Warming...'); text = load_pdfs(); chunks = chunk_text(text); vs = build_vectorstore(chunks); print('✅ Ready')"
```

### Reduce Memory Usage
```powershell
# Run API in production mode (no debug)
uvicorn src.api:app --workers 1
```

### Use Different Python
```powershell
# If system Python is slow, try:
$env:PATH = "C:\Program Files\Python311;" + $env:PATH
python --version
```

---

## 🔐 SECURITY CHECKLIST

### Before Deployment
```powershell
# 1. Never commit .env
echo ".env" >> .gitignore

# 2. Use environment variables
$env:OPENAI_API_KEY = "your-key"

# 3. Rotate key if compromised
# (Generate new key in OpenAI dashboard)

# 4. Add CORS restrictions (in production)
# (Don't allow "*" - restrict to known domains)
```

---

## 📞 QUICK DEBUG

### Full System Check (One Command)
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai; $e = $null; try { python -c "import sys; sys.path.insert(0, 'src'); from ingest import load_pdfs; from rag import build_vectorstore, chunk_text; from dotenv import load_dotenv; import os; load_dotenv(); print('Modules: OK'); text = load_pdfs(); print(f'Data: {len(text)} chars'); chunks = chunk_text(text); print(f'Chunks: {len(chunks)}'); vs = build_vectorstore(chunks); print('Vector Store: OK'); print(f'API Key: {\"Set\" if os.getenv(\"OPENAI_API_KEY\") else \"MISSING\"}')" } catch { $e = $_; Write-Host "ERROR: $_" }; if (-not $e) { Write-Host "✅ SYSTEM READY - Run: uvicorn src.api:app --reload" }
```

### Quick Health Check
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -c "import sys; sys.path.insert(0, 'src'); import ingest; print('✅ Ready')" && echo "Start API: uvicorn src.api:app --reload"
```

---

## 🎉 READY TO GO!

**Copy and run this:**
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
uvicorn src.api:app --reload
```

**Then visit:**
http://127.0.0.1:8000/docs

**Try query:**
```json
{"query": "Is sodium lauryl sulfate safe?"}
```

Enjoy! 🌿✨
