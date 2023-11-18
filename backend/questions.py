import openai
import json
import constants

class Questions:
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=constants.API_KEY)

    def _filter_multiple_choice_response(self, response):
        filtered_response = response.choices[0].message.content
        data_dict = json.loads(filtered_response)
        question = data_dict.get("Question", "")
        options = data_dict.get("Options", [])
        answer = data_dict.get("Answer", "")
        explanation = data_dict.get("Explanation", "")

        filtered_array = [question, options, answer, explanation]
        print(filtered_array, end="\n\n")
        # return filtered_array

    def create_multiple_choice_question(self, topic_query: str):
        messages = [
            {"role": "system", "content": constants.MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = constants.MODEL,
            messages = messages,
            temperature = constants.MULTIPLE_CHOICE_TEMPERATURE,
            max_tokens = constants.MULTIPLE_CHOICE_MAX_TOKENS
        ) 
        return self._filter_multiple_choice_response(response)

    def _filter_short_answer_response(self, response):
        filtered_response = response.choices[0].message.content
        print(filtered_response)
        data_dict = json.loads(filtered_response)
        question = data_dict.get("Question", "")
        answer = data_dict.get("Answer", "")
        explanation = data_dict.get("Explanation", "")

        filtered_array = [question, answer, explanation]
        print(filtered_array, end="\n\n")
        # return filtered_array
     
    def create_short_answer_question(self, topic_query: str):
        messages = [
            {"role": "system", "content": constants.SHORT_ANSWER_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = constants.MODEL,
            messages = messages,
            temperature = constants.SHORT_ANSWER_TEMPERATURE,
            max_tokens = constants.SHORT_ANSWER_MAX_TOKENS
        ) 
        return self._filter_short_answer_response(response)

    def _filter_true_or_false_response(self, response):
        filtered_response = response.choices[0].message.content
        data_dict = json.loads(filtered_response)
        question = data_dict.get("Question", "")
        answer = data_dict.get("Answer", "")
        explanation = data_dict.get("Explanation", "")

        filtered_array = [question, answer, explanation]
        print(filtered_array, end="\n\n")
        # return filtered_array
     
    def create_true_or_false_question(self, topic_query: str):
        messages = [
            {"role": "system", "content": constants.TRUE_OR_FALSE_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = constants.MODEL,
            messages = messages,
            temperature = constants.TRUE_OR_FALSE_TEMPERATURE,
            max_tokens = constants.TRUE_OR_FALSE_MAX_TOKENS
        ) 
        return self._filter_true_or_false_response(response)