**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**call a function multiple times in parallel


**Response:**
```bash
func() { echo "Do something"; }; export -f func; parallel func ::: {1..10}
```

<details><summary>Metadata</summary>

- Duration: 1920 ms
- Datetime: 2024-01-05T18:46:41.961924
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

