**Prompt:**
What is the exact zsh command to: read issues of another persons public github repo?

**Response:**
curl -s https://api.github.com/repos/{username}/{repo}/issues | jq '.[] | {title: .title, body: .body}'

<details><summary>Metadata</summary>

- Duration: 1529 ms
- Datetime: 2023-08-15T19:20:08.110123
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

