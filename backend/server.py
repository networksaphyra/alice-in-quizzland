from flask import Flask, request
from question_generator import Questions
import ai_config
import openai

app = Flask(__name__)
openai.api_key = ai_config.API_KEY
question_creator = Questions()

@app.route("/members", methods=["GET"])
def get_preferences() -> dict:
    client_data = request.json
    topic = client_data["topic"]
    multiple_choices_num, short_answer_num, true_or_false_num = client_data["multiple_choice_num"], client_data["short_answer_num"], client_data["true_or_false_num"]
    generated_questions = []

    for _ in range(multiple_choices_num):
        generated_questions.append(question_creator.create_multiple_choice_question(topic))
    for _ in range(short_answer_num):
        generated_questions.append(question_creator.create_short_answer_question(topic))
    for _ in range(true_or_false_num):
        generated_questions.append(question_creator.create_true_or_false_question(topic))

    return {'generated_questions': generated_questions}, 200

if __name__ == '__main__':
    app.run(debug=True)
