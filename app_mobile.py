"""
🌿 HealthyVenus.AI - Mobile Scanner App
Optimized for phone scanning of products
"""

import streamlit as st
import sys
import os
from PIL import Image
import pytesseract

sys.path.insert(0, 'src')

from ingest import load_pdfs
from rag import chunk_text, build_vectorstore
from agents import run_pipeline
from products_db import get_all_products, get_product_by_name, format_product_for_display
from search_history import get_search_history, get_recent_searches, format_history_for_display
from qr_scanner_new import scan_qr_code, parse_qr_data

# Configure for mobile
st.set_page_config(
    page_title="🌿 HealthyVenus Scanner",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Mobile CSS
st.markdown("""
<style>
    * {
        font-family: 'Segoe UI', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 50%, #FFFFFF 100%);
        padding: 0 !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 50%, #FFFFFF 100%);
    }
    
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    h1 {
        color: #1a1a1a;
        text-align: center;
        font-size: 2.5em;
        margin: 10px 0;
    }
    
    h2 {
        color: #1a1a1a;
        border-bottom: 4px solid #FFB6D9;
        padding-bottom: 12px;
        font-size: 1.5em;
        margin-top: 20px;
    }
    
    h3 {
        color: #333333;
        font-size: 1.1em;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #FFB6D9 0%, #FF99C8 100%);
        color: #1a1a1a;
        border: none;
        border-radius: 12px;
        padding: 16px 24px;
        font-size: 1.1em;
        font-weight: 700;
        width: 100%;
        margin: 10px 0;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(255, 182, 217, 0.6);
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        background: white;
        color: #1a1a1a;
        border: 2px solid #FFB6D9;
        border-radius: 12px;
        padding: 12px 20px;
        font-weight: 600;
        font-size: 0.95em;
        width: 100%;
        margin: 5px 0;
    }
    
    .stFileUploader {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%);
        border: 2px dashed #FFB6D9;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    
    .metric-card {
        background: white;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 6px 20px rgba(255, 182, 217, 0.25);
        margin: 12px 0;
        border-top: 5px solid #FFB6D9;
    }
    
    .danger-card {
        border-top: 5px solid #FF6B9D;
    }
    
    .warning-card {
        border-top: 5px solid #FFA500;
    }
    
    .safe-card {
        border-top: 5px solid #90EE90;
    }
    
    .stImage {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 6px 16px rgba(255, 182, 217, 0.3);
    }
    
    @media (max-width: 768px) {
        h1 { font-size: 2em; }
        h2 { font-size: 1.3em; }
        .stButton > button { padding: 12px 16px; font-size: 1em; }
    }
</style>
""", unsafe_allow_html=True)

# Mobile header
st.markdown("""
<div style="text-align: center; padding: 15px 0; background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 50%, #FFFFFF 100%); border-radius: 15px; margin: 10px 0;">
    <h1 style="margin: 0; color: #1a1a1a;">🌿 HealthyVenus</h1>
    <p style="font-size: 1em; color: #333333; margin: 5px 0;">
        <b>Scan & Analyze</b>
    </p>
</div>
""", unsafe_allow_html=True)

# Initialize database
if 'vectorstore' not in st.session_state:
    with st.spinner("🔄 Loading database..."):
        try:
            text_data = load_pdfs()
            chunks = chunk_text(text_data)
            st.session_state.vectorstore = build_vectorstore(chunks)
            st.session_state.db_loaded = True
        except Exception as e:
            st.error(f"Error loading database: {e}")
            st.session_state.db_loaded = False

# Main tabs - Mobile optimized
tab1, tab2, tab3 = st.tabs(["📸 Scan", "🛍️ Products", "📊 History"])

# TAB 1: SCANNER
with tab1:
    st.markdown("## 📸 Quick Scan")
    
    st.markdown("""
    <div style="background: #FFF5FB; border: 2px solid #FFB6D9; border-radius: 12px; padding: 15px; margin: 10px 0;">
    📱 <b>Best on Mobile!</b><br>
    1. Point camera at product label<br>
    2. Take clear photo<br>
    3. Upload below<br>
    4. Get instant analysis
    </div>
    """, unsafe_allow_html=True)
    
    # Camera or file upload
    uploaded_file = st.camera_input(
        "📱 Use phone camera to scan label:",
        key="camera_input"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True, caption="Captured Image")
        
        # Extract text
        with st.spinner("🤖 Analyzing..."):
            try:
                extracted_text = pytesseract.image_to_string(image)
                
                if extracted_text.strip():
                    st.markdown("### 📝 Extracted Ingredients")
                    st.text_area("Recognized:", value=extracted_text[:500], height=120, disabled=True, key="mobile_ocr")
                    
                    if st.button("🚀 Analyze Full", use_container_width=True, key="analyze_mobile"):
                        if st.session_state.get('db_loaded'):
                            with st.spinner("🤖 Running AI analysis..."):
                                try:
                                    result = run_pipeline(extracted_text, st.session_state.vectorstore)
                                    
                                    st.markdown("---")
                                    st.markdown("## 📊 Results")
                                    
                                    with st.expander("🧪 Ingredients", expanded=True):
                                        st.markdown(result['ingredient_scan'])
                                    
                                    with st.expander("⚠️ Safety Score", expanded=True):
                                        st.markdown(result['toxicity_scores'])
                                    
                                    with st.expander("✅ Recommendations", expanded=True):
                                        st.markdown(result['recommendations'])
                                    
                                    st.success("✅ Analysis Complete!")
                                except Exception as e:
                                    st.error(f"Error: {e}")
                    
                else:
                    st.warning("❌ No text detected. Try again with better lighting.")
                    
            except Exception as e:
                st.warning(f"OCR not available: {e}")
    
    # Alternative: Upload file
    st.markdown("### Or upload image:")
    file_upload = st.file_uploader("Choose image:", type=["jpg", "png"], key="file_mobile")
    
    if file_upload:
        image = Image.open(file_upload)
        st.image(image, use_container_width=True)
        
        with st.spinner("🤖 Extracting..."):
            extracted_text = pytesseract.image_to_string(image)
            if extracted_text.strip():
                st.text_area("Text:", extracted_text[:300], height=100, key="mobile_file_ocr")
                if st.button("Analyze", use_container_width=True, key="btn_file_analyze"):
                    st.info("Analyzing...")

# TAB 2: PRODUCTS
with tab2:
    st.markdown("## 🛍️ Products")
    
    all_products = get_all_products()
    
    for product_key, product in all_products.items():
        st.markdown(f"""
        <div style="background: white; border-radius: 15px; padding: 15px; margin: 10px 0; box-shadow: 0 4px 12px rgba(255, 182, 217, 0.25);">
        <h3 style="color: #1a1a1a; margin: 0;">{product['name']}</h3>
        <p style="color: #666666; margin: 5px 0;">{product['brand']} • {product['price']}</p>
        <p style="color: #333333; margin: 5px 0;"><b>Rating:</b> {product['rating']}</p>
        <p style="color: #333333; margin: 5px 0;"><b>Score:</b> {product['safety_score']}/10</p>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            st.image(product['image_url'], use_container_width=True, caption=product['name'])
        except:
            st.markdown("📦 Image unavailable")
        
        if st.button(f"View Details: {product['name']}", use_container_width=True, key=f"detail_{product_key}"):
            with st.expander("Full Details", expanded=True):
                st.markdown(format_product_for_display(product))

# TAB 3: HISTORY
with tab3:
    st.markdown("## 📊 Recent Searches")
    
    history = get_search_history()
    
    for i, item in enumerate(get_recent_searches(5)):
        risk_emoji = {
            "Very Low": "🟢",
            "Low": "🟢",
            "Moderate": "🟡",
            "High": "🔴",
            "Critical": "🔴"
        }
        
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 12px; margin: 10px 0; border-left: 4px solid #FFB6D9;">
        <p style="color: #1a1a1a; margin: 5px 0;"><b>🔍 {item['query']}</b></p>
        <p style="color: #666666; margin: 3px 0; font-size: 0.9em;">⏰ {item['timestamp']}</p>
        <p style="color: #333333; margin: 3px 0; font-size: 0.9em;">Score: {item['safety_score']}/10 • {item['rating']}</p>
        <p style="color: #333333; margin: 3px 0; font-size: 0.9em;">{risk_emoji.get(item['risk_level'], '❓')} {item['risk_level']}</p>
        </div>
        """, unsafe_allow_html=True)

# Mobile footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%); border-radius: 12px; border: 2px solid #FFB6D9;">
<p style="color: #1a1a1a; margin: 5px 0;"><b>🌿 HealthyVenus Scanner</b></p>
<p style="color: #666666; font-size: 0.9em; margin: 3px 0;">Scan beauty products safely</p>
</div>
""", unsafe_allow_html=True)
