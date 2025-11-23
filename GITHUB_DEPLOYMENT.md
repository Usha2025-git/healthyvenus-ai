# 🚀 HealthyVenus.AI - GitHub & Deployment Guide

## ✅ GitHub Repository Setup Complete!

**Repository:** https://github.com/Usha2025-git/healthyvenus-ai

```bash
# Clone on your machine:
git clone https://github.com/Usha2025-git/healthyvenus-ai.git
cd healthyvenus-ai
```

---

## 📋 **What's in the Repository**

```
healthyvenus-ai/
├── app.py ..................... Desktop web app (7 tabs)
├── app_mobile.py .............. Mobile scanner app
├── requirements.txt ........... All Python dependencies
├── .gitignore ................. Excludes .env files
├── render.yaml ................ Render deployment config
│
├── src/
│   ├── agents.py .............. 3-agent AI system
│   ├── rag.py ................. Vector database
│   ├── products_db.py ......... Product database (3 products)
│   ├── search_history.py ...... Search history module
│   ├── qr_scanner_new.py ...... QR code scanning
│   ├── ingest.py .............. Data ingestion
│   └── api.py ................. FastAPI backend
│
├── data/
│   └── sample_ingredients.txt .. Ingredient database
│
└── docs/
    ├── README.md
    ├── MVP_FEATURES.md
    ├── DESKTOP_MOBILE_GUIDE.md
    └── MOBILE_SETUP.md
```

---

## 🔐 **Security: API Key Protection**

✅ **Properly Protected:**
- `.env` file is in `.gitignore` (not committed)
- API key NOT in any tracked files
- GitHub Push Protection enabled
- Safe to commit to public repo!

**Local Setup:**
```bash
# Create .env in your local copy:
echo "OPENAI_API_KEY=sk-your-key-here" > .env

# Never commit this file!
```

---

## 📦 **Installation Instructions**

### 1. Clone Repository
```bash
git clone https://github.com/Usha2025-git/healthyvenus-ai.git
cd healthyvenus-ai
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
```bash
# Create .env file with your OpenAI API key:
echo OPENAI_API_KEY=sk-your-key-here > .env
```

### 5. Run the App

**Desktop Version:**
```bash
python -m streamlit run app.py
# Opens at http://localhost:8501
```

**Mobile Version:**
```bash
python -m streamlit run app_mobile.py
# Opens at http://localhost:8502
```

---

## 🌐 **Deploy to Render.com**

### Step 1: Create Render Account
https://render.com → Sign up

### Step 2: Create New Web Service
- Click "New" → "Web Service"
- Connect GitHub repo: `healthyvenus-ai`
- Select main branch

### Step 3: Configure Deployment

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
python -m streamlit run app.py --server.port 10000
```

### Step 4: Add Environment Variable
- Go to "Environment" tab
- Add new variable:
  - Key: `OPENAI_API_KEY`
  - Value: `sk-your-api-key-here`

### Step 5: Deploy
- Click "Create Web Service"
- Wait for deployment (~2-3 minutes)
- Your app will be live at: `https://healthyvenus-ai.onrender.com`

---

## 🎯 **API Endpoints** (if deploying FastAPI)

If using the FastAPI backend:

```bash
# Desktop app (Streamlit):
GET http://localhost:8501

# Mobile app (Streamlit):
GET http://localhost:8502

# FastAPI backend (optional):
GET http://localhost:8000/docs (Auto-generated API docs)
POST http://localhost:8000/analyze (Analyze ingredients)
```

---

## 📝 **Make Changes & Push**

### Workflow:
```bash
# Make changes to files
vim app.py  # Edit files

# Check what changed
git status

# Stage changes
git add app.py src/agents.py  # Or: git add .

# Commit
git commit -m "Update feature XYZ"

# Push to GitHub
git push origin main

# Render auto-deploys! ✅
```

---

## 🔄 **Update Instructions**

### Update from Repository:
```bash
# Fetch latest
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Run again
python -m streamlit run app.py
```

---

## 🚀 **Quick Deploy Checklist**

- [ ] Repository cloned locally
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] `.env` file created with API key
- [ ] Desktop app tested locally
- [ ] Mobile app tested locally
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Environment variable set on Render
- [ ] App deployed to Render
- [ ] Testing app at Render URL

---

## 📊 **Monitoring**

### View Logs:
```bash
# Render logs:
https://dashboard.render.com/services

# Or in terminal (if using Render CLI):
render logs --service healthyvenus-ai
```

### Check Status:
```bash
git status          # Local changes
git log             # Commit history
git remote -v       # Connected remotes
```

---

## 🐛 **Troubleshooting Deployment**

**App won't start?**
- Check `.env` file has valid API key
- Check `requirements.txt` has all dependencies
- Check Render logs for errors

**Too slow?**
- Render free tier has limited resources
- Upgrade to paid tier for better performance

**API key error?**
- Make sure environment variable is set in Render
- Restart the service
- Check key is valid

**Changes not showing?**
- Wait 2-3 minutes for auto-deploy
- Check git push was successful: `git log`
- Refresh browser (hard refresh: Ctrl+Shift+R)

---

## 📚 **Resources**

- **GitHub:** https://github.com/Usha2025-git/healthyvenus-ai
- **Render Docs:** https://render.com/docs
- **Streamlit Docs:** https://docs.streamlit.io
- **LangChain Docs:** https://python.langchain.com

---

## 👥 **Contributing**

Want to contribute?

1. Fork repository
2. Create feature branch: `git checkout -b feature/xyz`
3. Make changes
4. Commit: `git commit -m "Add feature XYZ"`
5. Push: `git push origin feature/xyz`
6. Open Pull Request

---

## 📄 **License**

MIT License - Feel free to use for personal/commercial projects

---

## 🎉 **You're All Set!**

Your HealthyVenus.AI app is now:
- ✅ On GitHub
- ✅ Version controlled
- ✅ Ready to deploy
- ✅ Easy to share & collaborate

**Next Steps:**
1. Clone locally: `git clone https://github.com/Usha2025-git/healthyvenus-ai.git`
2. Run locally: `python -m streamlit run app.py`
3. Deploy to Render when ready

**Questions?** Check the README.md in the repository!
