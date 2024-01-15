**Prompt:**
What is the exact zsh command to: read issues of another persons public github repo?

**Response:**
curl -s https://api.github.com/repos/{username}/{repo}/issues | jq '.[] | {title: .title, body: .body}'

<details><summary>Metadata</summary>

- Duration: 1412 ms
- Datetime: 2023-08-15T18:57:01.786292
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

