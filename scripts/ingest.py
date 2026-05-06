import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import the necessary modules
from app.ingestion.loader import load_txt_documents
from app.ingestion.chunker import chunk_text
from app.embeddings.openai_embedder import OpenAIEmbedder



# load all txt documents from data/raw directory
if __name__ == "__main__":
    docs = load_txt_documents("data/raw")
    chunks = chunk_text(docs)

    # extract texts from chunks
    texts = [chunk["text"] for chunk in chunks]

    # create OpenAI embedder
    embedder = OpenAIEmbedder()
    embeddings = embedder.embed_texts(texts)

    # print the number of embeddings
    print(f"Generated {len(embeddings)} embeddings")

    # print the length of the first embedding
    print("Sample embedding length:", len(embeddings[0]))