from app.embeddings.openai_embedder import OpenAIEmbedder
from app.vectorstore.faiss_store import FAISSVectorStore


# query pipeline class
class QueryPipeline:
    # initialize the query pipeline
    def __init__(self, index_path: str):
        self.embedder = OpenAIEmbedder()

        # load FAISS index and metadata
        self.vector_store = FAISSVectorStore(dimension=1536)
        self.vector_store.load(index_path)

    # search for similar chunks
    def search(self, query: str, top_k: int = 3):
        """
        Search relevant chunks for a query.
        """

        # embed the query
        query_embedding = self.embedder.embed_texts([query])[0]

        # search for similar chunks
        results = self.vector_store.search( 
            query_embedding=query_embedding, # query embedding
            top_k=top_k # number of similar chunks to return
        )

        # return the results
        return results