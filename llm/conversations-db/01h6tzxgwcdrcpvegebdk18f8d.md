**Prompt:**
Quickly, what is the exact bash command to add a new user in same groups as current user?
Reply only with the exact command text and nothing else before or after.

**Response:**
newuser="newusername"; sudo useradd -G `groups $(whoami) | cut -f2 -d':' | tr ' ' ','` -m $newuser

<details><summary>Metadata</summary>

- Duration: 5507 ms
- Datetime: 2023-08-02T11:25:14.119963
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

