**Prompt:**
I have multiple directories containing a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... Or named like HYPERLAPSE_0181-HYPERPIECE-2022_10_03__07_20_01.  Write a bash script to find missing file numbers in the series in each subdir


**Response:**
```bash
#!/bin/bash

find_missing_file_numbers() {
  dir=$1
  files=( "$dir"/HYPERLAPSE_*.DNG ) # match all DNG files in the directory
  if [[ ${#files[@]} -eq 0 ]]; then
    echo "No files found in $dir"
  else
    file_numbers=( $(basename "${files[@]%.*}" | awk -F_ '{print $2}' | sort -n) )
    missing_numbers=""
    for ((i=1; i<=${#file_numbers[@]}; i++)); do
      if [[ ${file_numbers[i-1]} -ne $i ]]; then
        missing_numbers+=" $i"
      fi
    done
    if [[ -z $missing_numbers ]]; then
      echo "No missing file numbers in $dir"
    else
      echo "Missing file numbers in $dir:$missing_numbers"
    fi
  fi
}

for subdir in */; do
  subdir=${subdir%/} # remove trailing slash
  find_missing_file_numbers "$subdir"
done
```

<details><summary>Metadata</summary>

- Duration: 6632 ms
- Datetime: 2023-10-05T18:53:36.457631
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

