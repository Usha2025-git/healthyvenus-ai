# 🚀 HealthyVenus.AI - Replit Deployment Guide

## ✅ Quick Replit Setup

### **Step 1: Import from GitHub to Replit**
1. Go to https://replit.com
2. Click **"+ Create"** → **"Import from GitHub"**
3. Paste: `https://github.com/Usha2025-git/healthyvenus-ai`
4. Click **Import project**
5. Wait for Replit to clone the repo

---

## 🔑 Step 2: Set Environment Variables

**In Replit Dashboard:**
1. Click **Tools** (left sidebar) → **Secrets**
2. Add new secret:
   - **Key:** `OPENAI_API_KEY`
   - **Value:** `sk-your-actual-key-here`
3. Click **Add new secret**

---

## 🎯 Step 3: Install Dependencies

**In Replit Terminal:**
```bash
pip install -r requirements.txt
```

Wait for all packages to install (takes ~2-3 min).

---

## 🌐 Step 4: Run the App

### **Option A: Desktop App (Recommended)**
```bash
streamlit run app.py
```

Replit will automatically:
- Install Streamlit
- Create a public URL
- Show something like: `https://replit.username-healthyvenus-ai.repl.co`

### **Option B: Mobile App**
```bash
streamlit run app_mobile.py
```

---

## 📱 Step 5: Access Your Live Website

Once running, Replit shows:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: https://replit.username-healthyvenus-ai.repl.co
```

**Share this URL** - it's your live website! ✅

---

## 🔄 Keep App Running (Optional)

### **Option 1: Use Replit's Always On**
1. Upgrade to Replit Pro
2. Enable "Always On" in project settings
3. App runs 24/7

### **Option 2: Use UptimeRobot (Free)**
1. Go to https://uptimerobot.com
2. Create account
3. Add monitor for your Replit URL
4. Pings URL every 5 min to keep it running

---

## 🐛 Troubleshooting

### **Issue: Dependencies not found**
```bash
pip install --upgrade -r requirements.txt
```

### **Issue: Streamlit port error**
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### **Issue: API key not working**
1. Double-check key in Secrets
2. Restart Replit shell: `Ctrl+Shift+C`
3. Re-run app

### **Issue: App times out**
- Replit free tier has 1-hour timeout
- Use UptimeRobot to keep it alive
- Or upgrade to Replit Pro

---

## 📊 Features Available on Replit

✅ **7-Tab Desktop App**
- Ingredient Analyzer
- OCR Scanner
- QR Code Scanner
- Product Database
- Products with Ratings
- Search History
- How It Works Guide

✅ **Mobile Scanning**
- Camera input (works on Replit!)
- Quick product lookup
- Touch-friendly UI

✅ **3-Agent AI System**
- Ingredient Scanner
- Toxicity Scoring
- Recommendation Engine

✅ **Product Database**
- 3 featured products
- Safety ratings (Poor/Good/Excellent)
- Images from Unsplash
- Research resources

---

## 🎉 Your Live Website

**URL Format:**
```
https://replit.@username-healthyvenus-ai.repl.co
```

**Share with:**
- Friends & family
- Social media
- Embed in website
- Add to portfolio

---

## 💡 Pro Tips

1. **Custom Domain** (Paid): Add your own domain in Replit settings
2. **Invite Collaborators**: Click Share → Add editor
3. **Fork for Friends**: They can fork your Replit to their account
4. **GitHub Sync**: Changes push to GitHub automatically
5. **Analytics**: Check traffic in Replit dashboard

---

## 📞 Quick Commands

```bash
# Install all dependencies
pip install -r requirements.txt

# Run desktop app
streamlit run app.py

# Run mobile app
streamlit run app_mobile.py

# Check Python version
python --version

# Test API key
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key loaded:', 'Yes' if os.getenv('OPENAI_API_KEY') else 'No')"
```

---

## 🚀 Next Steps

1. ✅ Import to Replit (done)
2. ✅ Add API key to Secrets (do this)
3. ✅ Install dependencies (do this)
4. ✅ Run `streamlit run app.py` (do this)
5. ✅ Share live URL (do this)
6. 🎉 **Your website is LIVE!**

---

## 📚 Resources

- **Replit Docs:** https://docs.replit.com
- **Streamlit Docs:** https://docs.streamlit.io
- **OpenAI API:** https://platform.openai.com/docs
- **GitHub Repo:** https://github.com/Usha2025-git/healthyvenus-ai

---

## 🎯 Your Live URL

**Copy & share this after deploying:**
```
https://replit.@username-healthyvenus-ai.repl.co
```

**Status:** 🟢 Ready to deploy to Replit!

---

**Built with ❤️ - HealthyVenus.AI MVP**

*AI-powered clean beauty ingredient scanner now LIVE on Replit!*
