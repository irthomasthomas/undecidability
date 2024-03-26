#!/bin/bash

# Read the input from pipe
read -r -d '' input

# Function to extract code from <source_code> tags
extract_code() {
    local code="$1"
    local start_tag="$2"
    local end_tag="$3"

    code=$(sed -n "/$start_tag/,/$end_tag/p" <<< "$code" | sed '1d;$d')

    while [[ "$code" == *"$start_tag"* ]]; do
    code=$(sed -n "/$start_tag/,/$end_tag/p" <<< "$code" | sed '1d;$d')
    done

    echo "$code"
}

# Extract the code between <source_code> and </source_code>
code=$(extract_code "$input" '<source_code>' '</source_code>')

# Save the code to a file with a default filename
filename="conversation_log_generator.sh"
echo "$code" > "$filename"

# Make the script executable
chmod +x "$filename"

# Execute the file with the provided conversation IDs as arguments
./"$filename" "$@"