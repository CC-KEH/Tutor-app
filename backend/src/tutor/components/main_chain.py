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
from tutor.templates.templates import mcq_template , science_agent_context
from llama_index.embeddings.google import GooglePaLMEmbedding
import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from langchain.tools import BaseTool
from langchain.agents import Tool
from tutor.tools.retrieval_tool import retrieve_data    
from langchain.output_parsers import PydanticOutputParser
from llama_index.core.tools import FunctionTool
from functools import partial
import json
from dotenv import load_dotenv
import genai

load_dotenv()

class parseFormat(BaseModel):
    number: int
    topics: str
    difficulty: str
    response_template: str

class Master:
    def __init__(self,knowledge_base_path):
        self.knowledge_base_path = knowledge_base_path
        self.ducument_loader = DocumentLoader(folder_path=self.knowledge_base_path)
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.default_embedding_model = GooglePaLMEmbedding(model_name="models/embedding-gecko-001", api_key=self.GOOGLE_API_KEY)
        self.tools = []
        self.gemini_llm = Gemini(model="models/gemini-pro")
        self.coding_agent_llm = None
        self.numerical_agent_llm = None
    
    
    def learn(self,index_name,embedding_model=None,namespace=""):
        if embedding_model is None:
            embedding_model = self.default_embedding_model
        
        
        _,_,data = self.ducument_loader.parse_data()
        
        _,_,retrieval_index = self.ducument_loader.store_to_index(
                data=data,
                index_name= index_name,
                namespace=namespace,
                embedding_model=embedding_model
            )
        
        retrieve_data_with_index = partial(retrieve_data, retrieval_index)

        # Then, create the FunctionTool
        retrieve_data_tool = FunctionTool.from_defaults(
            fn=retrieve_data_with_index,
            name="RetrieveDataTool",
            description="Tool for retrieving data based on the provided topics. This will give out the study materials. Input should be the topics separated by comma."
        )
        print("Tool made")
        
        self.tools.append(retrieve_data_tool)
        print("Master has learnt the study materials.")
        
        return True
        
        
        # try:
        #     _,_,data = self.ducument_loader.parse_data()
            
        #     _,_,retrieval_index = self.ducument_loader.store_to_index(
        #         data=data,
        #         index_name= index_name,
        #         namespace=namespace,
        #         embedding_model=embedding_model
        #     )
            
        #     query_engine = retrieval_index.as_query_engine(llm=self.study_agent_llm, verbose=True, similarity_top_k=20)
        #     query_engine_tool = QueryEngineTool(
        #                             query_engine=query_engine,
        #                             metadata=ToolMetadata(
        #                                 name = "study_materials",
        #                                 description="""this gives the context based on the study materials provided by user. Use this to ask the study materials based on just the topics provided.
        #                                             Example input: "transformers and vision transformers.""",
        #                             ),
        #                         )
        #     self.tools.append(query_engine_tool)
        #     print("Master has learnt the study materials.")
            
        # except Exception as e:
        #     print(e)
        #     return f"Error: {e}"
        
        
    
    def generate_mcq(self, json_str):
        
        print("Tools : ", self.tools)
        
        parser = PydanticOutputParser(pydantic_object=parseFormat)
        json_parsed_data = parser.parse(json_str)
        formatted_prompt = mcq_template.format(**json_parsed_data.dict())
        
        # print("Formatted prompt :",formatted_prompt)
        
        science_agent = ReActAgent.from_tools(self.tools, llm=self.gemini_llm, verbose=True, context=science_agent_context)
        
        science_agent.query(formatted_prompt)































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