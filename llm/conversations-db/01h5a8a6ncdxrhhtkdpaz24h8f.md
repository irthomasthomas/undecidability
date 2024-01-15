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

# Store the input path as $1
input_path="$1"

# Get the last modified file in the input path
lastfile=$(ls -lt "$input_path" | head -2 | tail -1)

# Ask for user confirmation before deleting the lastfile
read -p "Are you sure you want to delete '$lastfile'? (y/n) " user_confirmation

# Check if the user confirmed the deletion
if [ "$user_confirmation" == "y" ]; then
    # Delete the lastfile
    rm "$lastfile"
    echo "File '$lastfile' deleted."
else
    echo "Deletion cancelled."
fi

<details><summary>Metadata</summary>

- Duration: 5202 ms
- Datetime: 2023-07-14T13:09:11.385806
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

