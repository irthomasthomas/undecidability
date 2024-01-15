**Prompt:**
Is there a way to source bash scripts using relative paths?

**Response:**
Yes, you can source bash scripts using relative paths. When sourcing a script, you can specify the relative path to the script file instead of using an absolute path.

Here's an example to source a bash script using a relative path:

```bash
source ./path/to/script.sh
```

This assumes that the script you want to source is located in the `path/to` directory relative to the current directory. The `./` prefix denotes the current directory.

Note: When using relative paths, make sure you are executing the script from the correct working directory for the path to be valid.

<details><summary>Metadata</summary>

- Duration: 9124 ms
- Datetime: 2023-11-05T12:07:57.279621
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

