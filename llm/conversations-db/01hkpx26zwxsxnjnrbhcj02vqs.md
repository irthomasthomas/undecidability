**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**use fzf to display all jupyter notebooks. display only the filename


**Response:**
find . -name "*.ipynb" | fzf --preview 'basename {}'

<details><summary>Metadata</summary>

- Duration: 2325 ms
- Datetime: 2024-01-09T10:42:31.270514
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

