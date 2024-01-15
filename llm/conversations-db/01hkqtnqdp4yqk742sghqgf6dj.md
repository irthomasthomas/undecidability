**Prompt:**
generate a title from this url:https://huggingface.co/bigcode/tiny_starcoder_py:quote:TinyStarCoderPy

This is a 164M parameters model with the same architecture as StarCoder (8k context length, MQA & FIM). It was trained on the Python data from StarCoderData for ~6 epochs which amounts to 100B tokens.


Use


Intended use

The model was trained on GitHub code, to assist with some tasks like Assisted Generation. For pure code completion, we advise using our 15B models StarCoder or StarCoderBase.


Generation

# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/tiny_starcoder_py"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))


Fill-in-the-middle

Fill-in-the-middle uses special tokens to identify the prefix/middle/suffix part of the input and output:

input_text = "<fim_prefix>def print_one_two_three():\n    print('one')\n    <fim_suffix>\n    print('three')<fim_middle>"
inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))


Training


Model

Architecture: GPT-2 model with multi-query attention and Fill-in-the-Middle objective
Pretraining steps: 50k
Pretraining tokens: 100 billion
Precision: bfloat16

Hardware

GPUs: 32 Tesla A100
Training time: 18 hours

Software

Orchestration: Megatron-LM
Neural networks: PyTorch
BP16 if applicable: apex

License

The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement here.

**Response:**
"TinyStarCoderPy: A 164M Parameters Model for Assisted Code Generation and Completion"

<details><summary>Metadata</summary>

- Duration: 834 ms
- Datetime: 2024-01-09T19:20:00.883872
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

