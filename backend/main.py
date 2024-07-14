from tutor.components.main_chain import Master
import json

master = Master(knowledge_base_path="backend/knowledge_store")


master.learn(index_name='tutor')

with open("backend/src/tutor/templates/quiz_template.json", 'r') as file:
    json_data = json.load(file)


response_template = json.dumps(json_data, indent=4) 
    
print(response_template)

json_file = {
            "number": 10,
            "subject": "Maths",
            "difficulty": "easy",
            "response_template": response_template
        }
json_str = json.dumps(json_file)

master.generate_mcq(json_str)