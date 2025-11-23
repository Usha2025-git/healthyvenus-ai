from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize embeddings
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize LLM
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0)

def chunk_text(text):
    """Split text into chunks for embedding"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_text(text)

def build_vectorstore(chunks):
    """Create ChromaDB vector store from chunks"""
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name="ingredient_safety_db"
    )
    return vectorstore

def retrieve_context(query, vectorstore, k=3):
    """Retrieve relevant ingredient safety information"""
    docs = vectorstore.similarity_search(query, k=k)
    context = "\n\n".join([d.page_content for d in docs])
    return context
