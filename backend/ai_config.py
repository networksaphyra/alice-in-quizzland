from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("API_KEY")
MODEL = "gpt-3.5-turbo-1106"

# Mutilple Choice
MULTIPLE_CHOICE_TEMPERATURE = 0.1
MULTIPLE_CHOICE_MAX_TOKENS = 4096
MULITPLE_CHOICE_OPTION_NUMBER = 4
MULTIPLE_CHOICE_QUESTION_NUM = 3
MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Generate {MULTIPLE_CHOICE_QUESTION_NUM} question and multiple-choice options based on the provided topic. 
    Return a perfectly working and valid JSON Array with Objects inside it.
    The array and objects should have the following format:
    [
    {{
        "Question": "The question",
        "Options": ["Option A", "Option B", "Option C", "Option D"],
        "Answer": "Correct option for the question",
        "Explanation": "A brief explanation for the answer for this question",
    }},
    ]
"""

# Short Answers
SHORT_ANSWER_TEMPERATURE = 0.5
SHORT_ANSWER_MAX_TOKENS = 4096
SHORT_ANSWER_QUESTION_NUM = 3
SHORT_ANSWER_SYSTEM_BEHAVIOR_PROMPT=f"""
    Generate {SHORT_ANSWER_QUESTION_NUM} short question and a short answer on the provided topic. 
    Return a perfectly working and valid JSON Array with Objects inside it.
    The array and objects should have the following format:
    [
    {{
        "Question": "The question", 
        "Answer": "Short answer to the question",
        "Explanation": "A brief explanation for the answer for this question",
    }},
    ]
"""

# True or False
TRUE_OR_FALSE_TEMPERATURE = 0.1
TRUE_OR_FALSE_MAX_TOKENS = 4096
TRUE_OR_FALSE_QUESTION_NUM = 3
TRUE_OR_FALSE_SYSTEM_BEHAVIOR_PROMPT=f"""
    Generate {TRUE_OR_FALSE_QUESTION_NUM} statements that can only be true or false. Example: Questions: "The Earth is Round", Answer: True. Instead of some generic question such as: Question: "What shape is the earth?"
    Return a perfectly working and valid JSON Array with Objects inside it.
    The array and objects should have the following format:
    [
    {{
        "Question": "The question",
        "Answer": "True or false answer to that question",
        "Explanation": "A brief explanation for the answer for this question",
    }},
    ]
"""

#SHORT_ANSWER_TEMPERATURE = 0.5
CONFIRMATION_TEMPERATURE = 0.2
CONFIRMATION_MAX_TOKENS = 4096
CONFIRMATION_SYSTEM_BEHAVIOR_PROMPT=f"""
    You will be provided with two texts, and you will have to see if the texts remotely relay the same information.
    Return a perfectly working and valid JSON Array with Objects inside it:
    [
    {{
        "Confirmation": "True or False (where True means the answers relay the same information, and false means they do not"),
    }},
    ]
"""

if __name__ == "__main__":
    print(API_KEY)
