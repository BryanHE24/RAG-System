from typing import List, Dict


def chunk_text(
    documents: List[Dict],
    chunk_size: int = 500,
    overlap: int = 100
) -> List[Dict]:
    """
    Split documents into overlapping chunks.

    Each chunk keeps reference to original document.
    """

    chunks = []
    # iterate over all documents
    for doc in documents:
        text = doc["text"]
        doc_id = doc["id"]
    
        # split the document into overlapping chunks
        start = 0
        chunk_id = 0

        # while the start index is less than the length of the text
        while start < len(text):
            end = start + chunk_size

            chunk_text = text[start:end]         

            # create a chunk with id, text, and metadata
            chunk = {
                "id": f"{doc_id}_{chunk_id}",
                "text": chunk_text,
                "metadata": {
                    "source": doc["metadata"]["source"],
                    "parent_id": doc_id,
                    "chunk_index": chunk_id
                }
            }

            chunks.append(chunk)
            # move the start index forward by chunk_size - overlap
            start += chunk_size - overlap 
            chunk_id += 1

    return chunks