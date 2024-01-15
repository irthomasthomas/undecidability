**Prompt:**
What is the exact zsh command to: see how often I use a terminal tool.?


**Response:**
history | awk '{print $2}' | sort | uniq -c | sort -nr

<details><summary>Metadata</summary>

- Duration: 1143 ms
- Datetime: 2023-08-28T09:11:40.257406
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

