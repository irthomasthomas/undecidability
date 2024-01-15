**Prompt:**
What is the exact zsh command to: view release notes for a certain release at https://github.com/simonw/openai-to-sqlite?


**Response:**
curl -s https://github.com/simonw/openai-to-sqlite/releases/tag/{release-number} | grep -Po '(?<=<div class="markdown-body">)[^<]*'

<details><summary>Metadata</summary>

- Duration: 4786 ms
- Datetime: 2023-08-24T13:04:20.361692
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

