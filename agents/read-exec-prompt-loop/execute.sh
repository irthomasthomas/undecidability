#!/bin/bash

# Read the input from pipe
read -r -d '' input


# Extract the code between <source_script> and </source_script>
code=$(sed -n '/<source_script>/,/<\/source_script>/p' <<< "$input" | sed '1d;$d')

# Handle nested source tags
while [[ "$code" == *'<source_script>'* ]]; do
    code=$(sed -n '/<source_script>/,/<\/source_script>/p' <<< "$code" | sed '1d;$d')
done

# Save the code to a file with a default filename
filename="temp_script.sh"
echo "$code" > "$filename"

# Execute the file
bash "$filename" "01hs0rzbvnx2c3r65y0tmbn3bq"