**Prompt:**
sqlite3 logs.db 'SELECT id, model, prompt, response FROM responses WHERE prompt LIKE '%linux%''                                                                                               1 ✘ 
Error: in prepare, near "%": syntax error
  prompt, response FROM responses WHERE prompt LIKE %linux%
                                      error here ---^

**Response:**
The error is because you didn't enclose `%linux%` in quotes. The correct command should be:

```bash
sqlite3 logs.db "SELECT id, model, prompt, response FROM responses WHERE prompt LIKE '%linux%'"
```

In SQL, string values must be enclosed in single quotes (`'`). The `%` is a wildcard character that matches any sequence of characters in a `LIKE` clause. So, `'%linux%'` matches any string that contains 'linux'.

<details><summary>Metadata</summary>

- Duration: 6781 ms
- Datetime: 2023-11-05T21:12:10.673767
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

