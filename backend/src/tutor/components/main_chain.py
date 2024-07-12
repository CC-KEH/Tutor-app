import os
import json
import traceback
import pandas as pd
from tutor.components.load_documents import DocumentLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from llama_index.core.agent import ReActAgent
from pydantic import BaseModel
from tutor.templates.templates import mcq_template , QnA_agent_context
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.embeddings.google import GooglePaLMEmbedding
import google.generativeai as genai
from llama_index.llms.gemini import Gemini
import json
from dotenv import load_dotenv
import genai

load_dotenv()

class parseFormat(BaseModel):
    number: int
    subject: str
    tone: str
    response_template: str

class Master:
    def __init__(self,knowledge_base_path):
        self.knowledge_base_path = knowledge_base_path
        self.ducument_loader = DocumentLoader(folder_path=self.knowledge_base_path)
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.default_embedding_model = GooglePaLMEmbedding(model_name="models/embedding-gecko-001", api_key=self.GOOGLE_API_KEY)
        self.tools = []
        self.study_agent_llm = Gemini(model="models/gemini-pro")
        self.coding_agent_llm = None
        self.numerical_agent_llm = None
    
    
    def learn(self,index_name,embedding_model=None,namespace="common"):
        if embedding_model is None:
            embedding_model = self.default_embedding_model
        
        try:
            _,_,data = self.ducument_loader.parse_data()
            
            _,_,retrieval_index = self.ducument_loader.store_to_index(
                data=data,
                index_name= index_name,
                namespace=namespace,
                embedding_model=embedding_model
            )
            
            query_engine = retrieval_index.as_query_engine(llm=self.study_agent_llm, verbose=True)
            query_engine_tool = QueryEngineTool(
                                    query_engine=query_engine,
                                    metadata=ToolMetadata(
                                        name = "Transformers",
                                        description="this gives the study materials for transformers provided by user. Use this for fetching and reading study materials for transformers.",
                                    ),
                                )
            self.tools.append(query_engine_tool)
            print("Master has learnt the study materials.")
            
        except Exception as e:
            print(e)
            return f"Error: {e}"
        
        
    
    def generate_mcq(self, prompt):
        
        print("Tools : ", self.tools)
        
        # parser = PydanticOutputParser(parseFormat)
        # json_parsed_data = parser.parse(json_str)
        # formatted_prompt = mcq_template.format(**json_parsed_data.dict())
        
        # print("Formatted prompt :",formatted_prompt)
        
        agent = ReActAgent.from_tools(self.tools, llm=self.study_agent_llm, verbose=True, context=QnA_agent_context)
        
        agent.query(prompt)




# key = os.getenv("OPENAI_API_KEY")

# print("Value of MY_VARIABLE:", key)

# llm = ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo", temperature=0.3)


# quiz_generation_prompt = PromptTemplate(
#     input_variables=["text", "number", "grade", "tone", "response_json"],
#     template=template)



# quiz_chain=LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)


# quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=template)

# review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# # This is an Overall Chain where we run the two chains in Sequence
# generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
#                                         output_variables=["quiz", "review"], verbose=True,)