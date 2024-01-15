**Prompt:**
I have multiple directories containing a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... Or named like HYPERLAPSE_0181-HYPERPIECE-2022_10_03__07_20_01.  Write a bash script to find missing file numbers in the series in each subdir


**Response:**
```bash
#!/bin/bash

# Iterate through each subdirectory
for dir in */; do
  
  # Get the list of existing files in the directory
  files=( "$dir"HYPERLAPSE_*.DNG "$dir"HYPERLAPSE_*.HYPERPIECE-* )
  
  # Get the total number of expected files
  total_files=$(ls "$dir" | grep -E "HYPERLAPSE_[0-9]{4}\.DNG|HYPERLAPSE_[0-9]{4}-HYPERPIECE-[0-9]{4}_[0-9]{2}_[0-9]{2}__[0-9]{2}_[0-9]{2}_[0-9]{2}" | wc -l)
  
  # Get the list of missing file numbers
  missing_files=()
  for i in $(seq -f "%04g" 1 "$total_files"); do
    if [[ ! " ${files[@]} " =~ " HYPERLAPSE_$i.DNG " && ! " ${files[@]} " =~ " HYPERLAPSE_$i-HYPERPIECE-* " ]]; then
      missing_files+=(HYPERLAPSE_$i)
    fi
  done
  
  # Print the missing file numbers in the subdirectory
  echo "$dir: ${missing_files[@]}"
done

```

<details><summary>Metadata</summary>

- Duration: 7715 ms
- Datetime: 2023-10-05T18:53:19.784612
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

