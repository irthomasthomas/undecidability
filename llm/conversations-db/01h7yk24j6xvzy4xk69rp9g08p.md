**Prompt:**
What is the exact zsh command to: delete the last 2 commands?

**Response:**
history -d $(history | tail -n 2 | awk '{print $1}')

<details><summary>Metadata</summary>

- Duration: 1063 ms
- Datetime: 2023-08-16T07:13:17.854745
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

