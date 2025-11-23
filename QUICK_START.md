🌿 HEALTHYVENUS.AI - QUICK START GUIDE
======================================

## ✅ SETUP COMPLETE!

Your HealthyVenus.AI project is fully configured and ready to use.

### 📁 FILES CREATED:
- src/ingest.py (1.01 KB) - Loads ingredient data
- src/rag.py (1.13 KB) - Vector database system
- src/agents.py (4.46 KB) - 3-agent AI pipeline
- src/api.py (0.98 KB) - FastAPI backend
- src/run.py (0.95 KB) - CLI testing tool
- frontend/index.html (3.6 KB) - Web UI
- data/sample_ingredients.txt (7.31 KB) - Ingredient database
- .env - OpenAI API key configured
- requirements.txt - All dependencies installed
- render.yaml - Deployment config

---

## 🚀 START HERE - THREE OPTIONS:

### OPTION 1: WEB INTERFACE (EASIEST) ⭐
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
uvicorn src.api:app --reload
```
Then open in browser: http://127.0.0.1:8000/docs

### OPTION 2: CLI INTERFACE
```powershell
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python src\run.py
```
Type queries and get analysis

### OPTION 3: INTERACTIVE WEB APP
Start API (Option 1), then open: `frontend/index.html`

---

## 📊 SAMPLE TEST QUERIES:

Type these into any interface:
- "Is sodium lauryl sulfate safe?"
- "Analyze parabens in shampoo"
- "What are endocrine disruptors?"
- "Is retinol safe during pregnancy?"
- "Recommend safer fragrance alternatives"
- "Is niacinamide good for sensitive skin?"

Expected Response:
```
🧪 INGREDIENT SCAN:
[AI identifies and describes ingredients]

⚠️ TOXICITY SCORES:
[Safety ratings 1-10 with risk categories]

✅ RECOMMENDATIONS:
[Safer alternatives and actionable advice]
```

---

## 🔧 SYSTEM COMPONENTS:

**Data Flow:**
```
Your Query
    ↓
Agent 1: Ingredient Scanner (finds what ingredients are in the product)
    ↓
Agent 2: Toxicity Scorer (rates safety 1-10)
    ↓
Agent 3: Recommendation Engine (suggests safer alternatives)
    ↓
AI-Powered Response (via OpenAI GPT)
```

**Ingredient Database:**
- 12+ ingredients with safety scores
- Ranges from Glycerin (10/10 Safe) to Benzene (1/10 Critical Risk)
- Includes health concerns, medical evidence, and safer alternatives

---

## 📋 COMMAND REFERENCE:

| Command | Purpose |
|---------|---------|
| `uvicorn src.api:app --reload` | Start FastAPI server |
| `python src\run.py` | Start CLI interface |
| `pip install -r requirements.txt` | Install packages |
| Visit http://127.0.0.1:8000/docs | Interactive API docs |
| Open `frontend/index.html` | Web UI (after API starts) |

---

## 🌐 API ENDPOINT:

**POST /analyze**
```json
Request:
{
  "query": "Is sodium lauryl sulfate safe?"
}

Response:
{
  "query": "Is sodium lauryl sulfate safe?",
  "ingredient_scan": "...",
  "toxicity_scores": "...",
  "recommendations": "..."
}
```

---

## 📚 ADDING MORE DATA:

Add ingredient safety info:
1. Create files in `data/` folder:
   - `data/ingredients_2.txt` (text file)
   - `data/cosmetic_safety.pdf` (PDF file)
2. System auto-loads on next run

---

## 🚀 DEPLOYMENT (OPTIONAL):

To deploy on Render.com:
1. Push code to GitHub
2. Connect Render to your repo
3. Add env var: `OPENAI_API_KEY`
4. Deploy!
5. Your API: https://healthyvenus-api.onrender.com

---

## ✨ CURRENT INGREDIENT DATABASE:

**HIGH RISK (Avoid):**
- Benzene (1/10) - Carcinogen
- Lead/Heavy Metals (1/10) - Neurotoxin
- Formaldehyde (2/10) - Carcinogen
- Phthalates (2/10) - Endocrine disruptor
- Fragrance (3/10) - Hidden 3000+ chemicals

**MODERATE RISK:**
- SLS (4/10) - Skin irritant
- Parabens (5/10) - Endocrine concern
- Retinol (6/10) - Teratogenic in pregnancy

**SAFE OPTIONS:**
- Vitamin C (8/10) - Antioxidant
- Hyaluronic Acid (9/10) - Hydration
- Niacinamide (9/10) - Gentle & effective
- Zinc Oxide (9/10) - Safe sunscreen
- Glycerin (10/10) - Pure safe ingredient

---

## ❓ NEED HELP?

**Issue:** API won't start
**Fix:** Port 8000 in use → Try: `uvicorn src.api:app --port 8001`

**Issue:** Module not found
**Fix:** Run from project root: `cd c:\Users\sowmi\Desktop\healthyvenus_ai`

**Issue:** No data loading
**Fix:** Check `data/sample_ingredients.txt` exists

**Issue:** API key error
**Fix:** Verify `.env` has valid OPENAI_API_KEY

---

## 🎉 YOU'RE READY!

Pick an option above and start analyzing ingredients:
1. Run: `uvicorn src.api:app --reload`
2. Open: http://127.0.0.1:8000/docs
3. Click "POST /analyze"
4. Enter query: "Is sodium lauryl sulfate safe?"
5. See AI-powered analysis!

Enjoy! 🌿✨
