**Prompt:**
I need to do experiments to test the effects of all the different options in exllamav2. Here is a start I made. It needs to be tidied up and experiments added for lazy option, and batch_size.
I have no fingers so don't use placeholder text, always write the full solution. Here is a 40 dollar tip, friend.


import gc
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exllamav2 import(
    ExLlamaV2,
    ExLlamaV2Config,
    ExLlamaV2Cache,
    ExLlamaV2Cache_8bit,
    ExLlamaV2Tokenizer,
)

from exllamav2.generator import (
    ExLlamaV2BaseGenerator,
    ExLlamaV2Sampler
)

import time
import torch
import logging

# Initialize torch profiler
torch.cuda.memory._record_memory_history(max_entries=100000)

def test_max_seq_length(model_directory, cache, max_seqs):
    for max_seq_len in max_seqs:
        print(f"Testing max_seq_len {max_seq_len}")
        torch.cuda.empty_cache()
        model_directory = os.path.join(models_directory, model_directory)
        print()
        print(f"Loading model {model_directory} with cache_type {cache}")
        config = ExLlamaV2Config()
        config.model_dir = model_directory
        config.low_mem = True
        config.prepare()

        model = ExLlamaV2(config)

        file_prefix = f"{model_directory.split('/')[-1]}"
        torch.cuda.memory._dump_snapshot(f"{file_prefix}.pickle")
        
        if torch.cuda.device_count() > 1:
            split = [0,8]
        else:
            print("Found 1 GPU")
            split = []
        try:
            model.load(split)
        except Exception as e:
            print("Failed to load model")
            print(e)
            del model
            torch.cuda.empty_cache()
            gc.collect()
            time.sleep(2)
            # continue # change to return to exit
            return

        tokenizer = ExLlamaV2Tokenizer(config)
        if cache == "Cache_8bit":
            try:
                cache = ExLlamaV2Cache_8bit(model, max_seq_len = max_seq_len)
            except Exception as e:
                print("Failed to load 8bit cache")
                print(e)
                del model, cache
                torch.cuda.empty_cache()
                gc.collect()
                time.sleep(2)
                return
        else:
            try:
                cache = ExLlamaV2Cache(model, max_seq_len = max_seq_len)
            except Exception as e:
                print("Failed to load cache")
                print(e)
                del model, cache
                torch.cuda.empty_cache()
                gc.collect()
                time.sleep(2)
                return
        
        # print("Loading generator")
        generator = ExLlamaV2BaseGenerator(model, cache, tokenizer)

        # Generate some text

        settings = ExLlamaV2Sampler.Settings()
        settings.temperature = 0.85
        settings.top_k = 50
        settings.top_p = 0.8
        settings.token_repetition_penalty = 1.05
        settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])

        prompt = "Our story begins in the Scottish town of Auchtermuchty, where once"

        max_new_tokens = 150

        generator.warmup()
        time_begin = time.time()
        
        # print(f"Generating {max_new_tokens} tokens")
        output = generator.generate_simple(prompt, settings, max_new_tokens, seed = 1234)

        time_end = time.time()
        time_total = time_end - time_begin

        print(output)
        print()
        print(f"Cache type: {cache.__class__.__name__}")
        print(f"Response generated in {time_total:.2f} seconds, {max_new_tokens} tokens, {max_new_tokens / time_total:.2f} tokens/second")
        torch.cuda.memory._record_memory_history(enabled=None)
        torch.cuda.empty_cache()
        gc.collect()
        

def test_cache_types(model_directory, caches, max_seqs):
    for cache in caches:
        print(f"Testing cache type {cache}")
        test_max_seq_length(model_directory, cache, max_seqs)        

        

max_seqs = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192]
caches = ["Cache", "Cache_8bit"]
models_directory = "/home/thomas/Development/Projects/llm/Models/Test"
for model_directory in os.listdir(models_directory):
    print(f"Testing model {model_directory}")
    test_cache_types(model_directory, caches, max_seqs)
    

**Response:**
It looks like you're trying to test the effects of different configurations of the ExLlamaV2 model, specifically focusing on the maximum sequence length and cache types. To tidy up your code and add experiments for the `lazy` option and `batch_size`, I'll provide a revised version of your script with additional functions to test these parameters. I'll also make sure to handle the `lazy` option and `batch_size` within the existing functions where appropriate.

Here's the revised code:

```python
import gc
import sys
import os
import time
import torch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exllamav2 import (
    ExLlamaV2,
    ExLlamaV2Config,
    ExLlamaV2Cache,
    ExLlamaV2Cache_8bit,
    ExLlamaV2Tokenizer,
)

from exllamav2.generator import (
    ExLlamaV2BaseGenerator,
    ExLlamaV2Sampler
)

# Initialize torch profiler
torch.cuda.memory._record_memory_history(max_entries=100000)

def test_model_configuration(model_directory, cache_type, max_seq_len, lazy, batch_size):
    print(f"Testing configuration: cache_type={cache_type}, max_seq_len={max_seq_len}, lazy={lazy}, batch_size={batch_size}")
    torch.cuda.empty_cache()
    model_directory = os.path.join(models_directory, model_directory)
    print(f"Loading model {model_directory} with cache_type {cache_type}")

    config = ExLlamaV2Config()
    config.model_dir = model_directory
    config.low_mem = True
    config.lazy = lazy
    config.batch_size = batch_size
    config.prepare()

    model = ExLlamaV2(config)

    file_prefix = f"{model_directory.split('/')[-1]}"
    torch.cuda.memory._dump_snapshot(f"{file_prefix}.pickle")

    if torch.cuda.device_count() > 1:
        split = [0, 8]
    else:
        print("Found 1 GPU")
        split = []

    try:
        model.load(split)
    except Exception as e:
        print("Failed to load model")
        print(e)
        del model
        torch.cuda.empty_cache()
        gc.collect()
        time.sleep(2)
        return

    tokenizer = ExLlamaV2Tokenizer(config)
    if cache_type == "Cache_8bit":
        try:
            cache = ExLlamaV2Cache_8bit(model, max_seq_len=max_seq_len)
        except Exception as e:
            print("Failed to load 8bit cache")
            print(e)
            del model, cache
            torch.cuda.empty_cache()
            gc.collect()
            time.sleep(2)
            return
    else:
        try:
            cache = ExLlamaV2Cache(model, max_seq_len=max_seq_len)
        except Exception as e:
            print("Failed to load cache")
            print(e)
            del model, cache
            torch.cuda.empty_cache()
            gc.collect()
            time.sleep(2)
            return

    generator = ExLlamaV2BaseGenerator(model, cache, tokenizer)

    # Generate some text
    settings = ExLlamaV2Sampler.Settings()
    settings.temperature = 0.85
    settings.top_k = 50
    settings.top_p = 0.8
    settings.token_repetition_penalty = 1.05
    settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])

    prompt = "Our story begins in the Scottish town of Auchtermuchty, where once"
    max_new_tokens = 150

    generator.warmup()
    time_begin = time.time()

    output = generator.generate_simple(prompt, settings, max_new_tokens, seed=1234)

    time_end = time.time()
    time_total = time_end - time_begin

    print(output)
    print()
    print(f"Cache type: {cache.__class__.__name__}")
    print(f"Response generated in {time_total:.2f} seconds, {max_new_tokens} tokens, {max_new_tokens / time_total:.2f} tokens/second")
    torch.cuda.memory._record_memory_history(enabled=None)
    torch.cuda.empty_cache()
    gc.collect()

def run_experiments(models_directory, max_seqs, caches, lazy_options, batch_sizes):
    for model_directory in os.listdir(models_directory):
        print(f"Testing model {model_directory}")
        for cache in caches:
            for max_seq_len in max_seqs:
                for lazy in lazy_options:
                    for batch_size in batch_sizes:
                        test_model_configuration(model_directory, cache, max_seq_len, lazy, batch_size)

max_seqs = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192]
caches = ["Cache", "Cache_8bit"]
lazy_options = [True, False]
batch_sizes = [1, 2, 4, 8]  # Example batch sizes, adjust as needed
models_directory = "/home/thomas/Development/Projects/llm/Models/Test"

run_experiments(models_directory, max_seqs, caches, lazy_options, batch_sizes)
```

In this revised code, I've created a single function `test_model_configuration` that takes all the parameters you want to test, including `cache_type`, `max_seq_len`, `lazy`, and `batch_size`. The `run_experiments` function then iterates over all combinations of these parameters for each model in the `models_directory`.

Make sure to adjust the `batch_sizes` list to include the batch sizes you want to test. The `lazy` option is now a parameter of the `ExLlamaV2Config` object, and it's set before the model is loaded.

Remember to check the ExLlamaV2 documentation and source code to ensure that the `lazy` and `batch_size` options are correctly implemented and that they are compatible with the rest of the configuration settings.

<details><summary>Metadata</summary>

- Duration: 118206 ms
- Datetime: 2023-12-19T18:59:37.424807
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

