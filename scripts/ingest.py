import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import the necessary modules
from app.ingestion.loader import load_txt_documents
from app.ingestion.chunker import chunk_text
from app.embeddings.openai_embedder import OpenAIEmbedder
from app.vectorstore.faiss_store import FAISSVectorStore
from app.core.logging import setup_logger

logger = setup_logger(__name__) # get logger

# load all txt documents from data/raw directory
if __name__ == "__main__":
    # load all txt documents from data/raw directory
    docs = load_txt_documents("data/raw")
    # chunk the documents
    chunks = chunk_text(docs)

    # extract texts from chunks
    texts = [chunk["text"] for chunk in chunks]

    # create OpenAI embedder
    embedder = OpenAIEmbedder()
    embeddings = embedder.embed_texts(texts)

    # create FAISS vector store
    vector_store = FAISSVectorStore(
        dimension=len(embeddings[0])
    )

    # add embeddings to the vector store
    vector_store.add_embeddings(
        embeddings=embeddings,
        chunks=chunks
    )

    # save the FAISS index and metadata
    vector_store.save("storage/faiss_index")

    # log the success message
    logger.info("FAISS index saved successfully")