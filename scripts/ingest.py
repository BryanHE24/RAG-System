import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ingestion.loader import load_txt_documents

# load all txt documents from data/raw directory
if __name__ == "__main__":
    docs = load_txt_documents("data/raw")

    print(f"Loaded {len(docs)} documents")
    # print each document
    for doc in docs:
        print(doc)