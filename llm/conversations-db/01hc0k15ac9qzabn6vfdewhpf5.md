**Prompt:**
I have multiple directories containing a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... Or named like HYPERLAPSE_0181-HYPERPIECE-2022_10_03__07_20_01.  Write a bash script to find missing file numbers in the series in each subdir. Lets think it through step-by-step


**Response:**
```bash
#!/bin/bash

find_missing_files() {
  # Loop through each directory
  for dir in */; do
    # Get the list of file numbers in the directory
    file_nums=$(ls "$dir" | grep -oP '(?<=HYPERLAPSE_)\d+' | sort -n)
    
    # Get the highest and lowest file numbers
    lowest=$(echo "$file_nums" | head -n 1)
    highest=$(echo "$file_nums" | tail -n 1)
    
    # Find the missing file numbers
    missing=()
    for ((i = lowest; i <= highest; i++)); do
      if ! echo "$file_nums" | grep -q "$i"; then
        missing+=("$i")
      fi
    done
    
    # Print the missing file numbers
    echo "$dir: ${missing[*]}"
  done
}

# Call the function
find_missing_files
```

<details><summary>Metadata</summary>

- Duration: 6106 ms
- Datetime: 2023-10-05T18:53:56.977561
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

