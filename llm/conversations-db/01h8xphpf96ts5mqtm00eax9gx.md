**Prompt:**
What is the exact zsh command to: see how often I use a terminal tool, like grep, awk, wc, etc??


**Response:**
history | awk '{print $2}' | sort | uniq -c | sort -nr | grep -E "grep|awk|wc"

<details><summary>Metadata</summary>

- Duration: 1225 ms
- Datetime: 2023-08-28T09:10:40.670992
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

