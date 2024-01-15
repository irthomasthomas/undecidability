**Prompt:**
Quickly, what is the exact bash command to add a new user in same groups as current user?
Reply only with the exact command text and nothing else before or after.

**Response:**
newuser="newusername"; sudo useradd -G $(id -Gn | sed 's/ /,/g') $newuser

<details><summary>Metadata</summary>

- Duration: 5979 ms
- Datetime: 2023-08-02T11:24:47.302011
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

