**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**use github api to add a new issue label for irthomasthomas/undecidability


**Response:**
```bash
curl -X POST -H "Authorization: token YOUR_GITHUB_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/irthomasthomas/undecidability/labels -d '{"name":"new_label","color":"000000"}'
```

<details><summary>Metadata</summary>

- Duration: 3506 ms
- Datetime: 2023-11-28T10:28:31.692039
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

