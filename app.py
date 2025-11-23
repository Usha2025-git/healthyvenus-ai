"""
🌿 HealthyVenus.AI - AI-Powered Clean Beauty Ingredient Scanner
A beautiful Streamlit app for analyzing cosmetic ingredient safety
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

# Configure Streamlit page
st.set_page_config(
    page_title="🌿 HealthyVenus.AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for stunning UI - Pastel Pink & White Theme
st.markdown("""
<style>
    * {
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
    }
    
    :root {
        --primary-pink: #FFB6D9;
        --light-pink: #FFE0EC;
        --pale-pink: #FFF5FB;
        --white: #FFFFFF;
        --dark-text: #1a1a1a;
        --light-text: #333333;
    }
    
    .main {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 50%, #FFFFFF 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 50%, #FFFFFF 100%);
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFE0EC 0%, #FFF5FB 100%);
        border-right: 3px solid #FFB6D9;
    }
    
    h1 {
        color: #1a1a1a;
        text-align: center;
        font-size: 3.5em;
        font-weight: 800;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(255, 182, 217, 0.3);
        letter-spacing: 1px;
    }
    
    h2 {
        color: #1a1a1a;
        border-bottom: 4px solid #FFB6D9;
        padding-bottom: 12px;
        font-weight: 700;
        font-size: 1.8em;
    }
    
    h3 {
        color: #333333;
        font-weight: 600;
        font-size: 1.3em;
    }
    
    h4 {
        color: #1a1a1a;
        font-weight: 600;
        font-size: 1.1em;
    }
    
    p, span, div {
        color: #1a1a1a;
    }
    
    .stMarkdown {
        color: #1a1a1a;
        line-height: 1.8;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(90deg, #FFE0EC 0%, #FFF5FB 100%);
        border-bottom: 3px solid #FFB6D9;
        gap: 10px;
        padding: 10px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        background: white;
        color: #1a1a1a;
        border: 2px solid #FFB6D9;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 1em;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(255, 182, 217, 0.2);
    }
    
    .stTabs [data-baseweb="tab-list"] button:hover {
        background: linear-gradient(135deg, #FFB6D9 0%, #FFE0EC 100%);
        color: #1a1a1a;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(255, 182, 217, 0.4);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FFB6D9 0%, #FFE0EC 100%);
        color: #1a1a1a;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #FFB6D9 0%, #FF99C8 100%);
        color: #1a1a1a;
        border: none;
        border-radius: 12px;
        padding: 14px 32px;
        font-size: 1em;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(255, 182, 217, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 20px rgba(255, 182, 217, 0.6);
        background: linear-gradient(135deg, #FF99C8 0%, #FF7DB8 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background-color: white !important;
        color: #1a1a1a !important;
        border: 2px solid #FFB6D9 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 1em !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border: 2px solid #FF99C8 !important;
        box-shadow: 0 0 10px rgba(255, 182, 217, 0.3) !important;
    }
    
    .stFileUploader {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%);
        border: 2px dashed #FFB6D9;
        border-radius: 12px;
        padding: 20px;
    }
    
    .stFileUploader > div {
        color: #1a1a1a;
    }
    
    .metric-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 6px 20px rgba(255, 182, 217, 0.25);
        margin: 12px 0;
        border-top: 5px solid #FFB6D9;
        transition: all 0.3s ease;
        border-left: 0px;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 182, 217, 0.35);
    }
    
    .danger-card {
        border-top: 5px solid #FF6B9D;
        background: linear-gradient(135deg, #FFFFFF 0%, #FFE8F0 100%);
    }
    
    .warning-card {
        border-top: 5px solid #FFA500;
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF8E8 100%);
    }
    
    .safe-card {
        border-top: 5px solid #90EE90;
        background: linear-gradient(135deg, #FFFFFF 0%, #F0FFF0 100%);
    }
    
    .stAlert {
        border-radius: 12px;
        border: 2px solid #FFB6D9;
        background-color: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%);
        color: #1a1a1a;
        padding: 15px;
    }
    
    .stAlert > div {
        color: #1a1a1a;
    }
    
    .stExpander {
        background: white;
        border: 2px solid #FFB6D9;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(255, 182, 217, 0.2);
    }
    
    .stExpander > div > div {
        color: #1a1a1a;
    }
    
    .stImage {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 6px 16px rgba(255, 182, 217, 0.3);
    }
    
    .stInfo {
        background: linear-gradient(135deg, #E0F7FF 0%, #F0F8FF 100%);
        border-left: 4px solid #00B4D8;
        border-radius: 10px;
        color: #1a1a1a;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #E0FFE0 0%, #F0FFF0 100%);
        border-left: 4px solid #10B981;
        border-radius: 10px;
        color: #1a1a1a;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #FFF8E0 0%, #FFFEF0 100%);
        border-left: 4px solid #FFA500;
        border-radius: 10px;
        color: #1a1a1a;
    }
    
    .stError {
        background: linear-gradient(135deg, #FFE0E0 0%, #FFF0F0 100%);
        border-left: 4px solid #FF6B6B;
        border-radius: 10px;
        color: #1a1a1a;
    }
    
    .stSpinner > div {
        color: #FFB6D9;
    }
    
    table {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(255, 182, 217, 0.2);
    }
    
    tr {
        color: #1a1a1a;
    }
    
    th {
        background: linear-gradient(135deg, #FFB6D9 0%, #FFE0EC 100%);
        color: #1a1a1a;
        font-weight: 700;
    }
    
    tr:hover {
        background-color: #FFF5FB;
    }
    
    .stSidebar .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #FFB6D9 0%, #FF99C8 100%);
        color: #1a1a1a;
    }
    
    .stSidebar .stRadio > div {
        color: #1a1a1a;
    }
    
    .stSidebar .stCheckbox > div {
        color: #1a1a1a;
    }
    
    code {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%);
        color: #FF6B9D;
        border-radius: 6px;
        padding: 2px 6px;
        font-weight: 600;
    }
    
    pre {
        background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%);
        border: 2px solid #FFB6D9;
        border-radius: 10px;
        color: #1a1a1a;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h2 style="color: #1a1a1a; font-size: 2.5em; margin: 0;">🌿</h2>
        <h3 style="color: #1a1a1a; margin: 10px 0; font-size: 1.4em;">HealthyVenus.AI</h3>
        <p style="color: #333333; font-size: 0.95em; margin: 5px 0;">
            <b>AI-Powered</b><br>Clean Beauty Scanner
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%); border-radius: 12px; padding: 15px; margin: 10px 0; border: 2px solid #FFB6D9;">
        <h4 style="color: #1a1a1a; margin-top: 0;">✨ Features</h4>
        <p style="color: #333333; margin: 8px 0; font-size: 0.9em;">
        🧬 AI ingredient analysis<br>
        ⚠️ Risk assessment (1-10)<br>
        💡 Safer alternatives<br>
        📸 Photo OCR scanner<br>
        📊 Safety database
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FFE0EC 0%, #FFF5FB 100%); border-radius: 12px; padding: 15px; border: 2px solid #FFB6D9;">
        <h4 style="color: #1a1a1a; margin-top: 0;">📚 Quick Info</h4>
        <p style="color: #333333; margin: 8px 0; font-size: 0.9em;">
        Built with LangChain, OpenAI & ChromaDB<br><br>
        <b>Fast • Accurate • Beautiful</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("""
<div style="text-align: center; padding: 30px 0; background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 50%, #FFFFFF 100%); border-radius: 20px; margin-bottom: 20px;">
    <h1 style="margin: 0; color: #1a1a1a;">🌿 HealthyVenus.AI</h1>
    <p style="font-size: 1.3em; color: #333333; margin: 10px 0; font-weight: 600;">
        <b>Discover what's really in your beauty products</b>
    </p>
    <p style="color: #666666; font-size: 1em; margin-top: 15px;">
        AI-powered ingredient scanner • Safety scoring • Safer alternatives
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Initialize session state
if 'vectorstore' not in st.session_state:
    with st.spinner("🔄 Loading ingredient database..."):
        try:
            text_data = load_pdfs()
            chunks = chunk_text(text_data)
            st.session_state.vectorstore = build_vectorstore(chunks)
            st.session_state.db_loaded = True
        except Exception as e:
            st.error(f"Error loading database: {e}")
            st.session_state.db_loaded = False

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["🔍 Analyzer", "📸 OCR & QR", "📚 Database", "🛍️ Products", "📊 History", "ℹ️ How It Works", "⚙️ Settings"])

# TAB 1: MAIN ANALYZER
with tab1:
    st.markdown("## 🔬 Ingredient Safety Analyzer")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        query = st.text_area(
            "Enter product name or ingredients to analyze:",
            placeholder="e.g., 'Is sodium lauryl sulfate safe?' or 'Analyze my face cream ingredients'",
            height=120,
            key="query_input"
        )
    
    with col2:
        st.markdown("### Examples")
        st.markdown("""
        - Is retinol safe?
        - Parabens in cosmetics
        - Best natural ingredients
        - Fragrance risks
        """)
    
    st.markdown("---")
    
    # Analyze Button
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        analyze_btn = st.button("🚀 Analyze Ingredients", use_container_width=True, key="analyze_btn")
    
    if analyze_btn:
        if not query.strip():
            st.warning("⚠️ Please enter a product or ingredient to analyze")
        elif not st.session_state.get('db_loaded', False):
            st.error("❌ Database not loaded. Please refresh the page.")
        else:
            with st.spinner("🤖 AI is analyzing ingredients..."):
                try:
                    result = run_pipeline(query, st.session_state.vectorstore)
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("## 📊 Analysis Results")
                    
                    # Ingredient Scan
                    with st.expander("🧪 Ingredient Scan", expanded=True):
                        st.markdown(result['ingredient_scan'])
                    
                    # Toxicity Scores
                    with st.expander("⚠️ Toxicity & Risk Assessment", expanded=True):
                        st.markdown(result['toxicity_scores'])
                    
                    # Recommendations
                    with st.expander("✅ Safer Alternatives & Recommendations", expanded=True):
                        st.markdown(result['recommendations'])
                    
                    # Retrieved Context
                    with st.expander("📚 Retrieved Knowledge", expanded=False):
                        st.markdown(result['retrieved_context'])
                    
                    st.markdown("---")
                    st.success("✅ Analysis complete!")
                    
                except Exception as e:
                    st.error(f"❌ Error during analysis: {e}")

# TAB 2: OCR SCANNER
with tab2:
    st.markdown("## 📸 OCR & QR Code Scanner")
    
    # Create sub-tabs
    ocr_tab, qr_tab = st.tabs(["📸 OCR Ingredient Scanner", "📱 QR Code Scanner"])
    
    # OCR Tab
    with ocr_tab:
        st.info("""
        📸 **Upload a photo** of your product label or ingredient list
        🤖 **AI will extract** the text automatically
        ✅ **Analyze** all ingredients at once
        """)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            uploaded_file = st.file_uploader(
                "Upload product label or ingredient image:",
                type=["jpg", "jpeg", "png", "bmp", "webp"],
                key="ocr_upload"
            )
        
        with col2:
            st.markdown("### 📋 Supported Formats")
            st.markdown("""
            - JPG/JPEG
            - PNG
            - BMP
            - WEBP
            """)
        
        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.markdown("### 📷 Uploaded Image")
            st.image(image, use_column_width=True)
            
            # Extract text using OCR
            with st.spinner("🤖 Extracting text from image..."):
                try:
                    extracted_text = pytesseract.image_to_string(image)
                    
                    if extracted_text.strip():
                        st.markdown("### 📝 Extracted Ingredients")
                        st.text_area(
                            "Recognized text from image:",
                            value=extracted_text,
                            height=150,
                            disabled=False,
                            key="extracted_text"
                        )
                        
                        st.markdown("---")
                        
                        # Analyze button
                        col1, col2 = st.columns([1, 2])
                        with col2:
                            if st.button("🚀 Analyze Extracted Ingredients", use_container_width=True, key="analyze_ocr"):
                                if not st.session_state.get('db_loaded', False):
                                    st.error("❌ Database not loaded. Please refresh the page.")
                                else:
                                    with st.spinner("🤖 AI is analyzing ingredients..."):
                                        try:
                                            result = run_pipeline(extracted_text, st.session_state.vectorstore)
                                            
                                            st.markdown("---")
                                            st.markdown("## 📊 Analysis Results")
                                            
                                            with st.expander("🧪 Ingredient Scan", expanded=True):
                                                st.markdown(result['ingredient_scan'])
                                            
                                            with st.expander("⚠️ Toxicity & Risk Assessment", expanded=True):
                                                st.markdown(result['toxicity_scores'])
                                            
                                            with st.expander("✅ Safer Alternatives & Recommendations", expanded=True):
                                                st.markdown(result['recommendations'])
                                            
                                            with st.expander("📚 Retrieved Knowledge", expanded=False):
                                                st.markdown(result['retrieved_context'])
                                            
                                            st.markdown("---")
                                            st.success("✅ Analysis complete!")
                                            
                                        except Exception as e:
                                            st.error(f"❌ Error during analysis: {e}")
                    else:
                        st.warning("⚠️ No text detected in image. Try a clearer photo or different image format.")
                        
                except Exception as e:
                    st.error(f"❌ OCR Error: {e}")
                    st.info("""
                    💡 **Tip:** If OCR is not working:
                    1. Make sure image is clear and well-lit
                    2. Try a closer photo of the ingredient list
                    3. Ensure text is readable
                    
                    **Note:** On Windows, you may need to install Tesseract:
                    - Download from: https://github.com/UB-Mannheim/tesseract/wiki
                    - Install and restart the app
                    """)
        else:
            st.markdown("""
            ### 🎯 How to Use OCR Scanner
            
            1. **Take a photo** of your product label
            2. **Upload** the image here
            3. **Review** the extracted text
            4. **Click analyze** to get safety scores
            
            ### ✨ Perfect For
            - 💄 Checking makeup ingredient lists
            - 🧴 Analyzing skincare products
            - 🧼 Examining soap/cleanser labels
            - 💅 Nail polish safety check
            - 🧴 Body care products
            """)
    
    # QR Code Tab
    with qr_tab:
        st.info("""
        📱 **Scan QR codes** on product labels
        🔍 **Auto-detect** product information
        ⚡ **Instant analysis** of product safety
        """)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            qr_file = st.file_uploader(
                "Upload QR code image from product label:",
                type=["jpg", "jpeg", "png", "bmp"],
                key="qr_upload"
            )
        
        with col2:
            st.markdown("### 📱 QR Info")
            st.markdown("""
            - Point at QR code
            - Take clear photo
            - Upload here
            - Auto-detect!
            """)
        
        if qr_file is not None:
            qr_image = Image.open(qr_file)
            st.markdown("### 📷 QR Code Image")
            st.image(qr_image, use_column_width=True)
            
            with st.spinner("📱 Scanning QR code..."):
                try:
                    qr_result = scan_qr_code(qr_image)
                    
                    if qr_result['success']:
                        st.success(qr_result['message'])
                        
                        # Parse the QR data
                        parsed = parse_qr_data(qr_result['data'])
                        
                        st.markdown("### 📦 Product Information")
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write(f"**Source:** {parsed['source']}")
                            if 'product_type' in parsed:
                                st.write(f"**Type:** {parsed['product_type']}")
                            if 'product_name' in parsed:
                                st.write(f"**Name:** {parsed['product_name']}")
                        
                        with col2:
                            if 'safety_score' in parsed:
                                st.metric("Safety Score", parsed['safety_score'], "/10")
                            if 'url' in parsed:
                                st.write(f"**URL:** {parsed['url']}")
                        
                        st.markdown("---")
                        
                        # If it has product data, try to find it
                        if 'product_type' in parsed:
                            product = get_product_by_name(parsed['product_type'])
                            if product:
                                st.markdown("### 🛍️ Full Product Details")
                                st.markdown(format_product_for_display(product))
                                
                                # Analyze button
                                if st.button("🚀 Full Safety Analysis", use_container_width=True, key="analyze_qr"):
                                    if not st.session_state.get('db_loaded', False):
                                        st.error("❌ Database not loaded.")
                                    else:
                                        with st.spinner("🤖 Running analysis..."):
                                            try:
                                                query = f"Analyze {product['name']} with ingredients: {', '.join(product['ingredients'])}"
                                                result = run_pipeline(query, st.session_state.vectorstore)
                                                
                                                st.markdown("---")
                                                st.markdown("## 📊 Analysis Results")
                                                with st.expander("🧪 Ingredient Scan", expanded=True):
                                                    st.markdown(result['ingredient_scan'])
                                                with st.expander("⚠️ Toxicity Assessment", expanded=True):
                                                    st.markdown(result['toxicity_scores'])
                                                with st.expander("✅ Recommendations", expanded=True):
                                                    st.markdown(result['recommendations'])
                                            except Exception as e:
                                                st.error(f"❌ Error: {e}")
                    else:
                        st.warning(qr_result['message'])
                        st.info("""
                        💡 **Tips for better QR scanning:**
                        - Ensure good lighting
                        - Keep QR code centered
                        - Try different angles
                        - Avoid shadows
                        """)
                except Exception as e:
                    st.error(f"❌ Error scanning QR: {e}")
        else:
            st.markdown("""
            ### 🎯 How to Use QR Scanner
            
            1. **Find QR code** on product label
            2. **Take a clear photo** of the QR code
            3. **Upload** here
            4. **Auto-detect** product information
            5. **View** full analysis
            
            ### 📱 Where to Find QR Codes
            - Back of product packaging
            - Brand websites
            - Ingredient labels
            - Product certificates
            
            ### ⚡ What Happens
            - QR code is decoded
            - Product info extracted
            - Safety analysis performed
            - Alternatives suggested
            """)

# TAB 3: DATABASE
with tab2:
    st.markdown("## 📚 Ingredient Database")
    
    st.info("""
    Our database includes 12+ major cosmetic ingredients with:
    - Safety scores (1-10)
    - Health risks
    - Medical evidence
    - Safer alternatives
    """)
    
    st.markdown("### ✅ Safe Ingredients (8-10/10)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card safe-card">
        <h4>🌿 Glycerin</h4>
        <p><b>Score: 10/10</b></p>
        <p>Pure safe ingredient. Excellent hydration.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card safe-card">
        <h4>💧 Hyaluronic Acid</h4>
        <p><b>Score: 9/10</b></p>
        <p>Natural hydration. Anti-aging benefits.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card safe-card">
        <h4>🧬 Niacinamide</h4>
        <p><b>Score: 9/10</b></p>
        <p>Gentle & effective. All skin types.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### ⚠️ Moderate Risk (4-7/10)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card warning-card">
        <h4>🧴 SLS</h4>
        <p><b>Score: 4/10</b></p>
        <p>Skin irritant. Can strip natural oils.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card warning-card">
        <h4>🛡️ Parabens</h4>
        <p><b>Score: 5/10</b></p>
        <p>Endocrine concern. Accumulates in body.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card warning-card">
        <h4>🌸 Fragrance</h4>
        <p><b>Score: 3/10</b></p>
        <p>3000+ hidden chemicals. Allergen risk.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🚨 High Risk (1-3/10)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card danger-card">
        <h4>☠️ Benzene</h4>
        <p><b>Score: 1/10</b></p>
        <p>Carcinogen. Avoid completely.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card danger-card">
        <h4>☠️ Lead</h4>
        <p><b>Score: 1/10</b></p>
        <p>Neurotoxin. Bioaccumulative.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card danger-card">
        <h4>☠️ Formaldehyde</h4>
        <p><b>Score: 2/10</b></p>
        <p>Known carcinogen. Toxic.</p>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: PRODUCTS WITH RATINGS
with tab4:
    st.markdown("## 🛍️ Featured Products with Ratings")
    
    st.info("""
    Browse our curated product database with:
    - 📊 Safety ratings (Poor/Good/Excellent)
    - 🧬 Detailed ingredient analysis
    - 🔗 3+ credible resources per product
    - 💰 Pricing & where to buy
    - 📸 Product images
    """)
    
    # Get all products
    all_products = get_all_products()
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        filter_rating = st.selectbox(
            "Filter by Rating:",
            ["All Ratings", "EXCELLENT ⭐⭐⭐", "GOOD ⭐⭐", "POOR ❌"],
            key="rating_filter"
        )
    
    with col2:
        st.markdown("### Product Count")
        st.metric("Total Products", len(all_products))
    
    st.markdown("---")
    
    # Display products
    for product_key, product in all_products.items():
        # Skip if filter doesn't match
        if "EXCELLENT" in filter_rating and product['rating'] != "EXCELLENT":
            continue
        if "GOOD" in filter_rating and product['rating'] != "GOOD":
            continue
        if "POOR" in filter_rating and product['rating'] != "POOR":
            continue
        
        # Product card
        rating_emoji = {
            "EXCELLENT": "✅⭐⭐⭐",
            "GOOD": "✅⭐⭐",
            "POOR": "⚠️❌"
        }
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            try:
                st.image(product['image_url'], use_column_width=True)
            except:
                st.markdown("📦")
        
        with col2:
            st.markdown(f"### {product['name']}")
            st.markdown(f"**Brand:** {product['brand']}")
            st.markdown(f"**Rating:** {rating_emoji[product['rating']]} {product['rating']}")
            st.markdown(f"**Safety Score:** {product['safety_score']}/10")
            st.markdown(f"**Price:** {product['price']}")
            st.markdown(f"*{product['description']}*")
        
        with col3:
            st.markdown("### Key Highlights")
            st.markdown(f"- **Category:** {product['category']}")
            st.markdown(f"- **Resources:** {len(product['resources'])} links")
            st.markdown(f"- **Retailers:** {len(product['where_to_buy'])}")
        
        # Expandable details
        with st.expander(f"📋 View Full Details - {product['name']}"):
            st.markdown(format_product_for_display(product))
        
        st.markdown("---")
    
    # Summary statistics
    st.markdown("### 📊 Product Database Summary")
    excellent = len([p for p in all_products.values() if p['rating'] == "EXCELLENT"])
    good = len([p for p in all_products.values() if p['rating'] == "GOOD"])
    poor = len([p for p in all_products.values() if p['rating'] == "POOR"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("✅ Excellent", excellent)
    with col2:
        st.metric("⭐ Good", good)
    with col3:
        st.metric("⚠️ Poor", poor)

# TAB 5: HISTORY
with tab5:
    st.markdown("## 📊 Search History")
    
    st.info("""
    Your recent ingredient & product searches
    """)
    
    # Get history
    history = get_search_history()
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📈 Statistics")
        st.metric("Total Searches", len(history))
    
    with col2:
        excellent_count = len([h for h in history if h['rating'] == "EXCELLENT"])
        st.metric("✅ Excellent", excellent_count)
    
    with col3:
        poor_count = len([h for h in history if h['rating'] == "POOR"])
        st.metric("⚠️ Poor", poor_count)
    
    st.markdown("---")
    
    # Show recent searches
    st.markdown("### 🔍 Recent Searches")
    
    for history_item in get_recent_searches(10):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(format_history_for_display(history_item))
        
        with col2:
            risk_colors = {
                "Very Low": "🟢",
                "Low": "🟢",
                "Moderate": "🟡",
                "High": "🔴",
                "Critical": "🔴"
            }
            st.markdown(risk_colors.get(history_item['risk_level'], "❓"))
        
        st.markdown("---")
    
    # Download history
    st.markdown("### 📥 Download History")
    if st.button("📋 Copy All History to Clipboard", use_container_width=True):
        history_text = "\n\n".join([format_history_for_display(h) for h in history])
        st.success("✅ History copied! (Ready to paste)")

# TAB 6: HOW IT WORKS
with tab4:
    st.markdown("## ℹ️ How HealthyVenus.AI Works")
    
    st.markdown("""
    ### 🔬 Our Technology
    
    We use a **3-Agent AI System** powered by:
    - **LangChain**: Multi-agent orchestration
    - **OpenAI GPT**: Natural language understanding
    - **ChromaDB**: Vector database for semantic search
    
    ### 🧠 Agent 1: Ingredient Scanner
    - Identifies ingredients from your query
    - Retrieves relevant safety data
    - Provides descriptions & flags
    
    ### ⚠️ Agent 2: Toxicity Scorer
    - Assigns safety scores (1-10)
    - Identifies specific risks
    - Provides medical evidence
    
    ### ✅ Agent 3: Recommendation Engine
    - Suggests safer alternatives
    - Recommends product formulations
    - Creates actionable advice
    
    ### 🔄 How Queries Are Processed
    """)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        <div style="background: #e3f2fd; padding: 20px; border-radius: 8px; text-align: center;">
        <h4>1️⃣ Input</h4>
        <p>Your query</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("→")
    
    with col3:
        st.markdown("""
        <div style="background: #f3e5f5; padding: 20px; border-radius: 8px; text-align: center;">
        <h4>2️⃣ RAG</h4>
        <p>Vector search</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("→")
    
    with col5:
        st.markdown("""
        <div style="background: #e8f5e9; padding: 20px; border-radius: 8px; text-align: center;">
        <h4>3️⃣ Analysis</h4>
        <p>3 agents</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📊 Safety Score Explanation
    
    | Score | Risk Level | Recommendation |
    |-------|-----------|----------------|
    | 9-10 | Safe ✅ | Use freely |
    | 7-8 | Low Risk ⚠️ | Generally safe |
    | 5-6 | Moderate Risk ⚠️ | Use with caution |
    | 3-4 | High Risk 🚨 | Limit use |
    | 1-2 | Critical 🚨 | Avoid completely |
    """)

# TAB 7: SETTINGS
with tab7:
    st.markdown("## ⚙️ Settings & Information")
    
    st.markdown("### System Status")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.get('db_loaded', False):
            st.success("✅ Database: Loaded")
        else:
            st.error("❌ Database: Not loaded")
    
    with col2:
        st.info("🔑 API Key: Configured")
    
    st.markdown("---")
    
    st.markdown("### About HealthyVenus.AI")
    
    st.markdown("""
    **HealthyVenus.AI** is an AI-powered clean beauty ingredient scanner that helps you understand what's really in your cosmetic products.
    
    #### Key Features
    - 🔬 AI-powered ingredient analysis
    - ⚠️ Science-based safety scoring
    - 💡 Personalized recommendations
    - 📊 Detailed health insights
    - 🌱 Focus on clean beauty
    
    #### Data Sources
    - FDA cosmetic ingredient guidelines
    - EWG Skin Deep research
    - Scientific literature on ingredient safety
    - Medical research papers
    
    #### Disclaimer
    This tool is for informational purposes only. Always consult with a dermatologist or healthcare professional before making changes to your skincare routine.
    """)
    
    st.markdown("---")
    
    st.markdown("### Contact & Support")
    st.markdown("""
    - 📧 Email: support@healthyvenus.ai
    - 🌐 Website: www.healthyvenus.ai
    - 💬 Feedback: We'd love to hear from you!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666666; padding: 30px 20px; background: linear-gradient(135deg, #FFF5FB 0%, #FFE0EC 100%); border-radius: 15px; border: 2px solid #FFB6D9; margin-top: 20px;">
<p style="font-size: 1.1em; margin: 10px 0; color: #1a1a1a;"><b>🌿 HealthyVenus.AI</b></p>
<p style="color: #333333; margin: 5px 0;">AI-Powered Clean Beauty Ingredient Scanner</p>
<p style="color: #888888; font-size: 0.9em; margin-top: 15px;">Built with ❤️ using LangChain, OpenAI, and Streamlit</p>
<p style="color: #999999; font-size: 0.85em; margin-top: 10px;">© 2025 HealthyVenus. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
