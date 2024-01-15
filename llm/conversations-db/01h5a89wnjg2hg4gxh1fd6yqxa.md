**Prompt:**
Think carefully. Write a complete, fully functional bash script to Take a path as $1 input. 
Get the lastfile modified: ls -lt | head -2 
Ask for user confirmation before deleting the $lastfile.?
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and performant. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.
WARNING: Your response must NOT include text OUTSIDE of the code block.
SAY NOTHING ELSE!

**Response:**
#!/bin/bash

# Check if the user provided a path as $1 input
if [ $# -eq 0 ]; then
   echo "No path provided. Please provide a path as input."
   exit 1
fi

# Navigate to the provided path
cd $1

# Get the last modified file
lastfile=$(ls -lt | head -2 | tail -1 | awk '{print $NF}')

# Check if the lastfile variable is empty (no files in the directory)
if [ -z "$lastfile" ]; then
   echo "No files found in the directory."
   exit 1
fi

# Ask for user confirmation before deleting the file
read -p "Are you sure you want to delete $lastfile? (y/n): " confirm

# Verify user's confirmation
if [[ $confirm =~ ^[Yy]$ ]]; then
   rm $lastfile
   echo "$lastfile deleted successfully."
else
   echo "Deletion cancelled by the user."
fi

exit 0

<details><summary>Metadata</summary>

- Duration: 7475 ms
- Datetime: 2023-07-14T13:08:58.878403
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

