**Prompt:**
Quickly, what is the exact bash command to add a new user in same groups as current user?
Reply only with the exact command text and nothing else before or after.

**Response:**
newuser="newusername"; sudo useradd -G `groups $USER | cut -d' ' -f2- | sed 's/ /,/g'` -m $newuser

<details><summary>Metadata</summary>

- Duration: 3807 ms
- Datetime: 2023-08-03T11:17:16.934787
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

