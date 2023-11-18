from flask import Flask
from questions import Questions
import constants
import openai

app = Flask(__name__)
openai.api_key=constants.API_KEY

question_prompt = "Thermal Physics"
questions = Questions()

questions.create_multiple_choice_question(question_prompt)
questions.create_short_answer_question(question_prompt)
questions.create_true_or_false_question(question_prompt)