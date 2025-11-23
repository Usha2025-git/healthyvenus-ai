# 🌿 HealthyVenus.AI - Desktop & Mobile Apps

## 🖥️ **Desktop Version** (Current)
Full-featured dashboard with all tools

**URL:** http://localhost:8501

```bash
python -m streamlit run app.py
```

### Features:
- 🔍 Text-based ingredient analyzer
- 📸 OCR label scanner
- 📱 QR code scanner
- 📚 Complete ingredient database
- 🛍️ Product catalog (Excellent/Good/Poor)
- 📊 Search history
- ℹ️ How it works guide
- ⚙️ System settings

### Best For:
- 🖥️ Desktop/laptop research
- 📋 Detailed analysis
- 📚 Learning about ingredients
- 💼 Product comparison

---

## 📱 **Mobile Version** (Optimized)
Phone-friendly scanning app with camera support

**URL:** http://localhost:8502 (or custom port)

```bash
python -m streamlit run app_mobile.py --logger.level=error --client.toolbarMode=minimal
```

### Features:
- 📸 **Phone Camera Input** - Point & shoot labels
- 🛍️ Product browser
- 📊 Search history
- ⚡ Fast & responsive
- 📱 Touch-optimized UI

### Best For:
- 📱 In-store scanning
- 📸 Quick label photos
- 🏪 Shopping verification
- ⚡ Fast analysis on the go

---

## 🎯 **Product Images**

All products have beautiful images:

### ✅ Organic Coconut Shampoo (GOOD)
- Image: Professional shampoo bottle
- Status: ✓ Working

### ✅ Pure Argan Oil (EXCELLENT)  
- Image: Golden oil bottle
- Status: ✓ Working

### ✅ Glamour Matte Lipstick (POOR)
- Image: Red lipstick product
- Status: ✓ Working

---

## 🚀 **How to Run Both Versions**

### Terminal 1 - Desktop App:
```bash
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -m streamlit run app.py
```
**Access:** http://localhost:8501

### Terminal 2 - Mobile App:
```bash
cd c:\Users\sowmi\Desktop\healthyvenus_ai
python -m streamlit run app_mobile.py
```
**Access:** http://localhost:8502

---

## 📱 **Mobile App - 3 Tabs**

### Tab 1: 📸 Scan
- 📱 **Phone Camera** - Use device camera to capture labels
- 📤 Upload image - Alternative upload method
- 🤖 AI Analysis - Instant ingredient breakdown
- 📊 Safety scoring - Toxicity assessment

### Tab 2: 🛍️ Products
- Browse featured products
- View ratings (Excellent/Good/Poor)
- See product images
- Read full details

### Tab 3: 📊 History
- Recent searches (5 items)
- Safety scores
- Risk levels
- Timestamps

---

## 💡 **Which Version to Use?**

### Use **Desktop Version** when:
- 🖥️ Using a computer/laptop
- 📚 Want detailed information
- 🔍 Comparing multiple products
- 📋 Need full feature set
- 💼 Professional research

### Use **Mobile Version** when:
- 📱 Using a smartphone/tablet
- 🏪 Shopping in stores
- ⚡ Need quick analysis
- 📸 Scanning product labels
- 🚀 Want lightweight interface

---

## 🌐 **Network Access**

### Local Machine:
```
Desktop: http://localhost:8501
Mobile: http://localhost:8502
```

### From Other Devices (Phone/Tablet):
```
Desktop: http://<your-computer-ip>:8501
Mobile: http://<your-computer-ip>:8502
```

Get your IP:
```powershell
ipconfig
# Look for "IPv4 Address" under your network adapter
# Example: 192.168.1.68
```

---

## 📸 **Mobile Camera Feature**

The mobile app includes **native phone camera input**:

1. Open mobile app on phone
2. Tap 📱 "Use phone camera to scan label"
3. Point at product label
4. Take photo
5. Get instant analysis

Works on:
- ✅ iOS (Safari, Chrome)
- ✅ Android (Chrome, Firefox)
- ✅ Modern browsers with camera access

---

## 🎨 **Both Versions Feature**

✅ Pastel pink + white design  
✅ Dark text for readability  
✅ Beautiful gradients  
✅ Smooth animations  
✅ Professional styling  
✅ Touch-responsive  

---

## 📋 **File Guide**

```
healthyvenus_ai/
├── app.py .................. Desktop app (7 tabs)
├── app_mobile.py ........... Mobile app (3 tabs)
└── src/
    ├── products_db.py ...... Product database
    ├── search_history.py ... Search records
    ├── qr_scanner_new.py ... QR scanning
    ├── agents.py ........... AI agents
    ├── rag.py .............. Vector DB
    └── ingest.py ........... Data loading
```

---

## 🔧 **Troubleshooting**

### Port Already in Use?
```bash
# Desktop on different port:
streamlit run app.py --server.port 8503

# Mobile on different port:
streamlit run app_mobile.py --server.port 8504
```

### Camera Not Working?
- Ensure browser has camera permission
- Try Chrome/Firefox (best support)
- Check phone's camera permissions

### Images Not Loading?
- All images from Unsplash (requires internet)
- Check internet connection
- Refresh browser

---

## 📞 **Support**

- 🖥️ Desktop Issues → Use desktop version
- 📱 Mobile Issues → Use mobile version
- 📸 Scanning Issues → Check lighting/focus
- 🔗 Connection Issues → Check IP/port

---

**Ready to scan! 🌿✨**
