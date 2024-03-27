#!/bin/bash
# Read the input from pipe
read -r -d '' input

# Extract the code between <source_code> and </source_code>
code=$(sed -n '/<source_code>/,/<\/source_code>/p' <<< "$input" | sed '1d;$d')

# Handle nested source tags
while [[ "$code" == *'<source_code>'* ]]; do
    code=$(sed -n '/<source_code>/,/<\/source_code>/p' <<< "$code" | sed '1d;$d')
done

# Save the code
temp_file="temp_script.sh"
echo "$code" > "$temp_file"

# Execute
bash "$temp_file"