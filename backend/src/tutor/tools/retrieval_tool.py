# from langchain.tools import BaseTool
from pinecone import Pinecone
from llama_index.embeddings.google import GooglePaLMEmbedding
import os
from pydantic import Field


# def retrieve_data(retrival_index,topics: str) -> str:
#     """
#     Tool for retrieving data based on topics. Input should be the topics separated by comma.
#     Useful for getting context from database.
    
#     Args:
#         topics (str): Topic names separated by comma.
    
#     Returns:
#         str: Retrieved data joined by newlines.
#     """
#     GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#     PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
#     embedding_model = GooglePaLMEmbedding(model_name="models/embedding-gecko-001", api_key=GOOGLE_API_KEY)
#     vectors = embedding_model.get_text_embedding(topics)
#     pc = Pinecone(api_key=PINECONE_API_KEY)
#     index = pc.Index("tutor")
#     query_results = index.query(queries=vectors, include_metadata=True, top_k=10)
    
#     data = []
    
#     for result in query_results['matches']:
#         data.append(result['metadata']['text'])
    
#     return '\n\n'.join(data)

def retrieve_data(retrieval_index, topics: str) -> str:
    """
    Tool for retrieving data based on topics from a provided retrieval index.
    Input should be the topics separated by comma.
    Useful for getting context from the index.
    
    Args:
        retrieval_index: The VectorStoreIndex to query from.
        topics (str): Topic names separated by comma.
    
    Returns:
        str: Retrieved data joined by newlines.
    """
    # Create a retriever from the index
    retriever = retrieval_index.as_retriever(similarity_top_k=20)
    
    # Query the retriever
    retrieved_nodes = retriever.retrieve(topics)
    
    # Extract the content from retrieved nodes
    data = [node.node.get_content() for node in retrieved_nodes]
    
    print("number_of_chunks: ",len(data))
    for idx, chunk in enumerate(data):
        print(len(chunk))
    
    return '\n\n'.join(data)