import openai
import constants

class Questions:
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=constants.API_KEY)

    def filter_multiple_choice_response(self, response):
        filtered_reponse = response.choices[0].message.content
        return filtered_reponse

    def create_multiple_choice_question(self, query: str):
        messages = [
            {"role": "system", "content": constants.MULITPLE_CHOICE_SYSTEM_BEHAVIOR_PROMPT},
            {"role": "user", "content": query}
        ]
        response = self.client.chat.completions.create(
            model = constants.MODEL,
            messages = messages,
            temperature = constants.MULTIPLE_CHOICE_TEMPERATURE,
            max_tokens = constants.MULTIPLE_CHOICE_MAX_TOKENS
        ) 
        print(response)
        return f"Filtered Reponse : {response.choices[0].message}"

    def create_short_answer_question():
        pass