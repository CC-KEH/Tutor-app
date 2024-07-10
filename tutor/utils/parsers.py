import dotenv
import os
import pandas as pd
from llama_parse import LlamaParse

dotenv.load_dotenv()

class Parser:
    def __init__(self):
        self.LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
        self.pdf_parser = LlamaParse(api_key=self.LLAMA_API_KEY, result_type="markdown")
    
    def txt_parser(self,file_path):
        with open(self.file_path, 'r') as file:
            return file.read()

    def csv_parser(self,file_path):
        return pd.read_csv(self.file_path).to_dict(orient="records")
