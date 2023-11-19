import openai
import json
import ai_config
import asyncio

def log(statement):
    with open("log.log", "a") as file:
        file.write(statement + "\n")

class QuestionGenerator:
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=ai_config.API_KEY)

    def _extract_multiple_choice_data(self, response):
        filtered_response = response.choices[0].message.content
        log(filtered_response + "\n")
        try: 
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict

    def generate_multiple_choice_question(self, topic_query: str):
        while True:
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
            successful = self._extract_multiple_choice_data(response)
            if successful:
                break
        return successful
        

    def _extract_short_answer_data(self, response):
        filtered_response = response.choices[0].message.content
        log(filtered_response + "\n")

        try: 
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict
     
    def generate_short_answer_question(self, topic_query: str):
        while True:
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
            successful = self._extract_short_answer_data(response)
            if (successful): 
                break
        return successful


    def _extract_true_or_false_data(self, response):
        filtered_response = response.choices[0].message.content
        log(filtered_response + "\n")
        try:
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict
     
    def generate_true_or_false_question(self, topic_query: str):
        while True:
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
            successful = self._extract_multiple_choice_data(response)
            if successful:
                break
        return successful

    def _extract_confirmation_short_answer_data(self, response):
        filtered_response = response.choices[0].message.content
        log(filtered_response + "\n")
        try: 
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict

    def confirmation_short_answer(self, client_data) -> dict:
        answer, client_answer = client_data
        while True:
            messages = [
                {"role": "system", "content": ai_config.CONFIRMATION_SYSTEM_BEHAVIOR_PROMPT},
                {"role": "user", "content": f"text1: {answer}"},
                {"role": "user", "content": f"text2: {client_answer}"}
            ]
            response = self.client.chat.completions.create(
                model = ai_config.MODEL,
                messages = messages,
                temperature = ai_config.CONFIRMATION_TEMPERATURE,
                max_tokens = ai_config.CONFIRMATION_MAX_TOKENS
            )
            successful = self._extract_confirmation_short_answer_data(response)
            if (successful):
                break
        return successful
    

if __name__ == "__main__":
    async def main() -> dict:
        topic = "thermal physics"
        multiple_choice_num = 1
        short_answer_num = 3
        true_or_false_num = 5

        ai_config.MULTIPLE_CHOICE_QUESTION_NUM = multiple_choice_num
        ai_config.SHORT_ANSWER_QUESTION_NUM = short_answer_num
        ai_config.TRUE_OR_FALSE_QUESTION_NUM = true_or_false_num

        question_generator = QuestionGenerator()
        generated_questions = []

        await asyncio.gather(
            generated_questions.append(question_generator.generate_multiple_choice_question(topic)),
            generated_questions.append(question_generator.generate_short_answer_question(topic)),
            generated_questions.append(question_generator.generate_true_or_false_question(topic)),
        )
        print("here")
        print(generated_questions)
    
    asyncio.run(main())
