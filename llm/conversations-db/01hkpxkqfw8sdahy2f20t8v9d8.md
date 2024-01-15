**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**can you keep writing new lines to a linux pipe before it is read?


**Response:**
mkfifo my_pipe; while true; do echo "new line" > my_pipe; sleep 1; done &

<details><summary>Metadata</summary>

- Duration: 3745 ms
- Datetime: 2024-01-09T10:52:03.803147
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

