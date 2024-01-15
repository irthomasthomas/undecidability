**Prompt:**
Write a bash terminal command to PARSE title and url to variables from a markdown string like [title](url) Be concise, but include as much code as needed. Do not write anything else. Ever.

**Response:**
```bash
markdown="[title](url)"
title=$(echo "$markdown" | sed -n 's/.*\[\([^]]*\)\].*/\1/p')
url=$(echo "$markdown" | sed -n 's/.*(\([^)]*\)).*/\1/p')
```

<details><summary>Metadata</summary>

- Duration: 1802 ms
- Datetime: 2023-12-29T12:55:18.910946
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

