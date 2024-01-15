**Prompt:**
Write a bash terminal command to check which gpu driver is in use
Be concise, but include as much code as needed. Do not write anything else. Ever.

**Response:**
lspci -k | grep -A 2 -i "VGA"

<details><summary>Metadata</summary>

- Duration: 877 ms
- Datetime: 2023-12-29T12:05:14.033402
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

