import torch
from transformers import pipeline

class ModelProcessor():
    def __init__(self, max_tokens: int = 128):
        self.model = pipeline("text-generation", model="gpt2", device="cuda")
        self.max_tokens = max_tokens

    def update_max_tokens(self, max_tokens: int):
        self.max_tokens = max_tokens
        
    def run(self, prompt):
        response = self.model(prompt, max_length=self.max_tokens)
        return response[0]["generated_text"]
    
def prompt_generator(questions: str, difficulty: str, category: str, format: str):
    prompt_template = "I need your assistance through an interview. As an interviewer, I have to ask some questions from candidates. Please, customize sample questions based on the followng critera:\n\t\
1) There must be {} questions\n\t\
2) Difficulty level must be {}\n\t\
3) Questions must be on the topic of {}\n\t\
4) Questons format must be {}"

    return prompt_template.format(
            str(questions), 
            difficulty,
            category,
            format
            )

if __name__ == "__main__":
    processor = ModelProcessor(max_tokens=128)
    prompt = prompt_generator(questions=10, difficulty="easy", category="verbal reasoning", format="multiple-choice")
    print(prompt)
    response = processor.run(prompt)
    print(response)