**Prompt:**
What is the exact zsh command to: Equivalent in zsh? export -f which?


**Response:**
There is no exact equivalent of the `export -f which` command in zsh. However, you can achieve a similar result by defining a function and exporting it. Here's how you can do it:

```zsh
which() {
    command which "$@"
}
export -f which
```

This defines a function called `which` that calls the `which` command using the `command` built-in. Then, the `export -f` command is used to export the function so that it is available in subshells.

Note that this is not exactly the same as the `export -f which` command in bash, as it exports the function definition rather than the result of the `which` command.

<details><summary>Metadata</summary>

- Duration: 4458 ms
- Datetime: 2023-08-25T19:34:27.105245
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

