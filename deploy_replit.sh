#!/bin/bash
# 🚀 REPLIT AUTO-DEPLOY SCRIPT
# This script automatically deploys HealthyVenus.AI to Replit

echo "🚀 Starting HealthyVenus.AI Replit Deployment..."
echo ""

# Step 1: Install dependencies
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Step 2: Check API key
echo "🔑 Checking API key..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  WARNING: OPENAI_API_KEY not set in Secrets!"
    echo "   Please add it manually in Tools → Secrets"
else
    echo "✅ API key found"
fi
echo ""

# Step 3: Start the app
echo "🌐 Starting Streamlit app..."
echo ""
streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --logger.level=warning
