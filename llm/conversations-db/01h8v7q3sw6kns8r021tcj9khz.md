**Prompt:**
trap each error in the current terminal session. save the command that triggered it to suitable global var, and save the error/output text to another global var


**Response:**
```bash
trap 'last_command=$BASH_COMMAND' DEBUG
trap 'echo "Last command: $last_command. Error message: $?." >&2' ERR
```

<details><summary>Metadata</summary>

- Duration: 2652 ms
- Datetime: 2023-08-27T10:12:59.231351
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

