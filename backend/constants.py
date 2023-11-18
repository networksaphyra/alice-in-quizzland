API_KEY=open(".env", "r").readline().strip()
MODEL = "gpt-3.5-turbo"

# Mutilple Choice
MULTIPLE_CHOICE_TEMPERATURE = 0.1
MULTIPLE_CHOICE_MAX_TOKENS = 500
MULITPLE_CHOICE_OPTION_NUMBER = 4
MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Please generate a question and multiple-choice options based on the provided topic. 
    Return a JSON Object with following format:
        "Question": "The question"
        "Options": {"Option A", "Option B", "Option C", "Option D"}
        "Answer": Correct option for the question"
"""

# Short Answers
SHORT_ANSWER_TEMPERATURE = 0.5
SHORT_ANSWER_MAX_TOKENS = 500
SHORT_ANSWER_SYSTEM_BEHAVIOR_PROMPT=f"""
    Please generate a short question and a short answer to that question. 
    Return a JSON Object with following format:
        "Question": "The question"
        "Answer": Short answer to the question"
"""

# True or False
TRUE_OR_FALSE_TEMPERATURE = 0.1
TRUE_OR_FALSE_MAX_TOKENS = 50
TRUE_OR_FALSE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Please generate a true or false question and a True or False answer to that question. 
    Return a JSON Object with following format:
        "Question": "The question"
        "Answer": True or false answer to that question"
"""  