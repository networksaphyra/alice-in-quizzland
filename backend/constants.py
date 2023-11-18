API_KEY=open(".env", "r").readline().strip()

# Requests
MODEL = "gpt-3.5-turbo"
MULTIPLE_CHOICE_TEMPERATURE = 0.1
MULTIPLE_CHOICE_MAX_TOKENS = 500
MULITPLE_CHOICE_OPTION_NUMBER = 4
MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Please generate a question and multiple-choice options based on the provided topic. 
    Return a JSON Object with following format:
        "Question": "The question"\n
        "Options": {"Option A", "Option B", "Option C", "Option D"}\n
        "Answer": Correct Option"
"""
 