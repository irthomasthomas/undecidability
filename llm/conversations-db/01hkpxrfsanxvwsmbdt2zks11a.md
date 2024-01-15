**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**can you keep writing new lines to a linux pipe before it is read?


**Response:**
```bash
mkfifo mypipe; while true; do echo "New line" > mypipe; sleep 1; done &
```

<details><summary>Metadata</summary>

- Duration: 3437 ms
- Datetime: 2024-01-09T10:54:40.060480
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 1.3}
```

