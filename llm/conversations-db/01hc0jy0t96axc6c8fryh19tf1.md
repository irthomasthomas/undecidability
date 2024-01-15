**Prompt:**
I have multiple directories containing a series of files named HYPERLAPSE_0001.DNG, HYPERLAPSE_0002.DNG, HYPERLAPSE_0003.DNG... Or named like HYPERLAPSE_0181-HYPERPIECE-2022_10_03__07_20_01.  Write a bash script to find missing file numbers in the series in each subdir


**Response:**
```bash
#!/bin/bash

find_missing_file_numbers() {
  for dir in */; do
    cd "$dir" || continue
    files=$(ls HYPERLAPSE_*.DNG | sort -t "_" -k 2 -n)
    range=$(echo "$files" | grep -o -E '[0-9]+' | sort -n -u)
    missing=()

    i=1
    for num in $range; do
      while [[ $num -gt $i ]]; do
        missing+=($i)
        i=$((i+1))
      done
      i=$((i+1))
    done

    echo "Missing file numbers in $dir: ${missing[@]}"
    cd ..
  done
}

find_missi

<details><summary>Metadata</summary>

- Duration: 4738 ms
- Datetime: 2023-10-05T18:52:15.430054
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

