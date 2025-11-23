"""
Product Database with Ratings, Resources, and Images
"""

PRODUCTS_DATABASE = {
    "shampoo": {
        "name": "Organic Coconut Shampoo",
        "category": "Hair Care",
        "rating": "GOOD",
        "safety_score": 8.5,
        "description": "Gentle, sulfate-free shampoo with coconut extract and natural oils",
        "ingredients": [
            "Water",
            "Coconut Oil",
            "Aloe Vera",
            "Glycerin",
            "Vitamin E",
            "Natural Fragrance"
        ],
        "pros": [
            "✅ Sulfate-free (no SLS or SLES)",
            "✅ Natural ingredients",
            "✅ Gentle on scalp",
            "✅ Affordable",
            "✅ Eco-friendly packaging"
        ],
        "cons": [
            "⚠️ May not lather as much as chemical shampoos",
            "⚠️ Shorter shelf life"
        ],
        "image_url": "https://images.unsplash.com/photo-1535585633066-ba51f1529157?w=400&h=400&fit=crop",
        "resources": [
            {
                "title": "EWG Skin Deep - Shampoo Safety Guidelines",
                "url": "https://www.ewg.org/guides/cleaners/",
                "type": "Research",
                "credibility": "High"
            },
            {
                "title": "FDA - Cosmetic Ingredient Review: Coconut Oil",
                "url": "https://www.fda.gov/cosmetics/",
                "type": "Regulatory",
                "credibility": "High"
            },
            {
                "title": "Dermatological Review: Natural Hair Care Ingredients",
                "url": "https://www.ncbi.nlm.nih.gov/pmc/",
                "type": "Medical Study",
                "credibility": "High"
            },
            {
                "title": "Consumer Reports - Best Natural Shampoos 2025",
                "url": "https://www.consumerreports.org/",
                "type": "Product Review",
                "credibility": "Medium"
            }
        ],
        "brand": "Natural Botanicals Co.",
        "price": "$12.99",
        "where_to_buy": ["Amazon", "Sephora", "Local Health Stores"]
    },
    
    "oil": {
        "name": "Pure Argan Oil - Premium Cold-Pressed",
        "category": "Skincare/Hair Care",
        "rating": "EXCELLENT",
        "safety_score": 9.8,
        "description": "100% pure, cold-pressed argan oil with zero additives. Clean, premium ingredients.",
        "ingredients": [
            "100% Pure Argan Oil (Argania Spinosa Kernel Oil)"
        ],
        "pros": [
            "✅ Single ingredient - 100% pure",
            "✅ Cold-pressed, no solvents",
            "✅ Rich in Vitamin E and antioxidants",
            "✅ Works for face, hair, and body",
            "✅ Long shelf life",
            "✅ Certified organic available",
            "✅ Zero harmful chemicals"
        ],
        "cons": [
            "⚠️ May be too oily for very oily skin types",
            "⚠️ Premium pricing"
        ],
        "image_url": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=400&h=400&fit=crop",
        "resources": [
            {
                "title": "Journal of Cosmetic Dermatology - Argan Oil Benefits",
                "url": "https://onlinelibrary.wiley.com/journal/14736365",
                "type": "Peer-Reviewed Study",
                "credibility": "High"
            },
            {
                "title": "NIH - Argan Oil: Nutritional Composition and Effects",
                "url": "https://www.ncbi.nlm.nih.gov/",
                "type": "Medical Research",
                "credibility": "High"
            },
            {
                "title": "International Journal of Cosmetic Science - Oil Stability Study",
                "url": "https://onlinelibrary.wiley.com/",
                "type": "Scientific Research",
                "credibility": "High"
            },
            {
                "title": "Certified Organic Standards - Argan Oil",
                "url": "https://www.usda.gov/organic",
                "type": "Certification",
                "credibility": "High"
            },
            {
                "title": "Expert Review: Cold-Pressed vs Refined Argan Oils",
                "url": "https://www.healthline.com/",
                "type": "Expert Article",
                "credibility": "High"
            }
        ],
        "brand": "Pure Moroccan Essentials",
        "price": "$24.99",
        "where_to_buy": ["Amazon", "Sephora", "Ulta", "Morocco Direct"]
    },
    
    "lipstick": {
        "name": "Glamour Matte Lipstick - Red Passion",
        "category": "Makeup/Lips",
        "rating": "POOR",
        "safety_score": 3.2,
        "description": "Matte finish lipstick with questionable ingredient sourcing and multiple known allergens",
        "ingredients": [
            "Paraffin Wax",
            "Ozokerite",
            "Lead Acetate (potential trace)",
            "Carmine (Cochineal Extract)",
            "Talc",
            "Fragrance (undisclosed)",
            "FD&C Red No. 5",
            "FD&C Yellow No. 5",
            "Methylparaben",
            "Propylparaben",
            "Cadmium"
        ],
        "pros": [
            "✅ Good color payoff",
            "✅ Long-lasting (8+ hours)",
            "✅ Affordable"
        ],
        "cons": [
            "🚨 Contains lead acetate (neurotoxin)",
            "🚨 Talc may contain asbestos",
            "🚨 Synthetic dyes (FD&C Red/Yellow)",
            "🚨 Undisclosed 'fragrance' (3000+ chemicals)",
            "🚨 Parabens present (endocrine disruptor)",
            "🚨 Cadmium detected (carcinogen)",
            "🚨 Carmine from insects (not vegan)",
            "🚨 No transparency in sourcing",
            "🚨 Multiple known allergens",
            "🚨 Not dermatologist tested"
        ],
        "image_url": "https://images.unsplash.com/photo-1586894977186-f975f868d30f?w=400&h=400&fit=crop",
        "resources": [
            {
                "title": "FDA Warning - Lead in Lipsticks 2020",
                "url": "https://www.fda.gov/cosmetics/lipsticks",
                "type": "FDA Report",
                "credibility": "Critical"
            },
            {
                "title": "Berkeley Test Lab - Heavy Metals in Lipsticks Study",
                "url": "https://news.berkeley.edu/2020/10/26/",
                "type": "Scientific Study",
                "credibility": "High"
            },
            {
                "title": "Environmental Defense Fund - Cosmetic Safety Database",
                "url": "https://www.edf.org/health/cosmetics-database",
                "type": "Health Research",
                "credibility": "High"
            },
            {
                "title": "Campaign for Safe Cosmetics - Lipstick Investigation",
                "url": "https://www.safecosmetics.org/",
                "type": "Advocacy Research",
                "credibility": "High"
            },
            {
                "title": "WHO Report - Health Risks of Talc in Cosmetics",
                "url": "https://www.who.int/",
                "type": "Medical Advisory",
                "credibility": "Critical"
            }
        ],
        "brand": "Glamour Beauty Inc.",
        "price": "$8.99",
        "where_to_buy": ["Drug Stores", "Mass Market Retailers"],
        "recommendation": "⛔ AVOID - Multiple toxic ingredients detected. Switch to natural alternatives like 100% plant-based or mineral lipsticks."
    }
}

def get_product_by_name(name: str):
    """Get product details by name"""
    name_lower = name.lower()
    for key, product in PRODUCTS_DATABASE.items():
        if name_lower in key or name_lower in product["name"].lower():
            return product
    return None

def get_all_products():
    """Get all products"""
    return PRODUCTS_DATABASE

def get_products_by_rating(rating: str):
    """Get products by rating"""
    rating_upper = rating.upper()
    return {
        name: product for name, product in PRODUCTS_DATABASE.items()
        if product["rating"] == rating_upper
    }

def get_products_by_category(category: str):
    """Get products by category"""
    return {
        name: product for name, product in PRODUCTS_DATABASE.items()
        if category.lower() in product["category"].lower()
    }

def format_product_for_display(product: dict) -> str:
    """Format product data for display"""
    rating_emoji = {
        "EXCELLENT": "✅⭐⭐⭐",
        "GOOD": "✅⭐⭐",
        "POOR": "⚠️❌"
    }
    
    output = f"""
### {product['name']}

**Brand:** {product['brand']}  
**Price:** {product['price']}  
**Category:** {product['category']}  
**Rating:** {rating_emoji.get(product['rating'], product['rating'])} {product['rating']}  
**Safety Score:** {product['safety_score']}/10

---

#### Description
{product['description']}

---

#### Ingredients
"""
    
    for ingredient in product['ingredients']:
        output += f"- {ingredient}\n"
    
    output += "\n#### Pros\n"
    for pro in product['pros']:
        output += f"{pro}\n"
    
    output += "\n#### Cons\n"
    for con in product['cons']:
        output += f"{con}\n"
    
    output += "\n#### Resources & References\n"
    for i, resource in enumerate(product['resources'], 1):
        output += f"{i}. **{resource['title']}** ({resource['type']})  \n"
        output += f"   Credibility: {resource['credibility']}  \n"
        output += f"   [Link]({resource['url']})  \n\n"
    
    output += f"\n#### Where to Buy\n"
    for store in product['where_to_buy']:
        output += f"- {store}\n"
    
    if "recommendation" in product:
        output += f"\n#### ⚠️ Important Recommendation\n{product['recommendation']}\n"
    
    return output
