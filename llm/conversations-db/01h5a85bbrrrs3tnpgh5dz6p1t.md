**Prompt:**
Think carefully. Write a complete, fully functional bash script to Take a path as $1 input. 
Get the lastfile modified: ls -lt | head -2 
Ask for user confirmation before deleting the $lastfile.?
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and performant. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.

SAY NOTHING ELSE

**Response:**
#!/bin/bash

# Get the path from command-line argument
path=$1

# Get the last modified file in the given path
lastfile=$(ls -lt "$path" | awk 'NR==2 { print $NF }')

# Ask for user confirmation before deleting the last file
read -p "Are you sure you want to delete $lastfile? (y/n): " confirm

# Check user input for confirmation
if [[ $confirm == [Yy] ]]; then
    rm "$path/$lastfile"
    echo "File $lastfile deleted successfully!"
else
    echo "Deletion cancelled."
fi

<details><summary>Metadata</summary>

- Duration: 5090 ms
- Datetime: 2023-07-14T13:06:32.469179
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

