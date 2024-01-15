**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**write a jq to display this nice and with human date format: {
  "object": "list",
  "data": [
    {
      "id": "thread_vQ654DF9afSMfnu67ko2wAgf",
      "object": "thread",
      "created_at": 1704585868,
      "metadata": {}
    },
    {
      "id": "thread_47q4mssE0zfNdhuYYWjA24eD",
      "object": "thread",
      "created_at": 1704585708,
      "metadata": {}
    },


**Response:**
jq '.data[] | {id, object, created_at: (."created_at" | strftime("%Y-%m-%d %H:%M:%S"))}'

<details><summary>Metadata</summary>

- Duration: 1667 ms
- Datetime: 2024-01-08T12:46:42.782995
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

