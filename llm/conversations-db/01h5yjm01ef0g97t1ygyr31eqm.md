**Prompt:**
Quickly, what is the exact bash command to check if script is run in interactive shell?
Reply only with the exact command text and nothing else before or after.

**Response:**
[ -z "$PS1" ] && echo "Not interactive" || echo "Interactive"

<details><summary>Metadata</summary>

- Duration: 1042 ms
- Datetime: 2023-07-22T10:34:10.843126
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

