**Prompt:**
Make this content into a pretty gh markdown note:quote:- [ ] [
mit-han-lab/streaming-llm: Efficient Streaming Language Models with Attention Sinks](
https://github.com/mit-han-lab/streaming-llm)\n

TL;DR

We deploy LLMs for infinite-length inputs without sacrificing efficiency and performance.

News

[2023/10] StreamingLLM is integrated into Intel Extension for Transformers.
[2023/10] Check out Attention Sinks, a third-party implementation to enable StreamingLLM on more Huggingface LLMs.
Abstract

Deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected, is urgently needed but poses two major challenges. Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory. Secondly, popular LLMs cannot generalize to longer texts than the training sequence length. Window attention, where only the most recent KVs are cached, is a natural approach --- but we show that it fails when the text length surpasses the cache size. We observe an interesting phenomenon, namely attention sink, that keeping the KV of initial tokens will largely recover the performance of window attention. In this paper, we first demonstrate that the emergence of attention sink is due to the strong attention scores towards initial tokens as a ``sink'' even if they are not semantically important. Based on the above analysis, we introduce StreamingLLM, an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence length without any fine-tuning. We show that StreamingLLM can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more. In addition, we discover that adding a placeholder token as a dedicated attention sink during pre-training can further improve streaming deployment. In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2x speedup.

Usage

Environment Setup

conda create -yn streaming python=3.8
conda activate streaming

pip install torch torchvision torchaudio
pip install transformers==4.33.0 accelerate datasets evaluate wandb scikit-learn scipy sentencepiece

python setup.py develop
Run Streaming Llama Chatbot

CUDA_VISIBLE_DEVICES=0 python examples/run_streaming_llama.py  --enable_streaming
FAQ

What does "working on infinite-length inputs" imply for LLMs?

Handling infinite-length text with LLMs presents challenges. Notably, storing all previous Key and Value (KV) states demands significant memory, and models might struggle to generate text beyond their training sequence length. StreamingLLM addresses this by retaining only the most recent tokens and attention sinks, discarding intermediate tokens. This enables the model to generate coherent text from recent tokens without a cache reset — a capability not seen in earlier methods.

Is the context window of LLMs expanded?

No. The context window remains unchanged. Only the most recent tokens and attention sinks are retained, discarding middle tokens. This means the model can only process the latest tokens. The context window remains constrained by its initial pre-training. For instance, if Llama-2 is pre-trained with a context window of 4096 tokens, then the maximum cache size for StreamingLLM on Llama-2 remains 4096.

Can I input an extensive text, like a book, into StreamingLLM for summarization?

While you can input a lengthy text, the model will only recognize the latest tokens.\n
#### Suggested labels
#### {   "key": "llm-streaming",   "value": "Efficient deployment of Large Language Models for infinite-length inputs without sacrificing efficiency and performance" }

**Response:**
> **Note: Efficient Streaming Language Models with Attention Sinks**
> 
> [mit-han-lab/streaming-llm: Efficient Streaming Language Models with Attention Sinks](https://github.com/mit-han-lab/streaming-llm)
> 
> **TL;DR**
> 
> We deploy LLMs for infinite-length inputs without sacrificing efficiency and performance.
> 
> **News**
> 
> - [2023/10] StreamingLLM is integrated into Intel Extension for Transformers.
> - [2023/10] Check out Attention Sinks, a third-party implementation to enable StreamingLLM on more Huggingface LLMs.
> 
> **Abstract**
> 
> Deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected, is urgently needed but poses two major challenges. Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory. Secondly, popular LLMs cannot generalize to longer texts than the training sequence length. Window attention, where only the most recent KVs are cached, is a natural approach --- but we show that it fails when the text length surpasses the cache size. We observe an interesting phenomenon, namely attention sink, that keeping the KV of initial tokens will largely recover the performance of window attention. In this paper, we first demonstrate that the emergence of attention sink is due to the strong attention scores towards initial tokens as a "sink" even if they are not semantically important. Based on the above analysis, we introduce StreamingLLM, an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence length without any fine-tuning. We show that StreamingLLM can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more. In addition, we discover that adding a placeholder token as a dedicated attention sink during pre-training can further improve streaming deployment. In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2x speedup.
> 
> **Usage**
> 
> **Environment Setup**
> 
> ```
> conda create -yn streaming python=3.8
> conda activate streaming
> 
> pip install torch torchvision torchaudio
> pip install transformers==4.33.0 accelerate datasets evaluate wandb scikit-learn scipy sentencepiece
> 
> python setup.py develop
> ```
> 
> **Run Streaming Llama Chatbot**
> 
> ```
> CUDA_VISIBLE_DEVICES=0 python examples/run_streaming_llama.py --enable_streaming
> ```
> 
> **FAQ**
> 
> **What does "working on infinite-length inputs" imply for LLMs?**
> 
> Handling infinite-length text with LLMs presents challenges. Notably, storing all previous Key and Value (KV) states demands significant memory, and models might struggle to generate text beyond their training sequence length. StreamingLLM addresses this by retaining only the most recent tokens and attention sinks, discarding intermediate tokens. This enables the model to generate coherent text from recent tokens without a cache reset — a capability not seen in earlier methods.
> 
> **Is the context window of LLMs expanded?**
> 
> No. The context window remains unchanged. Only the most recent tokens and attention sinks are retained, discarding middle tokens. This means the model can only process the latest tokens. The context window remains constrained by its initial pre-training. For instance, if Llama-2 is pre-trained with a context window of 4096 tokens, then the maximum cache size for StreamingLLM on Llama-2 remains 4096.
> 
> **Can I input an extensive text, like a book, into StreamingLLM for summarization?**
> 
> While you can input a lengthy text, the model will only recognize the latest tokens.

<details><summary>Metadata</summary>

- Duration: 11740 ms
- Datetime: 2024-01-13T11:22:41.609231
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

