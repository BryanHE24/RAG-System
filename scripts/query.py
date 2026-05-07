import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.query.query_pipeline import QueryPipeline

if __name__ == "__main__":
    # create query pipeline
    pipeline = QueryPipeline(
        index_path="storage/faiss_index" # path to FAISS index
    )

    # loop until user exits
    while True:
        # get query from user                                                               
        query = input("\nEnter query (or 'exit'): ") 

        # exit if user enters 'exit'
        if query.lower() == "exit":
            break

        # search for similar chunks
        results = pipeline.search(query)

        print("\nTop Results:\n")

        # print results
        for i, result in enumerate(results, start=1):
            print(f"Result #{i}")
            print(f"Score: {result['score']}")
            print(f"Source: {result['chunk']['metadata']['source']}")
            print(f"Text: {result['chunk']['text']}")
            print("-" * 50)