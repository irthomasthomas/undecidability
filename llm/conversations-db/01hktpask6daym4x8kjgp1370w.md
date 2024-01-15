**Prompt:**
Make this content into a pretty gh markdown note:quote:- [ ] [Assisted Generation: a new direction toward low-latency text generation](https://huggingface.co/blog/assisted-generation)

Greedy decoding with assisted generation

Assisted generation is a balancing act. You want the assistant to quickly generate a candidate sequence while being as accurate as possible. If the assistant has poor quality, your get the cost of using the assistant model with little to no benefits. On the other hand, optimizing the quality of the candidate sequences may imply the use of slow assistants, resulting in a net slowdown. While we can't automate the selection of the assistant model for you, we’ve included an additional requirement and a heuristic to ensure the time spent with the assistant stays in check.

First, the requirement – the assistant must have the exact same tokenizer as your model. If this requirement was not in place, expensive token decoding and re-encoding steps would have to be added. Furthermore, these additional steps would have to happen on the CPU, which in turn may need slow inter-device data transfers. Fast usage of the assistant is critical for the benefits of assisted generation to show up.

Finally, the heuristic. By this point, you have probably noticed the similarities between the movie Inception and assisted generation – you are, after all, running text generation inside text generation. There will be one assistant model forward pass per candidate token, and we know that forward passes are expensive. While you can’t know in advance the number of tokens that the assistant model will get right, you can keep track of this information and use it to limit the number of candidate tokens requested to the assistant – some sections of the output are easier to anticipate than others.

Wrapping all up, here’s our original implementation of the assisted generation loop (code):

Use greedy decoding to generate a certain number of candidate tokens with the assistant model, producing candidates. The number of produced candidate tokens is initialized to 5 the first time assisted generation is called.
Using our model, do a forward pass with candidates, obtaining logits.
Use the token selection method (.argmax() for greedy search or .multinomial() for sampling) to get the next_tokens from logits.
Compare next_tokens to candidates and get the number of matching tokens. Remember that this comparison has to be done with left-to-right causality: after the first mismatch, all candidates are invalidated.
Use the number of matches to slice things up and discard variables related to unconfirmed candidate tokens. In essence, in next_tokens, keep the matching tokens plus the first divergent token (which our model generates from a valid candidate subsequence).
Adjust the number of candidate tokens to be produced in the next iteration — our original heuristic increases it by 2 if ALL tokens match and decreases it by 1 otherwise.

We’ve designed the API in 🤗 Transformers such that this process is hassle-free for you. All you need to do is to pass the assistant model under the new assistant_model keyword argument and reap the latency gains! At the time of the release of this blog post, assisted generation is limited to a batch size of 1.

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

prompt = "Alice and Bob"
checkpoint = "EleutherAI/pythia-1.4b-deduped"
assistant_checkpoint = "EleutherAI/pythia-160m-deduped"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
inputs = tokenizer(prompt, return_tensors="pt").to(device)

model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
assistant_model = AutoModelForCausalLM.from_pretrained(assistant_checkpoint).to(device)
outputs = model.generate(**inputs, assistant_model=assistant_model)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))
# ['Alice and Bob are sitting in a bar. Alice is drinking a beer and Bob is drinking a']

Is the additional internal complexity worth it? Let’s have a look at the latency numbers for the greedy decoding case (results for sampling are in the next section), considering a batch size of 1. These results were pulled directly out of 🤗 Transformers without any additional optimizations, so you should be able to reproduce them in your setup.

Assisted Generation Benchmark
OPT: Open
OPT: Summ
Whisper: ARS
CodeGen: Code
Flan-T5: Summ
Benchmark Info
GPU

Omit cases with memory offload?
Yes
No
Image

Assistant Model

facebook/opt-125m
Model Names:

1.3B: facebook/opt-1.3b
6.7B: facebook/opt-6.7b
30B: facebook/opt-30b
66B: facebook/opt-66b
Dataset used as input prompt:

C4 (en, validation set)
joaogante/assisted_generation_benchmarks
built with Gradio.
Hosted on   Spaces

Glancing at the collected numbers, we see that assisted generation can deliver significant latency reductions in diverse settings, but it is not a silver bullet – you should benchmark it before applying it to your use case. We can conclude that assisted generation:

🤏 Requires access to an assistant model that is at least an order of magnitude smaller than your model (the bigger the difference, the better);
🚀 Gets up to 3x speedups in the presence of INT8 and up to 2x otherwise, when the model fits in the GPU memory;
🤯 If you’re playing with models that do not fit in your GPU and are relying on memory offloading, you can see up to 10x speedups;
📄 Shines in input-grounded tasks, like automatic speech recognition or summarization.

Sample with assisted generation

Greedy decoding is suited for input-grounded tasks (automatic speech recognition, translation, summarization, ...) or factual knowledge-seeking. Open-ended tasks requiring large levels of creativity, such as most uses of a language model as a chatbot, should use sampling instead. Assisted generation is naturally designed for greedy decoding, but that doesn’t mean that you can’t use assisted generation with multinomial sampling!

Drawing samples from a probability distribution for the next token will cause our greedy assistant to fail more often, reducing its latency benefits. However, we can control how sharp the probability distribution for the next tokens is, using the temperature coefficient that’s present in most sampling-based applications. At one extreme, with temperatures close to 0, sampling will approximate greedy decoding, favoring the most likely token. At the other extreme, with the temperature set to values much larger than 1, sampling will be chaotic, drawing from a uniform distribution. Low temperatures are, therefore, more favorable to your assistant model, retaining most of the latency benefits from assisted generation, as we can see below.

#### Suggested labels
#### {   "key": "assisted-generation",   "value": "Text generation with the use of an assistant model for latency reduction" }

**Response:**
> **Assisted Generation: a new direction toward low-latency text generation**

Greedy decoding with assisted generation

Assisted generation is a balancing act. You want the assistant to quickly generate a candidate sequence while being as accurate as possible. If the assistant has poor quality, your get the cost of using the assistant model with little to no benefits. On the other hand, optimizing the quality of the candidate sequences may imply the use of slow assistants, resulting in a net slowdown. While we can't automate the selection of the assistant model for you, we’ve included an additional requirement and a heuristic to ensure the time spent with the assistant stays in check.

First, the requirement – the assistant must have the exact same tokenizer as your model. If this requirement was not in place, expensive token decoding and re-encoding steps would have to be added. Furthermore, these additional steps would have to happen on the CPU, which in turn may need slow inter-device data transfers. Fast usage of the assistant is critical for the benefits of assisted generation to show up.

Finally, the heuristic. By this point, you have probably noticed the similarities between the movie Inception and assisted generation – you are, after all, running text generation inside text generation. There will be one assistant model forward pass per candidate token, and we know that forward passes are expensive. While you can’t know in advance the number of tokens that the assistant model will get right, you can keep track of this information and use it to limit the number of candidate tokens requested to the assistant – some sections of the output are easier to anticipate than others.

Wrapping all up, here’s our original implementation of the assisted generation loop (code):

1. Use greedy decoding to generate a certain number of candidate tokens with the assistant model, producing candidates. The number of produced candidate tokens is initialized to 5 the first time assisted generation is called.
2. Using our model, do a forward pass with candidates, obtaining logits.
3. Use the token selection method (.argmax() for greedy search or .multinomial() for sampling) to get the next_tokens from logits.
4. Compare next_tokens to candidates and get the number of matching tokens. Remember that this comparison has to be done with left-to-right causality: after the first mismatch, all candidates are invalidated.
5. Use the number of matches to slice things up and discard variables related to unconfirmed candidate tokens. In essence, in next_tokens, keep the matching tokens plus the first divergent token (which our model generates from a valid candidate subsequence).
6. Adjust the number of candidate tokens to be produced in the next iteration — our original heuristic increases it by 2 if ALL tokens match and decreases it by 1 otherwise.

We’ve designed the API in 🤗 Transformers such that this process is hassle-free for you. All you need to do is to pass the assistant model under the new `assistant_model` keyword argument and reap the latency gains! At the time of the release of this blog post, assisted generation is limited to a batch size of 1.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

prompt = "Alice and Bob"
checkpoint = "EleutherAI/pythia-1.4b-deduped"
assistant_checkpoint = "EleutherAI/pythia-160m-deduped"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
inputs = tokenizer(prompt, return_tensors="pt").to(device)

model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
assistant_model = AutoModelForCausalLM.from_pretrained(assistant_checkpoint).to(device)
outputs = model.generate(**inputs, assistant_model=assistant_model)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))
# ['Alice and Bob are sitting in a bar. Alice is drinking a beer and Bob is drinking a']
```

Is the additional internal complexity worth it? Let’s have a look at the latency numbers for the greedy decoding case (results for sampling are in the next section), considering a batch size of 1. These results were pulled directly out of 🤗 Transformers without any additional optimizations, so you should be able to reproduce them in your setup.

**Assisted Generation Benchmark**
| OPT: Open | OPT: Summ | Whisper: ARS | CodeGen: Code | Flan-T5: Summ |
|------------|------------|---------------|----------------|----------------|
| GPU        |            |               |                |                |
| Omit cases with memory offload? | Yes | No | Image |
| Assistant Model | facebook/opt-125m | Model Names: | 1.3B: facebook/opt-1.3b | 6.7B: facebook/opt-6.7b |
| 30B: facebook/opt-30b | 66B: facebook/opt-66b | Dataset used as input prompt: | C4 (en, validation set) | joaogante/assisted_generation_benchmarks |
| built with Gradio. | Hosted on Spaces | | | |

Glancing at the collected numbers, we see that assisted generation can deliver significant latency reductions in diverse settings, but it is not a silver bullet – you should benchmark it before applying it to your use case. We can conclude that assisted generation:

- 🤏 Requires access to an assistant model that is at least an order of magnitude smaller than your model (the bigger the difference, the better);
- 🚀 Gets up to 3x speedups in the presence of INT8 and up to 2x otherwise, when the model fits in the GPU memory;
- 🤯 If you’re playing with models that do not fit in your GPU and are relying on memory offloading, you can see up to 10x speedups;
- 📄 Shines in input-grounded tasks, like automatic speech recognition or summarization.

**Sample with assisted generation**

Greedy decoding is suited for input-grounded tasks (automatic speech recognition, translation, summarization, ...) or factual knowledge-seeking. Open-ended tasks requiring large levels of creativity, such as most uses of a language model as a chatbot, should use sampling instead. Assisted generation is naturally designed for greedy decoding, but that doesn’t mean that you can’t use assisted generation with multinomial sampling!

Drawing samples from a probability distribution for the next token will cause our greedy assistant to fail more often, reducing its latency benefits. However, we can control how sharp the probability distribution for the next tokens is, using the temperature coefficient that’s present in most sampling-based applications. At one extreme, with temperatures close to 0, sampling will approximate greedy decoding, favoring the most likely token. At the other extreme, with the temperature set to values much larger than 1, sampling will be chaotic, drawing from a uniform distribution. Low temperatures are, therefore, more favorable to your assistant model, retaining most of the latency benefits from assisted generation, as we can see below.

#### Suggested labels
#### {   "key": "assisted-generation",   "value": "Text generation with the use of an assistant model for latency reduction" }

<details><summary>Metadata</summary>

- Duration: 23937 ms
- Datetime: 2024-01-10T22:01:28.548223
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

