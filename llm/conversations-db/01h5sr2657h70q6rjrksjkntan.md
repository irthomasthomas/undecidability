**Prompt:**
Quickly, what is the exact bash command to check if script is run in interactive shell?
Reply only with the exact command text and nothing else before or after.

**Response:**
[ -z "$PS1" ] && echo non-interactive || echo interactive

<details><summary>Metadata</summary>

- Duration: 1039 ms
- Datetime: 2023-07-20T13:33:06.583437
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

