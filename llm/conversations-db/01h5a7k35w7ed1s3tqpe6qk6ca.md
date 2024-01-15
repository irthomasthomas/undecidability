**Prompt:**
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. Don't include any instructions or other verbiage in this chat.
Think carefully. Write a complete, fully functional bash script to Take a path as $1 input. 
Get the lastfile modified: ls -lt | head -2 
Ask for user confirmation before deleting the $lastfile.?
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. Don't include any instructions or other verbiage in this chat.
Think it through step-by-step.

**Response:**
#!/bin/bash

# Take the path as input
path=$1

# Navigate to the specified directory
cd $path

# Get the last file modified
lastfile=$(ls -lt | head -2 | tail -1)

# Ask for user confirmation before deleting the file
read -p "Are you sure you want to delete $lastfile? (y/n) " confirm_delete

# If the user confirms deletion, delete the file
if [[ $confirm_delete == "y" ]]; then
  rm $lastfile
  echo "$lastfile deleted successfully."
else
  echo "Deletion cancelled."
fi

<details><summary>Metadata</summary>

- Duration: 4893 ms
- Datetime: 2023-07-14T12:56:34.462411
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

