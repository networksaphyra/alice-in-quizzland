import openai
import json
import ai_config
import threading

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

    def generate_multiple_choice_question(self, topic_query: str, generated_questions):
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
            generated_questions.append(successful)
        

    def _extract_short_answer_data(self, response):
        filtered_response = response.choices[0].message.content
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
    topic = "Albert Einstein"
    generated_questions = []
    question_generator = QuestionGenerator()
    
    generated_questions = []
    t1 = threading.Thread(target=question_generator.generate_multiple_choice_question, args=(topic, generated_questions))
    t2 = threading.Thread(target=question_generator.generate_short_answer_question, args=(topic, generated_questions))
    t3 = threading.Thread(target=question_generator.generate_true_or_false_question, args=(topic, generated_questions))

    t1.start()
    t2.start()
    t3.start()
    
    # t1.join()
    # t2.join()
    # t3.join()