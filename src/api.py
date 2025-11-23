import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from pydantic import BaseModel
from ingest import load_pdfs
from rag import chunk_text, build_vectorstore
from agents import run_pipeline

# -------- FASTAPI APP -------- #
app = FastAPI()

# Global variable for vector store
vectorstore = None

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "HealthyVenus.AI API is running", "status": "healthy"}

@app.on_event("startup")
def startup_event():
    """Initialize vector store on startup"""
    global vectorstore
    try:
        print("Loading ingredient safety data...")
        text_data = load_pdfs()
        
        print("Chunking text...")
        chunks = chunk_text(text_data)
        
        print("Building vector database...")
        vectorstore = build_vectorstore(chunks)
        print("✅ Vector database ready!")
    except Exception as e:
        print(f"Error during startup: {e}")
        import traceback
        traceback.print_exc()
        # Don't re-raise - let the API start anyway

@app.post("/analyze")
def analyze(request: QueryRequest):
    """
    Analyzes ingredient safety for a given product or ingredient list.
    Returns scan results, toxicity scores, and safer recommendations.
    """
    if vectorstore is None:
        return {"error": "Vector store not initialized"}
    result = run_pipeline(request.query, vectorstore)
    return result
