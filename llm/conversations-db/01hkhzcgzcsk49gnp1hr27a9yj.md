**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**Rename all .py files to .md


**Response:**
for file in *.py; do mv "$file" "${file%.py}.md"; done

<details><summary>Metadata</summary>

- Duration: 688 ms
- Datetime: 2024-01-07T12:46:55.803526
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

