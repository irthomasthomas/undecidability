**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**enable x over ssh


**Response:**
To enable X11 forwarding over SSH, you need to include the `-X` or `-Y` option when connecting to the remote server using the `ssh` command.

Here is the bash terminal command to achieve this:

```
ssh -X user@remote_server
```

Replace `user` with your username and `remote_server` with the IP address or hostname of the remote server you want to connect to.

<details><summary>Metadata</summary>

- Duration: 2572 ms
- Datetime: 2023-12-26T14:53:36.557981
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

