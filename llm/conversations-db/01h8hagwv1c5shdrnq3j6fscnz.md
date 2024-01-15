**Prompt:**
What is the exact zsh command to: find all files of mime type: application/vnd.sqlite3?


**Response:**
find . -type f -exec file --mime-type {} + | grep "application/vnd.sqlite3" | cut -d: -f1

<details><summary>Metadata</summary>

- Duration: 1937 ms
- Datetime: 2023-08-23T13:49:37.614937
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

