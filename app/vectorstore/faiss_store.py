import json
import os
from typing import List, Dict

import faiss
import numpy as np

# FAISS vector store class
class FAISSVectorStore:
    # initialize the FAISS vector store
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    # add embeddings to the vector store
    def add_embeddings(
        self,
        embeddings: List[List[float]],
        chunks: List[Dict]
    ):
        """
        Add embeddings and corresponding chunk metadata.
        """
        # convert embeddings to numpy array
        vectors = np.array(embeddings).astype("float32") 

        # add embeddings to the FAISS index
        self.index.add(vectors)

        # add metadata to the FAISS index
        for chunk in chunks:
            self.metadata.append(chunk)

    # search for similar embeddings
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 3
    ):
        """
        Perform similarity search.
        """
        # convert query embedding to numpy array
        query_vector = np.array([query_embedding]).astype("float32")
    
        # search for similar embeddings
        distances, indices = self.index.search(query_vector, top_k)

        results = []
    
        # iterate over similar embeddings
        for idx, distance in zip(indices[0], distances[0]):
            if idx == -1:
                continue

            results.append({
                "score": float(distance),
                "chunk": self.metadata[idx]
            })

        return results

    # save the FAISS index and metadata
    def save(self, path: str):
        """
        Save FAISS index and metadata.
        """

        os.makedirs(path, exist_ok=True)

        faiss.write_index(
            self.index,
            os.path.join(path, "index.faiss")
        )

        with open(os.path.join(path, "metadata.json"), "w") as f:
            json.dump(self.metadata, f)

    # load the FAISS index and metadata
    def load(self, path: str):
        """
        Load FAISS index and metadata.
        """

        self.index = faiss.read_index(
            os.path.join(path, "index.faiss")
        )

        with open(os.path.join(path, "metadata.json"), "r") as f:
            self.metadata = json.load(f)