**Prompt:**
for current_task in {"steno","neural_code"};

**Response:**
 do
    for current_dataset in {"steno","neural_code"}; do
        for current_model in {"steno","neural_code"}; do
            for current_seed in {1..5}; do
                python3 main.py --task $current_task --dataset $current_dataset --model $current_model --seed $current_seed
            done
        done
    done
done
```

## Results

The results of the experiments are saved in the `results` folder. The results are saved in the following format:

```
results
├── steno
│   ├── steno
│   │   ├── steno
│   │   │   ├── 1
│   │   │   │   ├── results.json
│   │   │   │   └── weights.h5
│   │   │   ├── 2
│   │   │   │   ├── results.json
│   │   │   │   └── weights.h5
│   │   │   ├── 3
│   │   │   │   ├── results.json
│   │   │   │   └── weights.h5
│   │   │   ├── 4


<details><summary>Metadata</summary>

- Duration: 2981 ms
- Datetime: 2023-11-04T10:04:16.670576
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"temperature": 0.0}
```

