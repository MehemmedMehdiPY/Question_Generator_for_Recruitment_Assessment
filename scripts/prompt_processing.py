import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

class ModelProcessor():
    def __init__(self, max_tokens: int = 128):
        self.model_path = 'mtgv/MobileLLaMA-1.4B-Chat'

        self.tokenizer = LlamaTokenizer.from_pretrained(self.model_path)
        self.model = LlamaForCausalLM.from_pretrained(
            self.model_path, torch_dtype=torch.float16, device_map='auto',
        )
        self.max_tokens = max_tokens

    def update_max_tokens(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.__set_pipeline()
        
    def run(self, prompt):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        input_ids = input_ids.to('cuda')
        generation_output = self.model.generate(
            input_ids=input_ids, max_new_tokens=self.max_tokens
            )
        response = self.tokenizer.decode(generation_output[0])
        return response
    
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