**Prompt:**
What is the exact zsh command to: parse markdown cli?


**Response:**
There isn't an exact zsh command to parse markdown from the command line. However, you can use a combination of tools to achieve this. One common approach is to use a tool like `pandoc` to convert markdown to another format, such as HTML or PDF. Here's an example command:

```zsh
pandoc input.md -o output.html
```

This command will convert the `input.md` file to HTML and save it as `output.html`. You can replace `output.html` with the desired output format.

Keep in mind that `pandoc` is not installed by default, so you may need to install it using a package manager like `brew` or `apt-get` before using it.

<details><summary>Metadata</summary>

- Duration: 4059 ms
- Datetime: 2023-08-28T11:43:00.141822
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

