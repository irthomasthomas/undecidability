**Prompt:**
Write a bash terminal command to check my local ip Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
ip addr show | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d '/' -f1

<details><summary>Metadata</summary>

- Duration: 944 ms
- Datetime: 2023-12-29T15:10:42.984461
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

