**Prompt:**
What is the exact zsh command to: combine github api or gh cli with glow to read the readme.MD of a github repo simonw/til?


**Response:**
gh api repos/simonw/til/readme | jq -r '.content' | base64 -d | glow -

<details><summary>Metadata</summary>

- Duration: 1134 ms
- Datetime: 2023-08-30T12:40:15.906019
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

