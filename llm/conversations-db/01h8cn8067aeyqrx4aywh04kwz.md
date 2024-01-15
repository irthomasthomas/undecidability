**Prompt:**
What is the exact zsh command to: update all pipx?


**Response:**
pipx list --outdated | cut -d' ' -f1 | xargs -n1 pipx upgrade

<details><summary>Metadata</summary>

- Duration: 1021 ms
- Datetime: 2023-08-21T18:20:49.224730
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

