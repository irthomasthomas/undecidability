**Prompt:**
Help: sending an issue comment to gh issue from linux terminal using gh cli. How do I format string to include new lines?

**Response:**
To include new lines in the issue comment you want to send using `gh cli`, you can use escape sequences or inline new lines. Here's how you can do it:

1. Using escape sequences: Use the `\n` escape sequence to indicate the new line.

```bash
gh issue comment create <issue-number> --body "This is the first line.\nThis is the second line."
```

2. Using inline new lines: You can include new lines inline within a single string by using the `$` character followed by double quotes around the string.

```bash
gh issue comment create <issue-number> --body $"This is the first line.
This is the second line."
```

Both of these methods will include new lines in the issue comment you send from the Linux terminal using `gh cli`. Choose the one that suits your preference.

<details><summary>Metadata</summary>

- Duration: 7973 ms
- Datetime: 2023-09-04T13:41:52.117659
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

