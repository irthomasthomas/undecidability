**Prompt:**
**USER_QUESTION:**
Explain some options for running this program and what the terms mean
**END_USER_QUESTION**


**Response:**

[INST] Options to run the `__main__.py` script:

1. `--model MODEL`: Specifies the path of the model to use for generating completions.
2. `--model_alias MODEL_ALIAS`: Specifies an alias name for the model to use for generating completions.
3. `--n_gpu_layers N_GPU_LAYERS`: Specifies the number of layers to put on the GPU. All remaining layers will be placed on the CPU. Set -1 to move all layers to the GPU.
4. `--main_gpu MAIN_GPU`: Specifies the main GPU to use when running the program.
5. `--tensor_split [TENSOR_SPLIT ...]`: Splits layers across multiple GPUs in proportion based on the provided tensor split values.
6. `--vocab_only VOCAB_ONLY`: Specifies whether to return only the vocabulary (True) or not (False).
7. `--use_mmap USE_MMAP`: Uses mmap if set to True. Mmap is a memory-mapping file I/O interface, which provides a virtual view of physical files on the system.
8. `--use_mlock USE_MLOCK`: Uses mlock if set to True. Mlock locks memory so that it cannot be paged out to disk by the operating system.
9. `--seed SEED`: Specifies a random seed number for generating completions. Set -1 for a random seed.
10. `--n_ctx N_CTX`: Specifies the context size used for generating completions.
11. `--n_batch N_BATCH`: Specifies the batch size to use per evaluation.
12. `--n_threads N_THREADS`: Specifies the number of threads to use.
13. `--n_threads_batch N_THREADS_BATCH`: Specifies the number of threads to use when batch processing.
14. `--rope_scaling_type ROPE_SCALING_TYPE`: Specifies the type of RoPE (Rotary Embeddings) scaling to use.
15. `--rope_freq_base ROPE_FREQ_BASE`: Specifies the base frequency for RoPE.
16. `--rope_freq_scale ROPE_FREQ_SCALE`: Specifies the frequency scaling factor for RoPE.
17. `--yarn_ext_factor YARN_EXT_FACTOR`: Specifies the external attention mechanism scaling factor in YARN (Yet Another Recurrent Network).
18. `--yarn_attn_factor YARN_ATTN_FACTOR`: Specifies the self-attention mechanism scaling factor in YARN.
19. `--yarn_beta_fast YARN_BETA_FAST`: Specifies the fast decay factor for attention mechanism in YARN.
20. `--yarn_beta_slow YARN_BETA_SLOW`: Specifies the slow decay factor for attention mechanism in YARN.
21. `--yarn_orig_ctx YARN_ORIG_CTX`: Specifies the original context size in YARN.
22. `--mul_mat_q MUL_MAT_Q`: Specifies whether to use experimental multi-matrix kernels (True) or not (False).
23. `--logits_all LOGITS_ALL`: Specifies whether to return logits for each token in the generated completions (True) or not (False).
24. `--embedding EMBEDDING`: Specifies whether to use embeddings (True) or not (False).
25. `--offload_kqv OFFLOAD_KQV`: Specifies whether to offload the key-value matrices to the GPU (True) or not (False).
26. `--last_n_tokens_size LAST_N_TOKENS_SIZE`: Specifies the number of last tokens to keep for repeat penalty calculation.
27. `--lora_base LORA_BASE`: Specifies an optional path to a base model, useful if using a quantized base model and you want to apply LoRA (Low-Rank Adaptation) to a floating point model.
28. `--lora_path LORA_PATH`: Specifies the path of a LoRA file to apply to the model.
29. `--numa NUMA`: Enables NUMA (Non-Uniform Memory Access) support for the program.
30. `--chat_format CHAT_FORMAT`: Specifies the chat format to use, such as "llama-2".
31. `--clip_model_path CLIP_MODEL_PATH`: Specifies the path of a CLIP model to use for multi-modal chat completion.
32. `--cache CACHE`: Enables caching to reduce processing times for evaluated prompts.
33. `--cache_type CACHE_TYPE`: Specifies the type of cache to use, such as "ram".
34. `--cache_size CACHE_SIZE`: Specifies the size of the cache in bytes.
35. `--verbose VERBOSE`: Specifies whether to print debug information (True) or not (False).
36. `--host HOST`: Specifies the address to listen on for incoming requests.
37. `--port PORT`: Specifies the port number to listen on for incoming requests.
38. `--ssl_keyfile SSL_KEYFILE`: Specifies the SSL key file path for HTTPS connections.
39. `--ssl_certfile SSL_CERTFILE`: Specifies the SSL certificate file path for HTTPS connections.
40. `--api_key API_KEY`: Specifies an API key to authenticate incoming requests. If set, all incoming requests need to be authenticated.
41. `--interrupt_requests INTERRUPT_REQUESTS`: Specifies whether to interrupt ongoing requests when a new request is received (True) or not (False).
42. `--config_file CONFIG_FILE`: Specifies the path of a config file to load and use for running the program.

<details><summary>Metadata</summary>

- Duration: 148366 ms
- Datetime: 2024-01-11T20:19:04.180517
- Model: dolphin-2.5-mixtral-8x7b

</details>

**Options:**
```json
{}
```

