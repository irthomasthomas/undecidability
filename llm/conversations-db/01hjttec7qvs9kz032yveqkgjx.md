**Prompt:**
Write a bash terminal command to PARSE title and url to variables from a markdown string like [title](url) Be concise, but include as much code as needed. Do not write anything else. Ever.

**Response:**
echo "[title](url)" | sed -n 's/^\[\(.*\)\](\(.*\)\)$/\1 \2/p'

<details><summary>Metadata</summary>

- Duration: 1020 ms
- Datetime: 2023-12-29T12:58:01.338403
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

