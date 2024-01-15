**Prompt:**
What is the exact zsh command to: add *.bak to head of .gitignore?


**Response:**
echo "*.bak" | cat - .gitignore > temp && mv temp .gitignore

<details><summary>Metadata</summary>

- Duration: 1243 ms
- Datetime: 2023-08-25T16:55:39.080186
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

