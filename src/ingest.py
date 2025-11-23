from pypdf import PdfReader
import os

def load_pdfs(folder_path="data"):
    """Load all ingredient safety PDFs and text files from data folder"""
    all_text = ""
    
    # Load PDFs
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"Loading {filename}...")
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text = page.extract_text() or ""
                all_text += text + "\n"
    
    # Load TXT files as fallback
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            txt_path = os.path.join(folder_path, filename)
            print(f"Loading {filename}...")
            with open(txt_path, 'r', encoding='utf-8') as f:
                all_text += f.read() + "\n"
    
    return all_text

if __name__ == "__main__":
    text = load_pdfs()
    print(f"Loaded {len(text)} characters of ingredient data")
