**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**find images in fzf


**Response:**
find . -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.gif' -o -iname '*.bmp' -o -iname '*.tiff' -o -iname '*.webp' \) | fzf --preview 'xdg-open {}'

<details><summary>Metadata</summary>

- Duration: 5375 ms
- Datetime: 2024-01-11T23:07:01.713999
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

