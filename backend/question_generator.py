import openai
import json
import ai_config

class QuestionGenerator:
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=ai_config.API_KEY)

    def _extract_multiple_choice_data(self, response):
        filtered_response = response.choices[0].message.content
        data_dict = json.loads(filtered_response)

        return data_dict

    def generate_multiple_choice_question(self, topic_query: str, num):
        messages = [
            {"role": "system", "content": f"""
    Generate {num} question and multiple-choice options based on the provided topic. 
    Return a perfectly working and valid JSON Array with Objects inside it.
    The array and objects have the following format:
    [
    {{
        "Question": "The question",
        "Options": {"Option A", "Option B", "Option C", "Option D"},
        "Answer": "Correct option for the question",
        "Explanation": "A brief explanation for the answer for this question",
    }},
    ... repeat with {num} different questions
    ]
"""},
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

        return data_dict
     
    def generate_short_answer_question(self, topic_query: str, num):
        messages = [
            {"role": "system", "content": f"""
    Generate {num} short question and a short answer on the provided topic. 
    Return a perfectly working and valid JSON Array with Objects inside it.
    The array and objects have the following format:
    [
    {{
        "Question": "The question"
        "Answer": "Short answer to the question"
        "Explanation": "A brief explanation for the answer for this question"
        }},
    ... repeat with {num} different questions
    ]
"""},
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

        return data_dict
     
    def generate_true_or_false_question(self, topic_query: str, num):
        messages = [
            {"role": "system", "content": f"""
    Generate {num} statements that can only be true or false. Example: Questions: "The Earth is Round", Answer: True. Instead of some generic question such as: Question: "What shape is the earth?"
    Return a perfectly working and valid JSON Array with Objects inside it.
    The array and objects have the following format:
    [
    {{
        "Question": "The question"
        "Answer": "True or false answer to that question"
    }},
    ... repeat with {num} different questions
    ]
"""},
            {"role": "user", "content": topic_query}
        ]
        response = self.client.chat.completions.create(
            model = ai_config.MODEL,
            messages = messages,
            temperature = ai_config.TRUE_OR_FALSE_TEMPERATURE,
            max_tokens = ai_config.TRUE_OR_FALSE_MAX_TOKENS
        ) 
        return self._extract_true_or_false_data(response)
    
if __name__ == "__main__":
    generator = QuestionGenerator()

    # Test generate_multiple_choice_question
    topic_query = "The Roman Empire"
    generated_multiple_choice = generator.generate_multiple_choice_question(topic_query)
    # print("Generated Multiple Choice Question:")
    # print(generated_multiple_choice, end="\n\n")

    # # Test generate_short_answer_question
    # generated_short_answer = generator.generate_short_answer_question(topic_query)
    # print("Generated Short Answer Question:")
    # print(generated_short_answer, end="\n\n")

    # Test generate_true_or_false_question
    generated_true_or_false = generator.generate_true_or_false_question(topic_query)
    print("Generated True or False Question:")
    print(generated_true_or_false, end="\n\n")
 