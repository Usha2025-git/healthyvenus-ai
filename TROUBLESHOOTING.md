🔧 TROUBLESHOOTING GUIDE
=======================

## BEFORE YOU START

Make sure you're in the correct directory:
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
```

---

## 🚀 STARTING THE API

### Problem: "Command not found: uvicorn"
**Cause:** Packages not installed
**Solution:** 
```powershell
pip install -r requirements.txt
```

### Problem: "Address already in use: 127.0.0.1:8000"
**Cause:** Port 8000 is in use by another process
**Solution:**
```powershell
# Use different port
uvicorn src.api:app --port 8001 --reload

# OR kill process on port 8000
netstat -ano | findstr :8000
# Then: taskkill /PID <PID> /F
```

### Problem: "ModuleNotFoundError: No module named 'fastapi'"
**Cause:** Dependencies not installed
**Solution:**
```powershell
pip install -r requirements.txt
python -c "import fastapi; print('OK')"
```

---

## 🔑 API KEY ISSUES

### Problem: "OpenAI API key not found"
**Cause:** .env file not configured
**Solution:**
1. Check .env exists in project root
2. Verify it has: `OPENAI_API_KEY=sk-proj-...`
3. Restart API server after editing

**Debug:**
```powershell
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('OPENAI_API_KEY')[:10])"
```

### Problem: "Authentication failed / Invalid API key"
**Cause:** Wrong or expired API key
**Solution:**
1. Check key starts with `sk-proj-`
2. Verify key is valid on OpenAI dashboard
3. Regenerate new key if needed
4. Update .env with new key

---

## 💾 DATA LOADING ISSUES

### Problem: "No data loaded / 0 characters"
**Cause:** No PDFs or TXT files in data/ folder
**Solution:**
1. Check data/ folder exists: `ls data/`
2. Add ingredient data:
   - Option A: Create `data/ingredients.txt` with content
   - Option B: Add `data/cosmetics.pdf` from web
3. Verify file is readable

**Check:**
```powershell
ls -la data/
python -c "from ingest import load_pdfs; text = load_pdfs(); print(f'Loaded {len(text)} chars')"
```

### Problem: "PDF reader error / Extract failed"
**Cause:** Corrupted PDF file
**Solution:**
1. Try different PDF file
2. Use TXT file instead: `data/ingredients.txt`
3. Check PDF isn't password protected

---

## 🤖 AGENT / AI ISSUES

### Problem: "Error in agent pipeline"
**Cause:** Usually API key or OpenAI issue
**Solution:**
```powershell
# Test API key works
python -c "from openai import OpenAI; client = OpenAI(); print('OK')"

# Or test with sample query
python src/run.py
```

### Problem: "Empty response from agent"
**Cause:** No relevant data found or API timeout
**Solution:**
1. Verify data is loaded: `python -c "from ingest import load_pdfs; print(len(load_pdfs()))"`
2. Try simpler query: "What is glycerin?"
3. Check internet connection
4. Wait 1 minute and retry (rate limit)

### Problem: "Slow responses / Timeout"
**Cause:** 
- First run initializes vector database
- API rate limiting
- Network issues
**Solution:**
- First query normal to be slow (10-30s)
- Subsequent queries faster (3-5s)
- If persistent, increase timeout or check network

---

## 🌐 API ENDPOINT ISSUES

### Problem: "Cannot POST /analyze"
**Cause:** Endpoint not accessible
**Solution:**
1. Verify API is running: `http://127.0.0.1:8000/`
2. Check port is correct (default 8000)
3. Try GET /: `http://127.0.0.1:8000/`
4. View docs: `http://127.0.0.1:8000/docs`

### Problem: "Method not allowed"
**Cause:** Using wrong HTTP method
**Solution:**
- /analyze requires POST (not GET)
- Use curl: `curl -X POST http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d "{\"query\":\"....\"}"`

### Problem: "400 Bad Request"
**Cause:** Invalid request format
**Solution:**
```json
// CORRECT:
{"query": "Is sodium lauryl sulfate safe?"}

// WRONG:
{"Query": "..."} // Capital Q
{"question": "..."} // Wrong field name
```

---

## 🌐 FRONTEND ISSUES

### Problem: "Frontend won't load"
**Cause:** API not running or CORS issue
**Solution:**
1. Start API: `uvicorn src.api:app --reload`
2. Wait 5 seconds for startup
3. Open frontend/index.html
4. Check browser console for errors (F12)

### Problem: "Error: Could not connect to API"
**Cause:** API not running on port 8000
**Solution:**
1. Start API in new terminal: `uvicorn src.api:app --reload`
2. Verify at: `http://127.0.0.1:8000/docs`
3. If using different port, update frontend:
   ```javascript
   // In frontend/index.html, find:
   const response = await fetch("http://127.0.0.1:8000/analyze", {
   // Change 8000 to your port number
   ```

### Problem: "CORS error in browser console"
**Cause:** Browser security restriction
**Solution:**
1. Local testing: Should work (same origin)
2. Remote API: Need CORS headers in api.py
3. Add to api.py:
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

---

## 📊 VECTOR STORE ISSUES

### Problem: "ChromaDB error / Collections not found"
**Cause:** Vector store not initialized
**Solution:**
```powershell
# Reset vector store
rm -r .chroma -Force  # Remove cache
python -c "from ingest import load_pdfs; from rag import chunk_text, build_vectorstore; text = load_pdfs(); chunks = chunk_text(text); vs = build_vectorstore(chunks); print('Vector store created')"
```

### Problem: "Very slow similarity search"
**Cause:** Large dataset or first run
**Solution:**
- Normal for large datasets
- Cache builds on first run (~10s)
- Subsequent queries are faster
- If persistent: reduce chunk size in rag.py

---

## 📝 PYTHON/IMPORT ISSUES

### Problem: "Module not found: langchain"
**Cause:** Not installed or wrong Python version
**Solution:**
```powershell
pip list | grep langchain  # Check installed
python --version  # Check Python 3.9+
pip install langchain --upgrade  # Reinstall
```

### Problem: "Python: command not found"
**Cause:** Python not in PATH
**Solution:**
```powershell
# Use full path
"C:\Program Files\Python39\python.exe" src\run.py

# OR add to PATH
# System Properties > Environment Variables > Add Python to PATH
```

### Problem: "ImportError: cannot import name 'OpenAIEmbeddings'"
**Cause:** Deprecated import (LangChain update)
**Solution:**
Warnings are OK - code still works
To fix permanently:
```powershell
pip install langchain-openai
# Then update imports in rag.py:
# from langchain_community.embeddings import OpenAIEmbeddings
```

---

## 🔍 DEBUGGING STEPS

### Test 1: Check Python & Packages
```powershell
python --version
pip list | grep -E "langchain|openai|chromadb|fastapi"
```

### Test 2: Check Environment
```powershell
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key Set' if os.getenv('OPENAI_API_KEY') else 'NO KEY')"
```

### Test 3: Check Data
```powershell
python -c "from ingest import load_pdfs; text = load_pdfs(); print(f'Data: {len(text)} chars')"
```

### Test 4: Check API
```powershell
python -c "from fastapi import FastAPI; print('FastAPI OK')"
```

### Test 5: Check Imports
```powershell
python -c "import sys; sys.path.insert(0, 'src'); import ingest, rag, agents; print('Modules OK')"
```

### Test 6: Start API
```powershell
uvicorn src.api:app --reload --log-level debug
```

---

## 🆘 STILL STUCK?

### Nuclear Option: Reset Everything
```powershell
# Backup your .env (saves your API key)
copy .env .env.backup

# Remove all cache
rm .chroma -Force -Recurse
rm -r src/__pycache__ -Force
rm -r .pytest_cache -Force

# Reinstall packages
pip install -r requirements.txt --force-reinstall

# Test again
python src/run.py
```

### Check Logs for Clues
```powershell
# Start API with verbose logging
uvicorn src.api:app --reload --log-level debug 2>&1 | Tee-Object api.log
```

### Common Error Messages

| Error | Cause | Fix |
|-------|-------|-----|
| "Address already in use" | Port in use | Use `--port 8001` |
| "Module not found" | Not installed | `pip install -r requirements.txt` |
| "API key not found" | Missing .env | Create `.env` with key |
| "No data" | data/ empty | Add ingredients.txt |
| "Connection refused" | API not running | `uvicorn src.api:app --reload` |
| "CORS error" | Browser restriction | Try different port or endpoint |
| "Timeout" | Query too slow | Normal for first run (10-30s) |

---

## 📞 QUICK SUPPORT

**Cannot start API:**
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
pip install -r requirements.txt
uvicorn src.api:app --reload --log-level debug
```

**Data not loading:**
```powershell
# Check data folder
ls data/
# Should see: sample_ingredients.txt
```

**Want to test without API:**
```powershell
python src/run.py  # CLI mode
```

**Full system check:**
```powershell
python -c "import sys; sys.path.insert(0, 'src'); from ingest import load_pdfs; from rag import build_vectorstore, chunk_text; text = load_pdfs(); chunks = chunk_text(text); vs = build_vectorstore(chunks); print('✅ System OK')"
```

---

## ✨ YOU'RE ALL SET!

Most issues resolve by:
1. Restarting the API
2. Checking the .env file
3. Verifying data exists
4. Checking internet connection

Good luck! 🚀
