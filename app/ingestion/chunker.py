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
        chunk_index = 0

        # while the start index is less than the length of the text
        while start < len(text):
            end = start + chunk_size

            # Prevent cutting words in half, ugly chunks, poorer embeddings
            if end < len(text):
                while end < len(text) and text[end] != " ":
                    end += 1
            # get the chunk content
            chunk_content = text[start:end].strip()      

            # create a chunk with id, text, and metadata
            chunk = {
                "id": f"{doc_id}_{chunk_index}",
                "text": chunk_content,
                "metadata": {
                    "source": doc["metadata"]["source"],
                    "parent_id": doc_id,
                    "chunk_index": chunk_index,
                    "chunk_size": len(chunk_content)
                }
            }
            # add the chunk to the list of chunks
            chunks.append(chunk)        
            # move the start index forward by chunk_size - overlap
            start += chunk_size - overlap
            chunk_index += 1

    return chunks