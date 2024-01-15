**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**turn the current dir into a gh repo


**Response:**
To turn the current directory into a GitHub repository, you can use the following bash terminal command:

```bash
git init
git remote add origin <repository_url>
git add .
git commit -m "Initial commit"
git push -u origin master
```

Replace `<repository_url>` with the URL of your GitHub repository.

<details><summary>Metadata</summary>

- Duration: 1751 ms
- Datetime: 2024-01-06T21:35:21.831918
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

