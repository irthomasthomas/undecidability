**Prompt:**
diff --git a/agents/huggingface-and-peft-deep-dive.md b/agents/huggingface-and-peft-deep-dive.md
new file mode 100644
index 0000000..fa4b269
--- /dev/null
+++ b/agents/huggingface-and-peft-deep-dive.md
@@ -0,0 +1,104 @@
+# Mastering Parameter-Efficient Fine-Tuning with The Hugging Face Transformers
+
+In the world of machine learning and natural language processing (NLP), the use of pre-trained models has become ubiquitous. One such example is the Hugging Face Transformers library which provides general-purpose architectures for NLP. BigCode's `bigcode/starcoderbase-7b` and PEFT (Parameter-Efficient Fine-Tuning) models, such as `bigcode/astraios-7b-parallel`, enhance the capabilities of these architectures further through fine-tuning techniques that allow for specialization with a lower computational cost. This article offers a comprehensive walkthrough of setting up a PEFT model using the Hugging Face Transformers library, focusing on the `bigcode/starcoderbase-7b` model and its PEFT variant.
+
+## Introduction to Hugging Face Transformers and PEFT
+
+The Hugging Face Transformers library is a robust and versatile collection of pre-trained models designed for a range of NLP tasks, including text classification, token classification, question-answering, and text generation. These models are built on transformer architectures that have proven effective in understanding and generating human-like text.
+
+PEFT models, such as those by BigCode, go a step further—they take a highly capable pre-trained model and map a smaller, more task-specific model on top of it, allowing for refinements and adaptations to new tasks without the need to train the entire model from scratch. Integrating PEFT into a workflow can dramatically reduce the time and resources needed for training.
+
+## Prerequisites
+
+Before diving into the technical steps, ensure that you have Python and the necessary packages installed. You'll need the `transformers` library, as well as the PEFT-specific module from BigCode:
+
+```bash
+# Install the Hugging Face Transformers library
+pip install -q transformers
+
+# Install the PEFT module from its repository
+pip install -e git+https://github.com/bigcode-project/astraios#subdirectory=peft
+```
+
+These commands install all the necessary components for running PEFT models with the Hugging Face Transformers library.
+
+## Setting Up the Environment
+
+With the prerequisites in place, you can import the necessary classes from both the `transformers` library and the `peft` module:
+
+```python
+from peft import PeftModel 
+from transformers import AutoModelForCausalLM, AutoTokenizer
+```
+
+The `AutoModelForCausalLM` class is a general model for causal language modeling (predicting the next token in a sequence), and `AutoTokenizer` is responsible for tokenizing input text (splitting text into tokens, or meaningful chunks). `PeftModel` is part of the PEFT toolkit and handles the efficient fine-tuning.
+
+## Loading the Pre-Trained Models
+
+Next, you need to specify the pre-trained models and Checkpoints that will be used:
+
+```python
+peft_checkpoint = "bigcode/astraios-7b-parallel"
+checkpoint = "bigcode/starcoderbase-7b"
+```
+
+These identifiers point to specific pre-trained models hosted on the Hugging Face model hub. After setting the checkpoints, load the base model and prepare it for fine-tuning with the `PeftModel`:
+
+```python
+model = AutoModelForCausalLM.from_pretrained(checkpoint)
+model = PeftModel.from_pretrained(model, peft_checkpoint)
+```
+
+These lines initialize the base model with pre-trained weights from `bigcode/starcoderbase-7b` and then prepare it for parameter-efficient fine-tuning using the `bigcode/astraios-7b-parallel` checkpoint, respectively.
+
+## Setting Up the Work Environment
+
+Before generating any text, you'll need to set up the computing device:
+
+```python
+device = "cuda" # for GPU usage or "cpu" for CPU usage
+```
+
+This line ensures that you utilize the GPU for faster computations, if available, otherwise the CPU will be used.
+
+## Preparing for Text Generation
+
+With the model and device set up, it's time to tokenize the input text. Tokenization involves converting raw text into a format understandable by the model—namely, a sequence of token IDs. Load the tokenizer from the same checkpoint as the base model and tokenize the input text:
+
+```python
+tokenizer = AutoTokenizer.from_pretrained(checkpoint)
+inputs = tokenizer.encode("Question: Please write a function in Python that performs bubble sort.
+
+Answer:", return_tensors="pt").to(device)
+```
+
+By using `return_tensors="pt"`, you're asking the tokenizer to format the output as PyTorch tensors, suitable for input into the model which has been sent to the GPU or CPU as defined by `device`.
+
+## Generating Text with the Model
+
+Now, use the tokenized input to generate a sequence of text with the model:
+
+```python
+outputs = model.generate(inputs)
+```
+
+The `model.generate` function takes the tokenized inputs and feeds them into the model, which then produces a sequence of output tokens.
+
+## Decoding the Output
+
+Once you have the output tokens, you'll want to convert them back into readable text. Use the tokenizer's `decode` method to achieve this:
+
+```python
+print(tokenizer.decode(outputs[0]))
+```
+
+The `tokenizer.decode` function converts the sequence of output token IDs back into a string, skipping any special tokens by default. This is what you'll see in the console—a generated response to the prompt.
+
+## Conclusion and Potential
+
+Following this walkthrough, you should have a functional PEFT model capable of generating code from prompts. The `bigcode/starcoderbase-7b` model is tailored for programming language processing, making it an invaluable tool for a variety of code-related tasks. By using PEFT for fine-tuning, you leverage high-performance capabilities while minimizing resource expenditure.
+
+By mastering these tools, you equip yourself with cutting-edge technology to propel your NLP projects forward. Whether you're looking to enhance coding productivity, build advanced code generators, or create intelligent programming assistants, the synergy between Hugging Face Transformers and BigCode's PEFT models offers a powerful platform for innovation.
+
+Start experimenting with different models, prompts, and fine-tuning options to discover the full extent of what these tools can achieve. The journey into the future of AI-assisted coding has just begun. Happy coding! 🚀
+
diff --git a/agents/peft-huggingface-code-explanation-llm-nlp.md b/agents/peft-huggingface-code-explanation-llm-nlp.md
index d68845c..a1756fe 100644
--- a/agents/peft-huggingface-code-explanation-llm-nlp.md
+++ b/agents/peft-huggingface-code-explanation-llm-nlp.md
@@ -67,9 +67,27 @@ print(tokenizer.decode(outputs[0]))
 
 </details>
 
-## Research Synthesis :robot:
 
-The option `return_tensors="pt"` within a tokenization command such as `tokenizer.encode` in the Hugging Face Transformers library is used to specify the format of the output tensors. Setting `return_tensors="pt"` instructs the tokenizer to return the output as PyTorch tensors.
+# Research Synthesis :robot:
+
+assistant: The `tokenizer.decode` function in the Hugging Face Transformers library is used to convert a sequence of token IDs back into a string of text. It essentially performs the reverse operation of `tokenizer.encode`.
+
+When a machine learning model, such as a language model, predicts a sequence of token IDs, we can't immediately read them because they're just numbers. `tokenizer.decode` maps each of these IDs back to its corresponding token in the tokenizer’s vocabulary and then joins these tokens to form a human-readable string.
+
+The function usually includes options to skip special tokens (like padding or start/end of sequence tokens) that are not typically displayed to users. This helps in obtaining a clean text output that can be directly used for presenting results or further processing.
+
+For instance, in your provided command:
+
+```python
+print(tokenizer.decode(outputs[0]))
+```
+
+- `outputs[0]` is expected to be a tensor of token IDs predicted by a model as output.
+- `tokenizer.decode` processes this tensor and converts the sequence of IDs to a string.
+- `print()` then outputs this string so you can read the generated text.
+
+It offers a straightforward method to translate model predictions from numeric form back into human language.
+assistant: The option `return_tensors="pt"` within a tokenization command such as `tokenizer.encode` in the Hugging Face Transformers library is used to specify the format of the output tensors. Setting `return_tensors="pt"` instructs the tokenizer to return the output as PyTorch tensors.
 
 Normally, the `tokenizer.encode` function returns a list of integers, where each integer represents a token ID corresponding to tokens derived from the input text. When integrating with a deep learning framework like PyTorch, you need to convert this list into tensors because PyTorch models require tensor inputs to perform computations.
 
@@ -121,13 +139,13 @@ In essence, this code is used to load a pre-trained causally masked language mod
 
 The checkpoint "bigcode/starcoderbase-7b" indicates that the pre-trained model is a specialized one for encoding programming languages, as explained in the previous conversation. Using such checkpoints allows leveraging vast amounts of previously learned knowledge for related tasks without starting from scratch.
 assistant: It looks like your last message was empty. If you have further questions or need assistance with anything else, feel free to ask!
-assistant: The line `model = PeftModel.from_pretrained(model, peft_checkpoint)` in Python refers to loading a pre-trained model using the `PeftModel` class, which is a part of a Parameter-Efficient Fine-Tuning (PEFT) system.
+assistant: The line `model = PeftModel.from_pretrained(model, peft_checkpoint)` in Python refers to loading a pre-trained model using the `PeftModel` class, which is a part of a Parameter-Efficient Fine-Tuning (PEFT) system, most likely provided by Hugging Face or a similar platform specialized in handling large pre-trained models.
 
-Here is what happens with this line of code:
+Here is what happens with this line o                                                                              f code:
 
 - `PeftModel` is a base class that handles parameter-efficient fine-tuning methods, which allows updating a small subset of a model's parameters rather than the full set, thereby reducing computational costs.
 - `.from_pretrained()` is a method used to initialize a model with weights saved from a previous training session. It is designed to be flexible with model frameworks.
-- The `model` argument within the `from_pretrained` method represents the base model or architecture you want to use.
+- The `model` argument within the `from_pretrained` method typically represents the base model or architecture you want to use.
 - `peft_checkpoint` is a string or path that points to the saved weights and configuration for the PEFT method, enabling it to pick up from where the previous training left off.
 
 This method typically only fine-tunes a small number of additional model parameters (such as adapters) while freezing the majority of the pre-trained model's parameters. This approach helps in saving memory and computing resources while still achieving performance close to a fully fine-tuned model. It is particularly advantageous for adapting large-scale models to specific tasks or datasets without the need for extensive retraining.
@@ -145,9 +163,6 @@ assistant: The Python statement `from peft import PeftModel` suggests the import
 
 The context of the `peft` package is not universally known; yet, based on related searches, it seems that it could be related to a Hugging Face's PEFT (Parameter-Efficient Fine-tuning), which is used for fine-tuning large pre-trained language models efficiently. The `PeftModel` could then represent a type of model adapted for this type of efficient fine-tuning. In PEFT, rather than updating all parameters of a large language model, only a small subset of parameters is adjusted, which reduces computational overhead and makes it feasible to fine-tune these models on less powerful hardware.
 
-However, without any standard documentation or widely recognized usage of `peft` as it stands in the snippet, this interpretation can only be speculative. To provide accurate information, it's essential to have more context or to be able to reference the exact source or documentation where `PeftModel` is defined.
-assistant: The code snippet `# pip install -q transformers` is a command typically run in the terminal, where:
-
 - `pip` is the package installer for Python. It allows you to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
 - `install` is the command used by pip to install packages from the Python Package Index (PyPI) and other indexes.
 - `-q` or `--quiet` is an option that tells pip to give less output. This option can minimize the amount of "progress" text displayed in the terminal and is often used to make logs cleaner. The `-q` flag can be used up to three times to reduce the output to warnings, errors, or critical logging levels only.
@@ -194,26 +209,10 @@ Sources:
     Snippet: Tokenizing Input¶. The primary entry point is a generator:. tokenize. tokenize (readline) ¶ The tokenize() generator requires one argument, readline, which must be a callabl
 </details>
 
-


**Response:**
Add Hugging Face Transformers and PEFT deep dive guide and code explanation

<details><summary>Metadata</summary>

- Duration: 943 ms
- Datetime: 2024-01-11T10:21:13.214903
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

