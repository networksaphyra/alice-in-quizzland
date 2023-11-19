import openai
import json
import ai_config

def log(statement):
    with open("log.log", "a") as file:
        file.write(statement + "\n")

class QuestionGenerator:
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=ai_config.API_KEY)

    def _extract_multiple_choice_data(self, response):
        filtered_response = response.choices[0].message.content
        log("Multiple Choice:")
        log(filtered_response + "\n")
        try: 
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict

    def generate_multiple_choice_question(self, topic_query: str, generated_questions):
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
        generated_questions.append(self._extract_multiple_choice_data(response))

    def _extract_short_answer_data(self, response):
        filtered_response = response.choices[0].message.content
        log("Short Answer")
        log(filtered_response + "\n")

        try: 
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict
     
    def generate_short_answer_question(self, topic_query: str, generated_questions):
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
        generated_questions.append(successful)


    def _extract_true_or_false_data(self, response):
        filtered_response = response.choices[0].message.content
        log("True or False")
        log(filtered_response + "\n")
        try:
            data_dict = json.loads(filtered_response)
        except json.JSONDecodeError:
            print("Error Handled...")
            return None
        return data_dict
     
    def generate_true_or_false_question(self, topic_query: str, generated_questions):
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
        generated_questions.append(successful)
    
if __name__ == "__main__":
    generator = QuestionGenerator()

    # Test generate_multiple_choice_question
    topic_query = "The Roman Empire"
    generated_multiple_choice = generator.generate_multiple_choice_question(topic_query)
    print("Generated Multiple Choice Question:")
    print(generated_multiple_choice, end="\n\n")

    # Test generate_short_answer_question
    generated_short_answer = generator.generate_short_answer_question(topic_query)
    print("Generated Short Answer Question:")
    print(generated_short_answer, end="\n\n")

    # Test generate_true_or_false_question
    generated_true_or_false = generator.generate_true_or_false_question(topic_query)
    print("Generated True or False Question:")
    print(generated_true_or_false, end="\n\n")
