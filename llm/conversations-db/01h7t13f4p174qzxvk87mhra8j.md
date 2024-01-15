**Prompt:**
A cool bash script that acts as a tutorial for advanced linux shell scripting

**Response:**
#!/bin/bash

# This script will create a new directory and copy files to it

# Prompt user for directory name
echo "Enter directory name: "
read directory_name

# Create directory
mkdir $directory_name

# Copy files to directory
cp ~/Documents/file1.txt $directory_name/
cp ~/Documents/file2.txt $directory_name/
cp ~/Documents/file3.txt $directory_name/

# Print message to user
echo "Files copied to $directory_name directory."

<details><summary>Metadata</summary>

- Duration: 11754 ms
- Datetime: 2023-08-14T12:42:18.667524
- Model: mlc-chat-WizardCoder-15B-V1.0-q4f16_1

</details>

**Options:**
```json
{"temperature": 0.0}
```

