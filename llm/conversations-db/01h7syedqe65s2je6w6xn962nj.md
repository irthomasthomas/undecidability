**Prompt:**
After thinking it through carefully, my top 5 favourite linux bash one-liners are... ?

**Response:**

# Delete all files and directories in the current directory
rm -rf *

# Delete all files with a .txt extension in the current directory
rm *.txt

# Delete the file "file.txt" if it exists in the current directory
rm file.txt

# Delete all files and directories in the current directory except for "file.txt"
rm -rf !(*.txt)

# Delete all files and directories in the current directory except for the ones in a directory called "backup"
rm -rf !(*backup)

<details><summary>Metadata</summary>

- Duration: 14190 ms
- Datetime: 2023-08-14T11:55:49.503688
- Model: mlc-chat-WizardCoder-15B-V1.0-q4f16_1

</details>

**Options:**
```json
{}
```

