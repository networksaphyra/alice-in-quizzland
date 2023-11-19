from flask import Flask, request
from question_generator import QuestionGenerator
import ai_config
import openai

app = Flask(__name__)
openai.api_key = ai_config.API_KEY
question_creator = QuestionGenerator()

@app.route("/members", methods=["POST"])
def get_preferences() -> dict:
    client_data = request.json
    topic = client_data["topic"]
    multiple_choices_num, short_answer_num, true_or_false_num = client_data["multipleChoice"], client_data["shortAnswer"], client_data["trueOrFalse"]
    ai_config.MULTIPLE_CHOICE_QUESTION_NUM, ai_config.SHORT_ANSWER_QUESTION_NUM, ai_config.TRUE_OR_FALSE_QUESTION_NUM = multiple_choices_num, short_answer_num, true_or_false_num
    print(multiple_choices_num, short_answer_num, true_or_false_num)
    generated_questions = []

    generated_questions.append(question_creator.generate_multiple_choice_question(topic))
    print('here')
    generated_questions.append(question_creator.generate_short_answer_question(topic))
    print('here')
    generated_questions.append(question_creator.generate_true_or_false_question(topic))
    print('here')
    return {'generated_questions': generated_questions}, 200



if __name__ == '__main__':
   app.run(debug=True)
