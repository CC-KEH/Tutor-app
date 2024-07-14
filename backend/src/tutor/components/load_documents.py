import os
import nest_asyncio
import dotenv
import pandas as pd
from tutor.utils.parsers import Parser
from pinecone import Pinecone, ServerlessSpec
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.pinecone import PineconeVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.core import StorageContext
from llama_index.core import Settings

dotenv.load_dotenv()
nest_asyncio.apply()


class DocumentLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
        self.PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        self.pc = Pinecone(api_key=self.PINECONE_API_KEY)

        self.parser = Parser()
        self.file_extractors = {
            ".pdf": self.parser.pdf_parser,
            ".csv": self.parser.csv_parser,
            ".txt": self.parser.txt_parser
        }

    def parse_data(self):
        try:
            
            reader = SimpleDirectoryReader(os.path.join(self.folder_path),
                                        file_extractor=self.file_extractors,
                                        recursive=True,
                                        num_files_limit=100)
            
            
            documents = reader.load_data(num_workers=4)
            
            # data = []
            # for doc in documents:
            #     data.append(doc.text)

            # print("Data : ",data)
            # print("Successfully parsed the documents.")
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
            storage_type = "llama_index"    # llama_index or langchain
        ):
        
        # index = self.pc.Index(index_name)
        # index.describe_index_stats()
        
        # text_splitter = RecursiveCharacterTextSplitter(
        #     separators = ["\n\n","\n"," "], 
        #     chunk_size = 200,  
        #     chunk_overlap  = 120, 
        #     length_function = len 
        # )
        
        # chunks = []
        # for text in data:
        #     ch = text_splitter.split_text(text)
        #     chunks.extend(ch)
        
        # print("Total chunks : ",len(chunks))
        # for idx, chunk in enumerate(chunks):
        #     text = chunk
        #     text = text.replace("\n",". ")
        #     text = text.replace("\t",". ")

        #     vector = embedding_model.get_text_embedding(text)
        #     vector_id = f"doc_chunk_{idx}"
            
        #     index.upsert(
        #         vectors = 
        #         [
        #             {
        #                 "id" : vector_id,
        #                 "values" : vector,
        #                 "metadata" : {'source': '','text' : text}
        #             }
        #         ],
        #         namespace=namespace,
        #     )
        
        # print("Successfully stored to database")
        # return True,"Stored to database"
        
        
        try:
            pc = Pinecone(api_key=self.PINECONE_API_KEY)
            pc_index_instance = pc.Index(index_name)
            
            if storage_type == "llama_index":
                vector_store = PineconeVectorStore(pinecone_index=pc_index_instance,namespace=namespace)
                storage_context = StorageContext.from_defaults(vector_store=vector_store)
                print("upserting data to pinecone")
                Settings.chunk_size = 100
                Settings.chunk_overlap = 10
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
        
        


