**Prompt:**
What is the exact zsh command to: view release notes for a certain release at https://github.com/simonw/openai-to-sqlite?


**Response:**
curl -s https://github.com/simonw/openai-to-sqlite/releases/tag/{release_tag} | grep -oP '(?<=<div class="markdown-body">).*?(?=</div>)' | lynx -stdin -dump

<details><summary>Metadata</summary>

- Duration: 2463 ms
- Datetime: 2023-08-24T13:03:41.409913
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

