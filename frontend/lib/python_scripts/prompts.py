instructions = "You are required to generate a quiz based on the following parameters: "

quiz_prompt = """
Topic: {topic}
Difficulty: {difficulty}
Question Count: {question_count}
"""

response_format = """
QuestionNo: {question_no}
Question: {question}
Option1: {option1}
Option2: {option2}
Option3: {option3}
Option4: {option4}

CorrectOption: {correct_option}
"""

prompt_template = {}