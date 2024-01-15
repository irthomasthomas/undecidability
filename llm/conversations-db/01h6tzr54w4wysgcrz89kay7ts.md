**Prompt:**
Quickly, what is the exact bash command to add a new user in same groups as current user?
Reply only with the exact command text and nothing else before or after.

**Response:**
sudo useradd -G $(id -Gn $(whoami)) newuser

<details><summary>Metadata</summary>

- Duration: 1671 ms
- Datetime: 2023-08-02T11:22:22.100693
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

