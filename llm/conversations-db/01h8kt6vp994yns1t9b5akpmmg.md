**Prompt:**
What is the exact zsh command to: list releases at https://github.com/simonw/openai-to-sqlite?


**Response:**
curl -s https://api.github.com/repos/simonw/openai-to-sqlite/releases | jq '.[].name'

<details><summary>Metadata</summary>

- Duration: 1506 ms
- Datetime: 2023-08-24T13:02:15.269599
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

