**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**get notified of new issues in a gh repo


**Response:**
```bash
gh api -X GET /repos/:owner/:repo/issues --paginate | jq '.[] | select(.created_at > "2023-04-01T00:00:00Z")' | xargs -I {} notify-send "New Issue" "{}"
```

<details><summary>Metadata</summary>

- Duration: 4143 ms
- Datetime: 2024-01-02T10:48:18.388778
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

