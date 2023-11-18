from flask import Flask
from questions import Questions
import constants
import openai

app = Flask(__name__)
openai.api_key=constants.API_KEY

question_prompt = "How Many Days In A Typical Year?"
questions = Questions()

print(questions.create_multiple_choice_question(question_prompt))
print(questions.create_short_answer_question(question_prompt))
print(questions.create_true_or_false_question(question_prompt))