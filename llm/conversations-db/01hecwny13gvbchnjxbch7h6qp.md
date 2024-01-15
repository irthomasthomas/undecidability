**Prompt:**
in {"steno","neural_code"}; do

**Response:**

    for model in {"bert","roberta"}; do
        for layer in {"all","last"}; do
            for task in {"pos","ner"}; do
                for seed in {1..5}; do
                    python run.py \
                        --model_name_or_path "bert-base-uncased" \
                        --model_type $model \
                        --task_name $task \
                        --layer $layer \
                        --output_dir "output/$model/$layer/$task/$seed" \
                        --data_dir "data/$task" \
                        --seed $seed \
                        --do_train \
                        --do_eval \
                        --do_predict \
                        --per_gpu_train_batch_size 32 \
                        --per_gpu_eval_batch_size 32 \
                        --learning_rate 2e-5 \
                        --num_train_epochs 3.0 \
                        --max_seq_length 128 \
                        --overwrite_output_dir \
                        --overwrite_cache \
                        --save_steps 10000 \
                        --logging_steps 10000 \
                        --eval_all_checkpoints \
                        --eval_steps 10000 \
                        --save_total_limit 1 \
                        --use_steno $use_steno
                done
            done
        done
    done


<details><summary>Metadata</summary>

- Duration: 2777 ms
- Datetime: 2023-11-04T10:04:54.985811
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"temperature": 0.0}
```

