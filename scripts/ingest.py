import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ingestion.pipeline import IngestionPipeline

# define the ingestion pipeline
if __name__ == "__main__":
    # create ingestion pipeline from pipeline.py
    pipeline = IngestionPipeline(
        data_dir="data/raw",
        index_path="storage/faiss_index",
        # chunk size and overlap can be adjusted for better results
        chunk_size=500,
        overlap=100
    )

    pipeline.run() # run the ingestion pipeline