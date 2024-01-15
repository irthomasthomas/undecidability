**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**What is the best protocol for tinkering with another gh repo for learning, and with a view to contributing improvements? I already created a fork on gh and cloned the repo locally, then set default to my fork. Is that right?


**Response:**
```bash
git remote add upstream <original_repo_URL> && git fetch upstream && git checkout -b feature-branch upstream/main
```

<details><summary>Metadata</summary>

- Duration: 3067 ms
- Datetime: 2024-01-12T11:43:30.621557
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

