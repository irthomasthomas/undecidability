**Prompt:**
What is the exact zsh command to: open the current directory in gh browser?


**Response:**
gh browse --repo "$(gh repo view --json nameWithOwner --jq '.nameWithOwner')" -- "$(pwd)"

<details><summary>Metadata</summary>

- Duration: 1194 ms
- Datetime: 2023-08-25T16:49:48.774935
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

