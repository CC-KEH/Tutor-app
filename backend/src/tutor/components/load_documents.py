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

    def parse_data(self):
        try:
            documents = SimpleDirectoryReader(os.path.join(self.folder_path),file_extractor=self.file_extractors).load_data()  
            
            print("Successfully parsed the documents.")
            return True,"Parsed data",documents

        except Exception as e:
            print(e)
            return False,f"Error: {e}",None
    
    def store_to_index(
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
                print("upserting data to pinecone")
                retrieval_index = VectorStoreIndex.from_documents(
                    data, 
                    storage_context=storage_context,
                    embed_model=embedding_model
                )
                print("upserted data to pinecone")
            
            print("Successfully stored to database")
            return True,"Stored to database", retrieval_index
        
        except Exception as e:
            print(e)
            return False, f"Error: {e}", None


