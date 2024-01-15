**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**use fzf to display all jupyter notebooks. In the list view, only display only the filename


**Response:**
find . -type f -name "*.ipynb" | fzf --preview 'basename {}'

<details><summary>Metadata</summary>

- Duration: 2806 ms
- Datetime: 2024-01-09T10:43:16.539277
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

