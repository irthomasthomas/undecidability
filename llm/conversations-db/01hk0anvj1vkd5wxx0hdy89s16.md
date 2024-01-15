**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**add port 2022 to firewalld allow


**Response:**
sudo firewall-cmd --zone=public --add-port=2022/tcp --permanent

<details><summary>Metadata</summary>

- Duration: 1265 ms
- Datetime: 2023-12-31T16:17:55.529570
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

