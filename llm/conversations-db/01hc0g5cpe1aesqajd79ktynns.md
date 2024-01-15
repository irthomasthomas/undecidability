**Prompt:**
I have a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... in a directory. Write a bash script to find missing file numbers in the series


**Response:**
#!/bin/bash

shopt -s nullglob

# Set the starting and ending file numbers of the series
START=1
END=100

# Loop through the file numbers
for ((i=START; i<=END; i++)); do
    # Check if the file exists
    if [ ! -f HYPERLAPSE_$(printf "%04d" $i).DNG ]; then
        # File is missing
        echo "Missing: $i"
    fi
done

<details><summary>Metadata</summary>

- Duration: 3171 ms
- Datetime: 2023-10-05T18:03:52.810208
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

