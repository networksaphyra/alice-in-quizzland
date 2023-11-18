import openai
import json
import ai_config

class QuestionGenerator:
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=ai_config.API_KEY)

    def _extract_multiple_choice_data(self, response):
        filtered_response = response.choices[0].message.content
        data_dict = json.loads(filtered_response)
        question = data_dict.get("Question", "")
        options = data_dict.get("Options", [])
        answer = data_dict.get("Answer", "")
        explanation = data_dict.get("Explanation", "")

        filtered_array = [question, options, answer, explanation]
        return filtered_array

    def generate_multiple_choice_question(self, topic_query: str):
        messages = [
            {"role": "system", "content": ai_config.MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = ai_config.MODEL,
            messages = messages,
            temperature = ai_config.MULTIPLE_CHOICE_TEMPERATURE,
            max_tokens = ai_config.MULTIPLE_CHOICE_MAX_TOKENS
        ) 
        return self._extract_multiple_choice_data(response)

    def _extract_short_answer_data(self, response):
        filtered_response = response.choices[0].message.content
        data_dict = json.loads(filtered_response)
        question = data_dict.get("Question", "")
        answer = data_dict.get("Answer", "")
        explanation = data_dict.get("Explanation", "")

        filtered_array = [question, answer, explanation]
        return filtered_array
     
    def generate_short_answer_question(self, topic_query: str):
        messages = [
            {"role": "system", "content": ai_config.SHORT_ANSWER_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = ai_config.MODEL,
            messages = messages,
            temperature = ai_config.SHORT_ANSWER_TEMPERATURE,
            max_tokens = ai_config.SHORT_ANSWER_MAX_TOKENS
        ) 
        return self._extract_short_answer_data(response)

    def _extract_true_or_false_data(self, response):
        filtered_response = response.choices[0].message.content
        data_dict = json.loads(filtered_response)
        question = data_dict.get("Question", "")
        answer = data_dict.get("Answer", "")

        filtered_array = [question, answer]
        return filtered_array
     
    def generate_true_or_false_question(self, topic_query: str):
        messages = [
            {"role": "system", "content": ai_config.TRUE_OR_FALSE_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = ai_config.MODEL,
            messages = messages,
            temperature = ai_config.TRUE_OR_FALSE_TEMPERATURE,
            max_tokens = ai_config.TRUE_OR_FALSE_MAX_TOKENS
        ) 
        return self._extract_true_or_false_data(response)