**Prompt:**
Write a bash terminal command to use ssh instead of password for git Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub | ssh user@hostname "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

<details><summary>Metadata</summary>

- Duration: 8364 ms
- Datetime: 2023-10-11T19:02:17.684115
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

