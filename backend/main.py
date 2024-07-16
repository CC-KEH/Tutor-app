from tutor.components.main_chain import Master
from pydantic import BaseModel
from typing import List, Optional
import uuid
from uuid import UUID, uuid4
import json

import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

class format(BaseModel):
    id: Optional[UUID] = None
    number: Optional[int] = 10
    topics: str
    difficulty: Optional[str] = "easy"
    response_template: Optional[str] = ""
    question_type: str = "mcq"



def store(FOLDER_PATH):
    try:
        master = Master(knowledge_base_path=FOLDER_PATH)
        master.learn(index_name='tutor')
        
        return True,"Stored the file",master
    except:
        return False,"Error in storing the file", None

def run(master,task):

    return master.generate_mcq(task)



if __name__ == "__main__":
    _, _, master = store(FOLDER_PATH="backend/artifacts")
    
    
    with open("backend/src/tutor/templates/quiz_template.json", 'r') as file:
        json_data = json.load(file)


    response_template = json.dumps(json_data, indent=4) 
        
    print(response_template)


    json_file = {
        "id": str(uuid.uuid4()),
        "number": 10,
        "topics": "transformers, vision transformers",
        "difficulty": "easy",
        "response_template": response_template,
        "question_type": "mcq"
    }

    # json_str = json.dumps(json_file)
    task = format(**json_file)
    
    result = run(master,task)
    
    print(result)