import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from langchain.llms import OpenAI
from dotenv import load_dotenv
from rag import retrieve_context

load_dotenv()
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

# ============ AGENT 1: INGREDIENT SCANNER ============
def ingredient_scanner_agent(query, vectorstore):
    """
    Agent 1: Scans and identifies ingredients from user query.
    Uses RAG to find relevant ingredient data.
    """
    context = retrieve_context(query, vectorstore, k=3)
    
    prompt = f"""
You are an Ingredient Scanner Agent for HealthyVenus.AI.

Your job: Identify all ingredients mentioned in the query and retrieve their safety data.

Retrieved ingredient database information:
{context}

User query: {query}

Output format:
- List all ingredients identified
- Provide brief description of each
- Note any immediate red flags

Response:
"""
    response = llm(prompt)
    return {
        "agent": "Ingredient Scanner",
        "retrieved_context": context,
        "analysis": response
    }

# ============ AGENT 2: TOXICITY SCORING ============
def toxicity_scoring_agent(query, scanner_output):
    """
    Agent 2: Analyzes toxicity and assigns safety scores (1-10).
    Classifies ingredients as safe, moderate, or harmful.
    """
    prompt = f"""
You are a Toxicity Scoring Agent for HealthyVenus.AI.

Based on the ingredient data below, assign safety scores and classify risks.

Ingredient Analysis from Scanner:
{scanner_output['analysis']}

Reference Data:
{scanner_output['retrieved_context']}

User Query: {query}

Your task:
1. Assign safety score (1-10) for each ingredient:
   - 9-10: Safe
   - 6-8: Moderate concern
   - 1-5: High risk / Avoid

2. Identify specific risks:
   - Endocrine disruptors
   - Carcinogens
   - Allergens
   - Skin irritants

3. Provide medical research citations when available

Output format:
Ingredient | Safety Score | Risk Category | Explanation

Response:
"""
    response = llm(prompt)
    return {
        "agent": "Toxicity Scoring",
        "risk_analysis": response
    }

# ============ AGENT 3: RECOMMENDATION ENGINE ============
def recommendation_agent(query, scanner_output, toxicity_output):
    """
    Agent 3: Suggests safer product alternatives and actionable recommendations.
    Generates personalized advice based on user profile.
    """
    prompt = f"""
You are a Product Recommendation Agent for HealthyVenus.AI.

Based on the ingredient analysis and toxicity scores, provide actionable recommendations.

Original Query: {query}

Ingredient Data:
{scanner_output['analysis']}

Toxicity Analysis:
{toxicity_output['risk_analysis']}

Your task:
1. Recommend safer alternative ingredients
2. Suggest cleaner product formulations
3. Provide specific brand recommendations (if known from data)
4. Create user-friendly action items
5. Explain why alternatives are better

Output format:
### Recommended Actions:
- [Action item 1]
- [Action item 2]

### Safer Alternatives:
- [Alternative ingredient/product with explanation]

### Why These Are Better:
- [Clear reasoning]

Response:
"""
    response = llm(prompt)
    return {
        "agent": "Recommendation Engine",
        "recommendations": response
    }

# ============ PIPELINE ORCHESTRATOR ============
def run_pipeline(query, vectorstore):
    """
    Orchestrates all 3 agents in sequence.
    Returns complete analysis with ingredients, scores, and recommendations.
    """
    print(f"\n🔍 Processing query: {query}\n")
    
    # Agent 1: Scan ingredients
    print("Agent 1: Scanning ingredients...")
    scanner_result = ingredient_scanner_agent(query, vectorstore)
    
    # Agent 2: Score toxicity
    print("Agent 2: Analyzing toxicity...")
    toxicity_result = toxicity_scoring_agent(query, scanner_result)
    
    # Agent 3: Generate recommendations
    print("Agent 3: Creating recommendations...")
    recommendation_result = recommendation_agent(query, scanner_result, toxicity_result)
    
    # Combine results
    final_output = {
        "query": query,
        "ingredient_scan": scanner_result["analysis"],
        "retrieved_context": scanner_result["retrieved_context"],
        "toxicity_scores": toxicity_result["risk_analysis"],
        "recommendations": recommendation_result["recommendations"]
    }
    
    print("\n✅ Analysis complete!\n")
    return final_output
