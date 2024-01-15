**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**turn the current dir into a gh repo


**Response:**
```bash
git init && git branch -M main && gh repo create --source=. --public
```

<details><summary>Metadata</summary>

- Duration: 1451 ms
- Datetime: 2024-01-06T21:35:52.973111
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

