**Prompt:**
I have multiple directories containing a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... Or named like HYPERLAPSE_0181-HYPERPIECE-2022_10_03__07_20_01.  Write a bash script to find missing file numbers in the series in each subdir


**Response:**
```bash
#!/bin/bash

# Loop through each subdirectory
for dir in */; do
    # Extract the directory name
    subdir="${dir%/}"
    
    # Find the maximum file number in the series
    max_number=$(find "$subdir" -name "HYPERLAPSE*" -type f -printf "%f\n" | awk -F_ '{print $2}' | awk -F. '{print $1}' | sort -n | tail -n 1)
    
    # Loop through the file numbers in the series
    for i in $(seq -w 1 $max_number); do
        # Check if the file exists
        [ ! -f "$subdir/HYPERLAPSE_$i.DNG" ] && echo "Missing file: $subdir/HYPERLAPSE_$i.DNG"
    done
done
```

<details><summary>Metadata</summary>

- Duration: 5219 ms
- Datetime: 2023-10-05T18:53:29.817710
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

