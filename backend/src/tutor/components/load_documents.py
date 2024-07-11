import os
import nest_asyncio
import dotenv
import pandas as pd
from tutor.utils.parsers import Parser
from pinecone import Pinecone, ServerlessSpec
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import StorageContext

dotenv.load_dotenv()
nest_asyncio.apply()


class DocumentLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
        self.PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        self.parser = Parser()
        self.file_extractors = {
            ".pdf": self.parser.pdf_parser,
            ".csv": self.parser.csv_parser,
            ".txt": self.parser.txt_parser
        }
        self.embed_model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"

    def parse_data(self):
        try:
            pdf_documents = SimpleDirectoryReader(os.path.join(self.folder_path,"pdf"),file_extractor=self.file_extractor).load_data()  
            csv_documents = SimpleDirectoryReader(os.path.join(self.folder_path,"csv"),file_extractor=self.file_extractor).load_data()  
            txt_documents = SimpleDirectoryReader(os.path.join(self.folder_path,"txt"),file_extractor=self.file_extractor).load_data()  
            
            return {
                "parsed_pdf" : pdf_documents,
                "parser_cvs" : csv_documents,
                "parsed_txt" : txt_documents
            }
        except Exception as e:
            return f"Error: {e}"
    
    def store_to_pinecone(
            self,
            data,
            index_name,
            namespace,
            embedding_model,
            storage_type = "default"    # default or custom
        ):
        
        try:
            pc = Pinecone(api_key=self.PINECONE_API_KEY)
            pc_index_instance = pc.Index(index_name)
            
            if storage_type == "default":
                vector_store = PineconeVectorStore(pinecone_index=pc_index_instance,namespace=namespace)
                storage_context = StorageContext.from_defaults(vector_store=vector_store)
                retrieval_index = VectorStoreIndex.from_documents(
                    data, 
                    storage_context=storage_context,
                    embed_model=embedding_model
                )
            
            return True,"Stored to database", retrieval_index
        
        except Exception as e:
            return False, f"Error: {e}", None


