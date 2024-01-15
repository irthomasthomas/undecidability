**Prompt:**
diff --git a/agents/peft-huggingface-code-explanation-llm-nlp.md b/agents/peft-huggingface-code-explanation-llm-nlp.md
new file mode 100644
index 0000000..d68845c
--- /dev/null
+++ b/agents/peft-huggingface-code-explanation-llm-nlp.md
@@ -0,0 +1,306 @@
+### GPT-4 explains new concepts from llm source-code using advanced search research assistant. Built on top of openai assistants and a bing custom search api.
+
+Have you ever wondered how to run thos little adapter models? Or wordered what those lines of python on every huggingface repo actually do?
+Read on to find out! 
+
+```python
+# huggingface script to run peft model
+# pip install -q transformers
+# pip install -e git+https://github.com/bigcode-project/astraios#subdirectory=peft
+from peft import PeftModel 
+from transformers import AutoModelForCausalLM, AutoTokenizer
+
+peft_checkpoint = "bigcode/astraios-7b-parallel"
+checkpoint = "bigcode/starcoderbase-7b"
+model = AutoModelForCausalLM.from_pretrained(checkpoint)
+model = PeftModel.from_pretrained(model, peft_checkpoint)
+device = "cuda" # for GPU usage or "cpu" for CPU usage
+
+tokenizer = AutoTokenizer.from_pretrained(checkpoint)
+model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
+
+inputs = tokenizer.encode("Question: Please write a function in Python that performs bubble sort.
+
+Answer:", return_tensors="pt").to(device)
+outputs = model.generate(inputs)
+print(tokenizer.decode(outputs[0]))
+```
+    
+<details>
+    <summary><b>Click to view search results...</b></summary>
+
+    Title: Tokenizer.Decode Method (Microsoft.ML.Tokenizers)
+    URL: https://learn.microsoft.com/en-us/dotnet/api/microsoft.ml.tokenizers.tokenizer.decode?view=ml-dotnet-preview
+    Snippet: public string? Decode (System.Collections.Generic.IEnumerable<int> ids, bool skipSpecialTokens = false); member this.Decode : seq<int> * bool -> string Public Function Decode (ids As IEnumerable(Of Integer), Optional skipSpecialTokens As Boolean = false) As String Parameters
+
+    Title: Tokenizer - Hugging Face
+    URL: https://huggingface.co/docs/transformers/main_classes/tokenizer
+    Snippet: A tokenizer is in charge of preparing the inputs for a model. The library contains tokenizers for all the models. Most of the tokenizers are available in two flavors: a full python implementation and a “Fast” implementation based on the Rust library 🤗 Tokenizers. The “Fast” implementations allows:
+
+    Title: pytorch - Tokens to Words mapping in the tokenizer decode step ...
+    URL: https://stackoverflow.com/questions/62317723/tokens-to-words-mapping-in-the-tokenizer-decode-step-huggingface
+    Snippet: To get exactly your desired output, you have to work with a list comprehension: #start index because the number of special tokens is fixed for each model (but be aware of single sentence input and pairwise sentence input) idx = 1 enc = [tokenizer.encode (x, add_special_tokens=False, add_prefix_space=True) for x in example.split ()] desired ...
+
+    Title: The tokenization pipeline - Hugging Face
+    URL: https://huggingface.co/docs/tokenizers/pipeline
+    Snippet: The tokenization pipeline When calling Tokenizer.encode or Tokenizer.encode_batch, the input text(s) go through the following pipeline:. normalization; pre-tokenization; model; post-processing; We’ll see in details what happens during each of those steps in detail, as well as when you want to decode <decoding> some token ids, and how the 🤗 Tokenizers library allows you to customize each ...
+
+    Title: Tokenizers - Hugging Face NLP Course
+    URL: https://huggingface.co/learn/nlp-course/chapter2/4?fw=tf
+    Snippet: The first type of tokenizer that comes to mind ... For example, we could use whitespace to tokenize the text into words by applying Python’s split() function: Copied. tokenized_text = "Jim Henson was a puppeteer ... we want to get a string. This can be done with the decode() method as follows: Copied. decoded_string = tokenizer.decode([7993 ...
+
+    Title: Hugging Face: Understanding tokenizers | by Awaldeep Singh - Medium
+    URL: https://medium.com/@awaldeep/hugging-face-understanding-tokenizers-1b7e4afdb154
+    Snippet: The main tool for processing textual data is a tokenizer. A tokenizer starts by splitting text into tokens according to a set of rules. The tokens are converted into numbers, which are used to ...
+
+    Title: Tokenizer Class (Microsoft.ML.Tokenizers) | Microsoft Learn
+    URL: https://learn.microsoft.com/en-us/dotnet/api/microsoft.ml.tokenizers.tokenizer?view=ml-dotnet-preview
+    Snippet: Decode(IEnumerable<Int32>, Boolean) Decode the given ids, back to a String. Decode(Int32, Boolean) Decodes the Id to the mapped token. Encode(String) Encodes input text to object has the tokens list, tokens Ids, tokens offset mapping. TrainFromFiles(Trainer, ReportProgress, String[]) Train the tokenizer model using input files.
+
+    Title: Utilities for Tokenizers - Hugging Face
+    URL: https://huggingface.co/docs/transformers/internal/tokenization_utils?highlight=batch_decode
+    Snippet: Padding side (left/right) padding token ids are defined at the tokenizer level (with self.padding_side, self.pad_token_id and self.pad_token_type_id). Please note that with a fast tokenizer, using the __call__ method is faster than using a method to encode the text followed by a call to the pad method to get a padded encoding.
+
+    Title: tokenize — Tokenizer for Python source — Python 3.12.1 documentation
+    URL: https://docs.python.org/3/library/tokenize.html
+    Snippet: Tokenizing Input¶. The primary entry point is a generator:. tokenize. tokenize (readline) ¶ The tokenize() generator requires one argument, readline, which must be a callable object which provides the same interface as the io.IOBase.readline() method of file objects. Each call to the function should return one line of input as bytes. The generator produces 5-tuples with these members: the ...
+
+</details>
+
+## Research Synthesis :robot:
+
+The option `return_tensors="pt"` within a tokenization command such as `tokenizer.encode` in the Hugging Face Transformers library is used to specify the format of the output tensors. Setting `return_tensors="pt"` instructs the tokenizer to return the output as PyTorch tensors.
+
+Normally, the `tokenizer.encode` function returns a list of integers, where each integer represents a token ID corresponding to tokens derived from the input text. When integrating with a deep learning framework like PyTorch, you need to convert this list into tensors because PyTorch models require tensor inputs to perform computations.
+
+The `return_tensors` argument specifies the type of tensors you want to return:
+
+- `"pt"` for PyTorch tensors, returned as `torch.Tensor` objects.
+- `"tf"` for TensorFlow tensors, returned as `tf.constant` objects.
+- `"np"` for NumPy arrays, returned as `np.ndarray` objects.
+
+So, in the context of the provided code snippet:
+
+```python
+inputs = tokenizer.encode("Question: Please write a function in Python that performs bubble sort.", return_tensors="pt").to(device)
+```
+
+The tokenizer will encode the input text into a sequence of tokens, then into a sequence of IDs, and finally, it will convert these IDs into a PyTorch tensor. The `.to(device)` call at the end indicates that this tensor will be moved to a specified device, such as a CPU or GPU, making it ready for input into a PyTorch model for computation.
+assistant: The `tokenizer.encode` method is a function provided by tokenization libraries, such as those offered by Hugging Face, that converts a string of text into a sequence of integers. These integers correspond to token IDs from a pre-defined vocabulary that the tokenizer has been trained on. Here is a step-by-step explanation of what the method does:
+
+1. **Tokenizing**: It first splits the input text into tokens. These could be words, subwords, or characters depending on the tokenizer used. For instance, a BERT tokenizer may split unknown words into known subwords.
+
+2. **Converting to IDs**: Each token is then converted to its corresponding integer ID from the tokenizer's vocabulary. This is necessary because machine learning models do not understand text; they work with numbers.
+
+3. **Adding Special Tokens**: Many pre-trained models require specific tokens to represent the start and end of a sentence. The `encode` method usually appends these automatically (for example, `[CLS]` at the start and `[SEP]` at the end for BERT models).
+
+4. **Creating Attention Mask**: While not directly output by the `encode` method (but by `encode_plus` and other similar methods), the process also involves creating attention masks to tell the model which tokens should be paid attention to and which should not (such as padding tokens).
+
+So, when the `tokenizer.encode` function is used as shown in the input:
+
+```python
+inputs = tokenizer.encode("Question: Please write a function in Python that performs bubble sort."
+```
+
+It will do the following:
+
+- Convert the given text into tokens that are suitable for the model associated with the tokenizer.
+- Convert each token into its corresponding ID to create a list of token IDs that the model can process.
+- Automatically handle the inclusion of any special tokens needed by the model.
+
+This list of token IDs ('inputs') can then be passed to a machine learning model for tasks such as text classification, question-answering, or text generation.
+assistant: The Python statement `model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)` involves a few different components from the Hugging Face `transformers` library:
+
+- `AutoModelForCausalLM`: This is a class from the Transformers library that instantiates a model with a language modeling head suited for causal language modeling tasks. Causal language modeling predicts the next token in a sequence (i.e., autoregressive modeling), which is useful for tasks like text generation.
+
+- `.from_pretrained(checkpoint)`: This method is used to load a pre-trained model specified by the `checkpoint`. The `checkpoint` variable typically holds the path to the model’s weights or the identifier of a pre-trained model hosted on the Hugging Face model hub (like "gpt-2" or "distilgpt2"). The method initializes the model with the weights stored at the given checkpoint.
+
+- `.to(device)`: After loading the pre-trained model, `.to(device)` transfers the model's weights to a specified computing device. The `device` could be a CPU or GPU (if available). This allows one to perform computations on the appropriate hardware accelerator.
+
+In essence, this code is used to load a pre-trained causally masked language model and prepare it for use (inference or further training) on the specified hardware device. It encapsulates the model’s architecture, weights, and configuration, providing an easy and efficient way to perform language modeling tasks and generate text.
+
+The checkpoint "bigcode/starcoderbase-7b" indicates that the pre-trained model is a specialized one for encoding programming languages, as explained in the previous conversation. Using such checkpoints allows leveraging vast amounts of previously learned knowledge for related tasks without starting from scratch.
+assistant: It looks like your last message was empty. If you have further questions or need assistance with anything else, feel free to ask!
+assistant: The line `model = PeftModel.from_pretrained(model, peft_checkpoint)` in Python refers to loading a pre-trained model using the `PeftModel` class, which is a part of a Parameter-Efficient Fine-Tuning (PEFT) system.
+
+Here is what happens with this line of code:
+
+- `PeftModel` is a base class that handles parameter-efficient fine-tuning methods, which allows updating a small subset of a model's parameters rather than the full set, thereby reducing computational costs.
+- `.from_pretrained()` is a method used to initialize a model with weights saved from a previous training session. It is designed to be flexible with model frameworks.
+- The `model` argument within the `from_pretrained` method represents the base model or architecture you want to use.
+- `peft_checkpoint` is a string or path that points to the saved weights and configuration for the PEFT method, enabling it to pick up from where the previous training left off.
+
+This method typically only fine-tunes a small number of additional model parameters (such as adapters) while freezing the majority of the pre-trained model's parameters. This approach helps in saving memory and computing resources while still achieving performance close to a fully fine-tuned model. It is particularly advantageous for adapting large-scale models to specific tasks or datasets without the need for extensive retraining.
+assistant: The identifier "bigcode/starcoderbase-7b" refers to a model known as StarCoderBase-7B hosted on the Hugging Face model hub. This model has the following characteristics:
+
+- It has 7 billion parameters.
+- It was trained on a dataset consisting of over 80 programming languages from "The Stack" (version 1.2), with all opt-out requests honored and thus excluded from the training data.
+- It employs Multi Query Attention and has a context window of 819


**Response:**
Added code explanation for running the PEFT model and using the Hugging Face tokenizer.

<details><summary>Metadata</summary>

- Duration: 1608 ms
- Datetime: 2024-01-10T20:55:42.477092
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

