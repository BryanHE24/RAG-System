from app.core.logging import setup_logger
from app.embeddings.openai_embedder import OpenAIEmbedder
from app.ingestion.chunker import chunk_text
from app.ingestion.loader import load_txt_documents
from app.vectorstore.faiss_store import FAISSVectorStore

logger = setup_logger(__name__) # get logger

# define the ingestion pipeline class
class IngestionPipeline:
    # initialize the ingestion pipeline with dinamic chunk size and overlap
    def __init__(
        self,
        data_dir: str,
        index_path: str,
        chunk_size: int = 500,
        overlap: int = 100
    ):  
        # set the data directory and index path
        self.data_dir = data_dir
        self.index_path = index_path

        # set the chunk size and overlap
        self.chunk_size = chunk_size
        self.overlap = overlap

        # create OpenAI embedder
        self.embedder = OpenAIEmbedder()

    # define the run method
    def run(self):
        """
        Execute full ingestion pipeline.
        """

        logger.info("Starting ingestion pipeline") # log the start of the ingestion pipeline

        # Load documents
        docs = load_txt_documents(self.data_dir)

        # Chunk documents
        chunks = chunk_text(
            docs,
            chunk_size=self.chunk_size,
            overlap=self.overlap
        )

        logger.info(f"Generated {len(chunks)} chunks")

        # Extract text
        texts = [chunk["text"] for chunk in chunks]

        # Generate embeddings
        embeddings = self.embedder.embed_texts(texts)

        logger.info(f"Generated {len(embeddings)} embeddings")

        # Create vector store
        vector_store = FAISSVectorStore(
            dimension=len(embeddings[0])
        )

        # Add embeddings
        vector_store.add_embeddings(
            embeddings=embeddings,
            chunks=chunks
        )

        # Save index
        vector_store.save(self.index_path)

        logger.info("Ingestion pipeline completed successfully")