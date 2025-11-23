#!/bin/sh
# Replit Run Script for HealthyVenus.AI

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Starting HealthyVenus.AI..."
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
