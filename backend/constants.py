API_KEY=open(".env", "r").readline().strip()
MODEL = "gpt-3.5-turbo"

# Mutilple Choice
MULTIPLE_CHOICE_TEMPERATURE = 0.1
MULTIPLE_CHOICE_MAX_TOKENS = 500
MULITPLE_CHOICE_OPTION_NUMBER = 4
MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Generate a question and multiple-choice options based on the provided topic. 
    Return a perfectly working and valid JSON Object in the following format:
        "Question": "The question"
        "Options": {"Option A", "Option B", "Option C", "Option D"}
        "Answer": "Correct option for the question"
        "Explanation": "A brief explanation for the answer for this question"
"""

# Short Answers
SHORT_ANSWER_TEMPERATURE = 0.5
SHORT_ANSWER_MAX_TOKENS = 500
SHORT_ANSWER_SYSTEM_BEHAVIOR_PROMPT=f"""
    Generate a short question and a short answer on the provided topic. 
    Return a perfectly working and valid JSON Object in the following format:
        "Question": "The question"
        "Answer": "Short answer to the question"
        "Explanation": "A brief explanation for the answer for this question"
"""

# True or False
TRUE_OR_FALSE_TEMPERATURE = 0.1
TRUE_OR_FALSE_MAX_TOKENS = 50
TRUE_OR_FALSE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Generate a statement that can only be true or false. Example: Questions: "The Earth is Round", Answer: True. Instead of some generic question such as: Question: "What shape is the earth?"
    Return a perfectly working and valid JSON Object in the following format:
        "Question": "The question"
        "Answer": "True or false answer to that question"
        "Explanation": "A brief explanation for the answer for this question"
"""