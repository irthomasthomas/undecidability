**Prompt:**
In KDE Plasma 5 running on manjaro (Arch) linux, how do I list the xdg
file tags, like dolphin uses? In the terminal

**Response:**
To list the XDG file tags in KDE Plasma 5 on Manjaro (Arch) Linux, you can use the `kioclient5` command-line tool. Here's how you can do it in the terminal:

1. Open a terminal window by pressing `Ctrl` + `Alt` + `T` or searching for "terminal" in the application launcher.
2. Type the following command and press Enter:
   ```
   kioclient5 exec "kcmshell5 filetypes"
   ```
   This command will open the "File Associations" settings window.
3. In the "File Associations" window, select the desired file category on the left side, such as "Text".
4. On the right side, you will see a list of associated file types for that category.
   Each file type will have a "+" button to expand and view the associated tags.

You can repeat the steps to view the tags for other file categories or explore various files.

<details><summary>Metadata</summary>

- Duration: 7825 ms
- Datetime: 2023-09-03T10:14:11.099488
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

