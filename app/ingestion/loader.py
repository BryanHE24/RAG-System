import os
import uuid
from typing import List, Dict


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

        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return documents