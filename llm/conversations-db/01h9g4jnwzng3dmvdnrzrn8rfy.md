**Prompt:**
What does ls */ do in zsh on manjaro(Arch) linux?

**Response:**
In the Zsh shell on Manjaro or Arch Linux, the command "ls */" lists all the directories in the current directory, excluding any files.

Here's how it works:

- "ls" is the command to list files and directories.
- "*/" is a pattern or wildcard that matches all directories in the current directory. The asterisk (*) represents any characters, and the slash (/) specifies that only directories should be matched.
- When you run "ls */", Zsh expands the pattern and lists all the directories in the current directory.

For example, if you have the following directories in your current directory:
- "dir1"
- "dir2"
- "file1.txt"

Running "ls */" will show the following output:
- dir1
- dir2

The "file1.txt" is ignored because it is not a directory.

<details><summary>Metadata</summary>

- Duration: 7884 ms
- Datetime: 2023-09-04T13:02:06.034585
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

