**Prompt:**
I have two gpus. Update this bash one-liner to monitor them both seperately

while :; do printf "GPU 0 Memory Used: %s MiB" "$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits  | awk 'NR==1{print $1}')"; sleep 1; done

**Response:**
while :; do printf "GPU 0 Memory Used: %s MiB" "$(nvidia-smi --id=0 --query-gpu=memory.used --format=csv,noheader,nounits  | awk 'NR==1{print $1}')"; printf "GPU 1 Memory Used: %s MiB" "$(nvidia-smi --id=1 --query-gpu=memory.used --format=csv,noheader,nounits  | awk 'NR==1{print $1}')"; sleep 1; done

<details><summary>Metadata</summary>

- Duration: 3888 ms
- Datetime: 2023-12-17T14:24:57.831599
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

