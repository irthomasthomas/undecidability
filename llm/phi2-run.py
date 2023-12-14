# from huggingface_hub import snapshot_download
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

def generate(prompt: str, tokenizer, model, generation_params: dict = {"max_length":200})-> str : 
    print("Generating...")
    
    # Start timing for prompt processing
    prompt_time_begin = time.time()
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    prompt_time_end = time.time()
    total_prompt_tokens = len(prompt)  # Assuming 1 token per character, adjust as needed
    print(f"Prompts: {total_prompt_tokens} tokens, {total_prompt_tokens / (prompt_time_end - prompt_time_begin):.2f} tokens/second")
    
    # Start timing for token generation
    token_time_begin = time.time()
    outputs = model.generate(**inputs, **generation_params)
    token_time_end = time.time()
    total_gen_tokens = len(tokenizer.batch_decode(outputs)[0])  # Assuming 1 token per character, adjust as needed
    print(f"Tokens: {total_gen_tokens} tokens, {total_gen_tokens / (token_time_end - token_time_begin):.2f} tokens/second")
    
    completion = tokenizer.batch_decode(outputs)[0]
    return completion


# model_path = "/home/thomas/Development/Projects/llm/phi2/MS-f16-phi-2/phi-2"
model_path = "/home/thomas/Development/Projects/llm/phi2/phi-2"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)

torch.set_default_dtype(torch.float16)
print("Testing models in float16...")
print("---------------------------------------------------------------------------------")
result = generate("There's always a brighter future if", tokenizer, model)  # Assuming generate function takes tokenizer and model as arguments
print(result)
print("---------------------------------------------------------------------------------")
