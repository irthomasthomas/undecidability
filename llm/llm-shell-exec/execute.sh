#!/bin/bash

# Read the input from pipe
read -r -d '' input

# Extract the code between triple backticks
code=$(sed -n '/```/,/```/p' <<< "$input" | sed '1d;$d')

# Save the code to a file with a default filename
filename="temp_script.sh"
echo "$code" > "$filename"


# Execute the file
sh "$filename" "01hs0rzbvnx2c3r65y0tmbn3bq"