from flask import Flask
from questions import Questions
import pprint
import constants
import openai

app = Flask(__name__)
openai.api_key=constants.API_KEY

question_prompt = "How Many Days In A Typical Year?"
questions = Questions()

pprint.pprint(questions.create_multiple_choice_question(query=question_prompt))