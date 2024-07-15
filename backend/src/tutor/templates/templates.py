mcq_agent_context = """Purpose: The primary role of this agent is to assist users to make multiple choice questions along with correct options on the basis of the given study material."""
qna_agent_context = """Purpose: The primary role of this agent is to assist users to make questions and answers based on the given study material."""
numerical_qna_agent_context = """Purpose: The primary role of this agent is to assist users to make numerical questions and solved answers based on the given study material."""
numerical_mcq_agent_context = """Purpose: The primary role of this agent is to assist users to make numerical multiple choice questions along with correct options based on the given study material."""

mcq_template="""
You are an expert {question_type} maker. Fetch and use the study materials given by the user, it is your job to \
create {question_type} of {number} questions for topics {topics} of {difficulty} difficulty. 
Strictly fetch and use only the study materials provided by the user. \
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs.
Make sure correct answers are not always the same option for each question.
### RESPONSE_JSON
{response_template}

"""
