**Prompt:**
Make this content into a pretty gh markdown note:quote:- [ ] [OpenNMT/CTranslate2: Fast inference engine for Transformer models](https://github.com/OpenNMT/CTranslate2)\n
CTranslate2

CTranslate2 is a C++ and Python library for efficient inference with Transformer models.

The project implements a custom runtime that applies many performance optimization techniques such as weights quantization, layers fusion, batch reordering, etc., to accelerate and reduce the memory usage of Transformer models on CPU and GPU.

The following model types are currently supported:

Encoder-decoder models: Transformer base/big, M2M-100, NLLB, BART, mBART, Pegasus, T5, Whisper
Decoder-only models: GPT-2, GPT-J, GPT-NeoX, OPT, BLOOM, MPT, Llama, Mistral, CodeGen, GPTBigCode, Falcon
Encoder-only models: BERT, DistilBERT, XLM-RoBERTa
Compatible models should be first converted into an optimized model format. The library includes converters for multiple frameworks:

OpenNMT-py
OpenNMT-tf
Fairseq
Marian
OPUS-MT
Transformers
The project is production-oriented and comes with backward compatibility guarantees, but it also includes experimental features related to model compression and inference acceleration.

Key features

Fast and efficient execution on CPU and GPU
The execution is significantly faster and requires less resources than general-purpose deep learning frameworks on supported models and tasks thanks to many advanced optimizations: layer fusion, padding removal, batch reordering, in-place operations, caching mechanism, etc.
Quantization and reduced precision
The model serialization and computation support weights with reduced precision: 16-bit floating points (FP16), 16-bit brain floating points (BF16), 16-bit integers (INT16), and 8-bit integers (INT8).
Multiple CPU architectures support
The project supports x86-64 and AArch64/ARM64 processors and integrates multiple backends that are optimized for these platforms: Intel MKL, oneDNN, OpenBLAS, Ruy, and Apple Accelerate.
Automatic CPU detection and code dispatch
One binary can include multiple backends (e.g. Intel MKL and oneDNN) and instruction set architectures (e.g. AVX, AVX2) that are automatically selected at runtime based on the CPU information.
Parallel and asynchronous execution
Multiple batches can be processed in parallel and asynchronously using multiple GPUs or CPU cores.
Dynamic memory usage
The memory usage changes dynamically depending on the request size while still meeting performance requirements thanks to caching allocators on both CPU and GPU.
Lightweight on disk
Quantization can make the models 4 times smaller on disk with minimal accuracy loss.
Simple integration
The project has few dependencies and exposes simple APIs in Python and C++ to cover most integration needs.
Configurable and interactive decoding
Advanced decoding features allow autocompleting a partial sequence and returning alternatives at a specific location in the sequence.\n
#### Suggested labels
#### {   "key": "llm-inference-engines",   "value": "Software for efficient running of Large Language Model inferences" } {   "key": "llm-quantization",   "value": "All about optimizing and serving Quantized Large Language Models" }

**Response:**
> **CTranslate2**

CTranslate2 is a C++ and Python library for efficient inference with Transformer models.

The project implements a custom runtime that applies many performance optimization techniques such as weights quantization, layers fusion, batch reordering, etc., to accelerate and reduce the memory usage of Transformer models on CPU and GPU.

The following model types are currently supported:

- Encoder-decoder models: Transformer base/big, M2M-100, NLLB, BART, mBART, Pegasus, T5, Whisper
- Decoder-only models: GPT-2, GPT-J, GPT-NeoX, OPT, BLOOM, MPT, Llama, Mistral, CodeGen, GPTBigCode, Falcon
- Encoder-only models: BERT, DistilBERT, XLM-RoBERTa

Compatible models should be first converted into an optimized model format. The library includes converters for multiple frameworks:

- OpenNMT-py
- OpenNMT-tf
- Fairseq
- Marian
- OPUS-MT
- Transformers

The project is production-oriented and comes with backward compatibility guarantees, but it also includes experimental features related to model compression and inference acceleration.

**Key features**

- Fast and efficient execution on CPU and GPU
  - The execution is significantly faster and requires less resources than general-purpose deep learning frameworks on supported models and tasks thanks to many advanced optimizations: layer fusion, padding removal, batch reordering, in-place operations, caching mechanism, etc.
- Quantization and reduced precision
  - The model serialization and computation support weights with reduced precision: 16-bit floating points (FP16), 16-bit brain floating points (BF16), 16-bit integers (INT16), and 8-bit integers (INT8).
- Multiple CPU architectures support
  - The project supports x86-64 and AArch64/ARM64 processors and integrates multiple backends that are optimized for these platforms: Intel MKL, oneDNN, OpenBLAS, Ruy, and Apple Accelerate.
- Automatic CPU detection and code dispatch
  - One binary can include multiple backends (e.g. Intel MKL and oneDNN) and instruction set architectures (e.g. AVX, AVX2) that are automatically selected at runtime based on the CPU information.
- Parallel and asynchronous execution
  - Multiple batches can be processed in parallel and asynchronously using multiple GPUs or CPU cores.
- Dynamic memory usage
  - The memory usage changes dynamically depending on the request size while still meeting performance requirements thanks to caching allocators on both CPU and GPU.
- Lightweight on disk
  - Quantization can make the models 4 times smaller on disk with minimal accuracy loss.
- Simple integration
  - The project has few dependencies and exposes simple APIs in Python and C++ to cover most integration needs.
- Configurable and interactive decoding
  - Advanced decoding features allow autocompleting a partial sequence and returning alternatives at a specific location in the sequence.

#### Suggested labels
- { "key": "llm-inference-engines", "value": "Software for efficient running of Large Language Model inferences" }
- { "key": "llm-quantization", "value": "All about optimizing and serving Quantized Large Language Models" }

<details><summary>Metadata</summary>

- Duration: 11558 ms
- Datetime: 2024-01-13T13:30:44.905383
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

