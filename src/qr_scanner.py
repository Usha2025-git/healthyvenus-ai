"""
QR Code Scanner for product labels
"""

import numpy as np
from PIL import Image
import io

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

def scan_qr_code(image) -> dict:
    """
    Scan QR code from image
    Returns product information or ingredient data
    """
    try:
        if not HAS_CV2:
            return {
                "success": False,
                "data": None,
                "type": "NO_CV2",
                "message": "OpenCV not available. Please install: pip install opencv-python"
            }
        
        # Convert PIL image to numpy array
        if isinstance(image, Image.Image):
            image_np = np.array(image)
        else:
            image_np = image
        
        # Initialize QR code detector
        detector = cv2.QRCodeDetector()
        
        # Detect and decode QR code
        data, bbox, straight_qr = detector.detectAndDecode(image_np)
        
        if data:
            return {
                "success": True,
                "data": data,
                "type": "QR_CODE",
                "message": f"✅ QR Code detected: {data}"
            }
        else:
            return {
                "success": False,
                "data": None,
                "type": "NO_QR",
                "message": "No QR code detected in image. Try a clearer photo."
            }
    except Exception as e:
        return {
            "success": False,
            "data": None,
            "type": "ERROR",
            "message": f"Error scanning QR code: {str(e)}"
        }

def parse_qr_data(qr_data: str) -> dict:
    """
    Parse QR code data and extract product information
    """
    # Sample QR code format: PRODUCT:SHAMPOO:Organic Coconut Shampoo:8.5
    if "PRODUCT:" in qr_data:
        parts = qr_data.split(":")
        if len(parts) >= 4:
            return {
                "source": "QR_CODE",
                "product_type": parts[1],
                "product_name": parts[2],
                "safety_score": parts[3] if len(parts) > 3 else "Unknown",
                "extracted": True
            }
    
    # If it's a URL
    if qr_data.startswith("http"):
        return {
            "source": "QR_URL",
            "url": qr_data,
            "extracted": True
        }
    
    # Generic data
    return {
        "source": "QR_DATA",
        "raw_data": qr_data,
        "extracted": True
    }

def get_sample_qr_codes() -> dict:
    """Get sample QR code data for demonstration"""
    return {
        "shampoo": {
            "format": "PRODUCT:SHAMPOO:Organic Coconut Shampoo:8.5",
            "description": "Shampoo Product QR"
        },
        "oil": {
            "format": "PRODUCT:OIL:Pure Argan Oil:9.8",
            "description": "Oil Product QR"
        },
        "lipstick": {
            "format": "PRODUCT:LIPSTICK:Glamour Matte Lipstick:3.2",
            "description": "Lipstick Product QR"
        },
        "url": {
            "format": "https://healthyvenus.ai/product/shampoo",
            "description": "Product URL QR"
        }
    }
