**Prompt:**
Rewrite this to output two csv files, one containing paths of the found files, and the other the paths of the missing:\n /home/thomas/Development/scripts/search_for_icons_from_streamdeck_json.sh

**Response:**
To output two CSV files, one containing the paths of the found files and the other containing the paths of the missing files, you can use the following script:

```bash
#!/bin/bash

found_files_csv="/home/thomas/Development/scripts/found_files.csv"
missing_files_csv="/home/thomas/Development/scripts/missing_files.csv"

# Run the search_for_icons_from_streamdeck_json.sh script and redirect its output
output=$(bash /home/thomas/Development/scripts/search_for_icons_from_streamdeck_json.sh)

# Create separate CSV files for found and missing files
echo "$output" | grep -E "^Found:" | awk -F':' '{print $2}' > "$found_files_csv"
echo "$output" | grep -E "^Missing:" | awk -F':' '{print $2}' > "$missing_files_csv"

echo "Paths of found files saved to: $found_files_csv"
echo "Paths of missing files saved to: $missing_files_csv"
```

Make sure to replace `/home/thomas/Development/scripts/found_files.csv` and `/home/thomas/Development/scripts/missing_files.csv` with the desired file paths for the two CSV files.

<details><summary>Metadata</summary>

- Duration: 7248 ms
- Datetime: 2023-10-09T12:46:54.180348
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

