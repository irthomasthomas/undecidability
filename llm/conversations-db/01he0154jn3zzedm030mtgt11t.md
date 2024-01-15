**Prompt:**
The script returned zero results. But when I manually run: find /run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/drone -type f \(  -name "*2022_09_23__17_35_31*" -o -name "*2022_09_23__17_33_33*" -o -name "*2022_09_23__17_30_51*" -o -name "*2022_09_23__16_00_55*" -o -name "*2022_09_23__16_00_13*" \) it does return results.
+#!/bin/bash

search_dir="$1"
source_dir="$2"

# Get the list of filenames without extensions from trim_queue directory
filenames=()
while IFS= read -r file; do
    filenames+=("$(basename "$file" | cut -d. -f1)")
done < <(find "$source_dir" -type f)

# Chunk size for each find command
chunk_size=10

# Generate the find query for each chunk
chunks=()
chunk=""
count=0
for filename in "${filenames[@]}"; do
    if [ "$count" -eq "$chunk_size" ]; then
        chunks+=("$chunk")
        chunk=""
        count=0
    fi
    chunk+=" -name \"*$filename*\" -o"
    count=$((count+1))
done

# Add the last chunk to the list
chunks+=("$chunk")

# Execute the find command for each chunk
for chunk in "${chunks[@]}"; do
    query="${chunk::-3}"  # Remove the extra -o
    find "$search_dir" -type f \( $query \)
done

**Response:**
The script is designed to search for files in the `search_dir` directory that have the same names (without extensions) as the files in the `source_dir` directory. The names are divided into chunks of `chunk_size` (10 by default) and the `find` command is run for each chunk.

If the script returns zero results, it means that no files in the `search_dir` directory match the names of the files in the `source_dir` directory.

However, you mentioned that when you manually run the `find` command with specific filenames, it does return results. This suggests that the names you're searching for manually are not present in the `source_dir` directory, or they are present but their extensions are not being correctly removed by the `cut` command.

Here are a few things you can check:

1. Make sure the `source_dir` directory contains the files you're looking for. You can check this by running `ls $source_dir`.

2. Check if the filenames in the `source_dir` directory have extensions. If they don't, the `cut` command will not work as expected. You can check this by running `ls $source_dir | grep '.'`.

3. If the filenames in the `source_dir` directory have multiple periods, the `cut` command will only keep the part before the first period. For example, if a filename is `2022_09_23__17_35_31.txt.gz`, the `cut` command will return `2022_09_23__17_35_31`, not `2022_09_23__17_35_31.txt`. If this is the case, you might need to adjust the `cut` command to keep the part of the filename you're interested in.

4. Make sure the `search_dir` directory is the correct directory you want to search in. You can check this by running `ls $search_dir`.

5. Check if the `find` command is working correctly. You can do this by running one of the generated `find` commands manually and seeing if it returns the expected results.

<details><summary>Metadata</summary>

- Duration: 49540 ms
- Datetime: 2023-10-30T10:12:13.136330
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

