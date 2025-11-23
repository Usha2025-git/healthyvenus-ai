"""
Search History Manager
"""

SAMPLE_HISTORY = [
    {
        "timestamp": "2025-11-23 14:32",
        "query": "Is SLS safe in shampoo?",
        "product_analyzed": "Organic Coconut Shampoo",
        "safety_score": 8.5,
        "rating": "GOOD",
        "risk_level": "Low"
    },
    {
        "timestamp": "2025-11-23 14:15",
        "query": "Pure argan oil ingredients",
        "product_analyzed": "Pure Argan Oil - Premium Cold-Pressed",
        "safety_score": 9.8,
        "rating": "EXCELLENT",
        "risk_level": "Very Low"
    },
    {
        "timestamp": "2025-11-23 13:45",
        "query": "Lead in cosmetics",
        "product_analyzed": "Glamour Matte Lipstick - Red Passion",
        "safety_score": 3.2,
        "rating": "POOR",
        "risk_level": "Critical"
    },
    {
        "timestamp": "2025-11-23 13:20",
        "query": "Best clean beauty products",
        "product_analyzed": "Multiple Products",
        "safety_score": 7.5,
        "rating": "GOOD",
        "risk_level": "Low"
    },
    {
        "timestamp": "2025-11-23 12:50",
        "query": "Parabens in skincare",
        "product_analyzed": "General Query",
        "safety_score": 4.0,
        "rating": "POOR",
        "risk_level": "Moderate"
    },
    {
        "timestamp": "2025-11-23 12:30",
        "query": "Natural alternatives to retinol",
        "product_analyzed": "General Query",
        "safety_score": 8.0,
        "rating": "GOOD",
        "risk_level": "Low"
    },
    {
        "timestamp": "2025-11-23 12:05",
        "query": "Fragrance safety concerns",
        "product_analyzed": "General Query",
        "safety_score": 3.5,
        "rating": "POOR",
        "risk_level": "Moderate"
    },
    {
        "timestamp": "2025-11-23 11:40",
        "query": "Coconut oil for skin",
        "product_analyzed": "General Query",
        "safety_score": 9.2,
        "rating": "EXCELLENT",
        "risk_level": "Very Low"
    }
]

def get_search_history():
    """Get all search history"""
    return SAMPLE_HISTORY

def get_recent_searches(limit: int = 5):
    """Get recent searches"""
    return SAMPLE_HISTORY[:limit]

def format_history_for_display(history_item: dict) -> str:
    """Format history item for display"""
    risk_colors = {
        "Very Low": "🟢",
        "Low": "🟢",
        "Moderate": "🟡",
        "High": "🔴",
        "Critical": "🔴"
    }
    
    rating_emoji = {
        "EXCELLENT": "✅⭐⭐⭐",
        "GOOD": "✅⭐⭐",
        "POOR": "⚠️❌"
    }
    
    return f"""
**{history_item['timestamp']}**  
🔍 Query: *{history_item['query']}*  
📦 Product: {history_item['product_analyzed']}  
📊 Safety: {history_item['safety_score']}/10  
⭐ Rating: {rating_emoji.get(history_item['rating'], history_item['rating'])}  
{risk_colors.get(history_item['risk_level'], '❓')} Risk: {history_item['risk_level']}  
    """
