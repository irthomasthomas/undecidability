**Prompt:**
What is the exact zsh command to: Run a process and automatically kill it in 3 minutes?


**Response:**
The exact zsh command to run a process and automatically kill it in 3 minutes is:

```zsh
(sleep 180 && kill -9 $$) & process_command
```

Replace `process_command` with the actual command you want to run. This command starts a subshell `(sleep 180 && kill -9 $$)` in the background, which waits for 180 seconds (3 minutes) and then kills the current process. The `&` at the end runs the `process_command` in the foreground.

<details><summary>Metadata</summary>

- Duration: 4820 ms
- Datetime: 2023-09-04T16:59:03.432223
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

