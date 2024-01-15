**Prompt:**
usage: __main__.py [-h] [--model MODEL] [--model_alias MODEL_ALIAS] [--n_gpu_layers N_GPU_LAYERS]
                  [--main_gpu MAIN_GPU] [--tensor_split [TENSOR_SPLIT ...]] [--vocab_only VOCAB_ONLY]
                  [--use_mmap USE_MMAP] [--use_mlock USE_MLOCK] [--seed SEED] [--n_ctx N_CTX]
                  [--n_batch N_BATCH] [--n_threads N_THREADS] [--n_threads_batch N_THREADS_BATCH]
                  [--rope_scaling_type ROPE_SCALING_TYPE] [--rope_freq_base ROPE_FREQ_BASE]
                  [--rope_freq_scale ROPE_FREQ_SCALE] [--yarn_ext_factor YARN_EXT_FACTOR]
                  [--yarn_attn_factor YARN_ATTN_FACTOR] [--yarn_beta_fast YARN_BETA_FAST]
                  [--yarn_beta_slow YARN_BETA_SLOW] [--yarn_orig_ctx YARN_ORIG_CTX]
                  [--mul_mat_q MUL_MAT_Q] [--logits_all LOGITS_ALL] [--embedding EMBEDDING]
                  [--offload_kqv OFFLOAD_KQV] [--last_n_tokens_size LAST_N_TOKENS_SIZE]
                  [--lora_base LORA_BASE] [--lora_path LORA_PATH] [--numa NUMA]
                  [--chat_format CHAT_FORMAT] [--clip_model_path CLIP_MODEL_PATH] [--cache CACHE]
                  [--cache_type CACHE_TYPE] [--cache_size CACHE_SIZE] [--verbose VERBOSE]
                  [--host HOST] [--port PORT] [--ssl_keyfile SSL_KEYFILE]
                  [--ssl_certfile SSL_CERTFILE] [--api_key API_KEY]
                  [--interrupt_requests INTERRUPT_REQUESTS] [--config_file CONFIG_FILE]

🦙 Llama.cpp python server. Host your own LLMs!🚀

options:
  -h, --help            show this help message and exit
  --model MODEL         The path to the model to use for generating completions.
  --model_alias MODEL_ALIAS
                        The alias of the model to use for generating completions.
  --n_gpu_layers N_GPU_LAYERS
                        The number of layers to put on the GPU. The rest will be on the CPU. Set -1 to
                        move all to GPU.
  --main_gpu MAIN_GPU   Main GPU to use.
  --tensor_split [TENSOR_SPLIT ...]
                        Split layers across multiple GPUs in proportion.
  --vocab_only VOCAB_ONLY
                        Whether to only return the vocabulary.
  --use_mmap USE_MMAP   Use mmap. (default: True)
  --use_mlock USE_MLOCK
                        Use mlock. (default: True)
  --seed SEED           Random seed. -1 for random. (default: 4294967295)
  --n_ctx N_CTX         The context size. (default: 2048)
  --n_batch N_BATCH     The batch size to use per eval. (default: 512)
  --n_threads N_THREADS
                        The number of threads to use. (default: 16)
  --n_threads_batch N_THREADS_BATCH
                        The number of threads to use when batch processing. (default: 16)
  --rope_scaling_type ROPE_SCALING_TYPE
  --rope_freq_base ROPE_FREQ_BASE
                        RoPE base frequency
  --rope_freq_scale ROPE_FREQ_SCALE
                        RoPE frequency scaling factor
  --yarn_ext_factor YARN_EXT_FACTOR
  --yarn_attn_factor YARN_ATTN_FACTOR
  --yarn_beta_fast YARN_BETA_FAST
  --yarn_beta_slow YARN_BETA_SLOW
  --yarn_orig_ctx YARN_ORIG_CTX
  --mul_mat_q MUL_MAT_Q
                        if true, use experimental mul_mat_q kernels (default: True)
  --logits_all LOGITS_ALL
                        Whether to return logits. (default: True)
  --embedding EMBEDDING
                        Whether to use embeddings. (default: True)
  --offload_kqv OFFLOAD_KQV
                        Whether to offload kqv to the GPU.
  --last_n_tokens_size LAST_N_TOKENS_SIZE
                        Last n tokens to keep for repeat penalty calculation. (default: 64)
  --lora_base LORA_BASE
                        Optional path to base model, useful if using a quantized base model and you
                        want to apply LoRA to an f16 model.
  --lora_path LORA_PATH
                        Path to a LoRA file to apply to the model.
  --numa NUMA           Enable NUMA support.
  --chat_format CHAT_FORMAT
                        Chat format to use. (default: llama-2)
  --clip_model_path CLIP_MODEL_PATH
                        Path to a CLIP model to use for multi-modal chat completion.
  --cache CACHE         Use a cache to reduce processing times for evaluated prompts.
  --cache_type CACHE_TYPE
                        The type of cache to use. Only used if cache is True. (default: ram)
  --cache_size CACHE_SIZE
                        The size of the cache in bytes. Only used if cache is True. (default:
                        2147483648)
  --verbose VERBOSE     Whether to print debug information. (default: True)
  --host HOST           Listen address (default: localhost)
  --port PORT           Listen port (default: 8000)
  --ssl_keyfile SSL_KEYFILE
                        SSL key file for HTTPS
  --ssl_certfile SSL_CERTFILE
                        SSL certificate file for HTTPS
  --api_key API_KEY     API key for authentication. If set all requests need to be authenticated.
  --interrupt_requests INTERRUPT_REQUESTS
                        Whether to interrupt requests when a new request is received. (default: True)
  --config_file CONFIG_FILE
                        Path to a config file to load.


**Response:**


## Example usage:
```bash
./__main__.py --model "path/to/your/model" --n_gpu_layers -1 --use_mlock True --use_mmap False --seed 0 --n_ctx 256 --n_batch 1 --n_threads 8 --n_threads_batch 8 --rope_scaling_type "RMSNorm" --rope_freq_base 1e-6 --rope_freq_scale 1.0 --yarn_ext_factor 2.0 --yarn_attn_factor 2.0 --yarn_beta_fast 0.4 --yarn_beta_slow 0.4 --yarn_orig_ctx True --mul_mat_q True --logits_all False --embedding True --offload_kqv True --last_n_tokens_size 64 --lora_base "path/to/your/model" --lora_path "path/to/your/lora" --chat_format "llama-2" --clip_model_path "path/to/your/clip/model" --cache True --cache_type "ram" --cache_size 4294967295 --verbose True --host localhost --port 8001 --ssl_keyfile "path/to/your/ssl/key.pem" --ssl_certfile "path/to/your/ssl/cert.pem" --api_key "your-api-key" --interrupt_requests True
```

<details><summary>Metadata</summary>

- Duration: 37942 ms
- Datetime: 2024-01-11T19:32:03.362523
- Model: dolphin-2.5-mixtral-8x7b

</details>

**Options:**
```json
{}
```

