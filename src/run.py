import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ingest import load_pdfs
from rag import chunk_text, build_vectorstore
from agents import run_pipeline

print("Loading ingredient data...")
text = load_pdfs()

print("Chunking...")
chunks = chunk_text(text)

print("Building vector store...")
vs = build_vectorstore(chunks)

print("\n" + "="*50)
print("HEALTHYVENUS.AI - INGREDIENT SAFETY ANALYZER")
print("="*50 + "\n")

while True:
    query = input("\n🔍 Enter product/ingredient to analyze (or 'quit' to exit): ")
    if query.lower() == 'quit':
        break
    
    result = run_pipeline(query, vs)
    
    print("\n" + "="*50)
    print("📊 ANALYSIS RESULTS")
    print("="*50)
    print(f"\n🧪 Ingredient Scan:\n{result['ingredient_scan']}")
    print(f"\n⚠️ Toxicity Scores:\n{result['toxicity_scores']}")
    print(f"\n✅ Recommendations:\n{result['recommendations']}")
    print("\n" + "="*50)
