# check available models in your gemini account
import os
from dotenv import load_dotenv
from google import genai

# load api key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "").strip()

if not api_key:
    raise ValueError("GEMINI_API_KEY missing in .env file")

# connect to gemini
client = genai.Client(api_key=api_key)

def check_models():
    print("Fetching models from Gemini API...")
    
    # get all models list
    models = list(client.models.list())
    
    print("\nMain models you can use:")
    for m in models:
        name = m.name.replace("models/", "")
        
        # main models for chat and vision
        if name in ["gemini-2.5-flash", "gemini-2.5-pro"]:
            print(f"- {name} (recommended for chat, vision, tools)")
            
        # models for vector embeddings and rag
        elif name in ["gemini-embedding-001", "gemini-embedding-2"]:
            print(f"- {name} (for text embeddings and rag)")

if __name__ == "__main__":
    check_models()
