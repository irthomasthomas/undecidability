**Prompt:**
Help: sending an issue comment to gh issue from linux terminal using gh cli. How do I format string to include new lines?

**Response:**
Formatting a string to include new lines in a GitHub issue comment from a Linux terminal using GitHub CLI tool can be managed by the 'echo' command.

Here is an example:

```bash
gh issue comment <issue_number> --body "$(echo -e "This is my comment.\nThis is a new line.\nThis is another new line.")"
```

In this command, `-e` option of echo is used to enable interpretation of backslash escapes like "\n" for a new line. You should replace `<issue_number>` with the issue number you intend to comment on. 

Also, be sure to include your comment between the quotes following echo -e. You can add as many new lines as you want by including additional "\n". Be aware that the use of parenthesis $() is to preserve the newline characters from being stripped out. 

Remember that you have to be in the repository (after cloning) where the issue has been made before running this command, unless you specify the repository with `--repo` option before `issue comment`:

```bash
gh issue comment <issue_number> --repo <owner>/<repo> --body "$(echo -e "This is my comment.\nThis is a new line.\nThis is another new line.")"
```

<details><summary>Metadata</summary>

- Duration: 26073 ms
- Datetime: 2023-09-04T13:48:15.288965
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

