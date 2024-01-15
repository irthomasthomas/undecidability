**Prompt:**
Quickly, what is the exact bash command to View systemd startup services?
Reply only with the exact command text and nothing else before or after.


**Response:**
systemctl list-unit-files --type=service --state=enabled

<details><summary>Metadata</summary>

- Duration: 1147 ms
- Datetime: 2023-09-12T14:29:41.941179
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
how do I view the details of each unit file?

**Response:**
systemctl cat <unit-file-name>

<details><summary>Metadata</summary>

- Duration: 916 ms
- Datetime: 2023-09-12T14:31:08.646142
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

