from typing import List
from openai import OpenAI
from app.core.config import OPENAI_API_KEY, OPENAI_BASE_URL

# OpenAI embedder class
class OpenAIEmbedder:
    # initialize the OpenAI embedder
    def __init__(self, model: str = "text-embedding-3-small"):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL
        )
        self.model = model

    # embed texts using batching
    def embed_texts(self, texts: List[str], batch_size: int = 20) -> List[List[float]]:
        """
        Embed texts using batching.
        """
        all_embeddings = []
        # iterate over texts in batches
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]

            # create embeddings for the batch
            response = self.client.embeddings.create(
                model=self.model,
                input=batch
            )

            # extract embeddings from response
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)

        return all_embeddings