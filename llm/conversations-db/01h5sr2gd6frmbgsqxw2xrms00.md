**Prompt:**
Quickly, what is the exact bash command to check if script is run in interactive shell?
Reply only with the exact command text and nothing else before or after.

**Response:**
[ -z "$PS1" ] && echo "Not interactive" || echo "Interactive"

<details><summary>Metadata</summary>

- Duration: 1293 ms
- Datetime: 2023-07-20T13:33:16.824254
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

