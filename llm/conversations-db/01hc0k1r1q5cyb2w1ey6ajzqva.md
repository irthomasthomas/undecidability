**Prompt:**
I have multiple directories containing a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... Or named like HYPERLAPSE_0181-HYPERPIECE-2022_10_03__07_20_01.  Write a bash script to find missing file numbers in the series in each subdir. Lets think it through carefully


**Response:**
#!/bin/bash

# Function to find missing file numbers in a directory
find_missing_files_in_directory() {
    # Check if directory exists
    if [ -d "$1" ]; then
        # Change to the directory
        cd "$1" || return

        # Get the maximum file number in the directory
        max_file_num=$(ls -1 HYPERLAPSE_* 2>/dev/null | awk -F'[_.]' '{print $2}' | sort -n | tail -1)

        # Check if there are any files in the directory
        if [ -n "$max_file_num" ]; then
            # Loop through each file number in the series
            for ((i=1; i<=max_file_num; i++)); do
                # Check if the file exists
                if [ ! -f "HYPERLAPSE_$(printf "%04d" "$i").DNG" ]; then
                    # Print the missing file number
                    printf "%04d\n" "$i"
                fi
            done
        else
            # Print a message if there are no files in the directory
            echo "No files found in the directory"
        fi
    else
        # Print a message if the directory does not exist
        echo "Directory does not exist"
    fi
}

# Find missing file numbers in all subdirectories
find_missing_files_in_subdirectories() {
    # Loop through each subdirectory
    for subdir in */; do
        # Print the subdirectory name
        echo "Subdirectory: $subdir"
        
        # Find missing file numbers in the subdirectory
        find_missing_files_in_directory "$subdir"
    done
}

# Main script

# Check if input is empty
if [[ -z "$1" ]]; then
    echo "No input provided"
    exit 1
fi

# Use the provided directory as the starting point
starting_dir="$1"

# Change to the starting directory
cd "$starting_dir" || exit

# Find missing file numbers in all subdirectories
find_missing_files_in_subdirectories

<details><summary>Metadata</summary>

- Duration: 11492 ms
- Datetime: 2023-10-05T18:54:10.771095
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

