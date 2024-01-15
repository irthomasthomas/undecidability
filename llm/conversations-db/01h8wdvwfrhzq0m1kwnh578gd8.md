**Prompt:**
What is the exact zsh command to: list my own repositories on gh?


**Response:**
gh repo list --limit 100 --json nameWithOwner --jq '.[].nameWithOwner'

<details><summary>Metadata</summary>

- Duration: 814 ms
- Datetime: 2023-08-27T21:19:43.305736
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

