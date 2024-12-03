import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline

class ModelProcessor():
    def __init__(self, max_tokenizer: int = 128):
        self.model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
            )
        self.max_tokenizer = max_tokenizer

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            quantization_config=self.bnb_config,
            device_map="auto"
            )
        self.__set_pipeline()

    def update_max_tokenizer(self, max_tokenizer):
        self.max_tokenizer = max_tokenizer
        self.__set_pipeline()
    
    def __set_pipeline(self):
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=self.max_tokenizer
                )
        
    def run(self, prompt):
        return self.pipe(prompt)
        
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
    processor = ModelProcessor(max_tokenizer=128)
    prompt = prompt_generator(questions=10, difficulty="easy", category="verbal reasoning", format="multiple-choice")
    print(prompt)
    response = processor.run(prompt)
    print(response[0]['generated_text'])