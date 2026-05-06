import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ingestion.loader import load_txt_documents
from app.ingestion.chunker import chunk_text


# load all txt documents from data/raw directory
if __name__ == "__main__":
    docs = load_txt_documents("data/raw")
    print(f"Loaded {len(docs)} documents")

    # chunk the documents
    chunks = chunk_text(docs) 

    print(f"Created {len(chunks)} chunks")
    
    # print each chunk
    for chunk in chunks:
        print(chunk)