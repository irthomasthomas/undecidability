**Prompt:**
Think it through carefully. Write a script to trap all errors in a terminal session for both bash and zsh?

**Response:**
You can trap errors in bash and zsh by using the `trap` command. The `trap` command allows you to catch signals and execute code when they occur. Signal `ERR` is sent when any command exits with non-zero status.

Here's a simple script that will trap all errors in a terminal session:

For bash:

```bash
#!/bin/bash

# Function to handle error
handle_error() {
  echo "Error occurred on line $1"
}

# Trap ERR signal and call handle_error function
trap 'handle_error $LINENO' ERR

# Your script goes here
```

For zsh:

```zsh
#!/bin/zsh

# Function to handle error
handle_error() {
  echo "Error occurred on line $1"
}

# Trap ERR signal and call handle_error function
TRAPZERR() {
  handle_error $LINENO
}

# Your script goes here
```

In both scripts, the `handle_error` function is called whenever an error occurs. The `$LINENO` variable contains the current line number in the script, which is passed to the `handle_error` function.

You can replace the `echo` command in the `handle_error` function with any code that you want to execute when an error occurs.

Note: The `trap` command only catches errors in commands that are executed after it is called. If you want to catch all errors in your script, you should call `trap` at the start of your script.

<details><summary>Metadata</summary>

- Duration: 18249 ms
- Datetime: 2023-08-27T10:20:29.798326
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

