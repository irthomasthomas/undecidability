**Prompt:**
Write a bash terminal command to check which gpu driver is in use
Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
lspci -k | grep -A 2 -i "VGA"

<details><summary>Metadata</summary>

- Duration: 1938 ms
- Datetime: 2023-10-25T19:44:04.136732
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

