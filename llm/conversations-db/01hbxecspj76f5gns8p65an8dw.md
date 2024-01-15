**Prompt:**
Write a bash terminal command to disable ssh and enable root login Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
sudo systemctl stop sshd.service && sudo systemctl disable sshd.service && sudo sed -i 's/PermitRootLogin no/PermitRootLogin yes/' /etc/ssh/sshd_config && sudo systemctl restart sshd.service

<details><summary>Metadata</summary>

- Duration: 4184 ms
- Datetime: 2023-10-04T13:35:14.041687
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

