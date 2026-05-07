import os
import uuid
from typing import List, Dict

from app.core.logging import setup_logger

logger = setup_logger(__name__) # get logger

def load_txt_documents(data_dir: str) -> List[Dict]:
    """
    Load all .txt documents from a directory.

    Returns:
        List of documents with structure:
        {
            "id": str,
            "text": str,
            "metadata": {"source": str}
        }
    """
    documents = []

    # log the directory from which documents are being loaded
    logger.info(f"Loading documents from: {data_dir}")

    # iterate over all files in the directory
    for filename in os.listdir(data_dir):
        # skip if not a txt file
        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(data_dir, filename)
        # read the file
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # create a document with id, text, and metadata
            doc = {
                "id": str(uuid.uuid4()),
                "text": text,
                "metadata": {
                    "source": filename
                }
            }

            documents.append(doc)

            # log the document that was loaded
            logger.info(f"Loaded document: {filename}")

        except Exception as e:
            # log the error if the document could not be loaded
            logger.error(f"Error loading {filename}: {e}")

    # log the total number of documents loaded
    logger.info(f"Total documents loaded: {len(documents)}")

    return documents