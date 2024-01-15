**Prompt:**
Get the list of files (no dirs) in '/run/media/thomas/828ca7e5-381d-4149-8fc5-6d6aa26b90f2/trim_queue'.

Then make a find query that searches for any file starting with each filename sans ext. similar to: find /path/to/directory -type f \( -name "*query1*" -o -name "*query2*" -o -name "*query3*" \)

Location to search: '/run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/drone' and sub dirs.

**Response:**
To get the list of files (excluding directories) in '/run/media/thomas/828ca7e5-381d-4149-8fc5-6d6aa26b90f2/trim_queue', you can use the following command:

```bash
find /run/media/thomas/828ca7e5-381d-4149-8fc5-6d6aa26b90f2/trim_queue -type f
```

This will recursively search for files (`-type f`) in the specified directory and its subdirectories.

To create a find query that searches for files starting with each filename (without the extension), you can use a loop to generate the query dynamically. Here's an example:

```bash
#!/bin/bash

search_dir="/run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/drone"
trim_queue_dir="/run/media/thomas/828ca7e5-381d-4149-8fc5-6d6aa26b90f2/trim_queue"

# Get the list of filenames without extensions from trim_queue directory
filenames=()
while IFS= read -r file; do
    filenames+=("$(basename "$file" | cut -d. -f1)")
done < <(find "$trim_queue_dir" -type f)

# Generate the find query
query=""
for filename in "${filenames[@]}"; do
    query+=" -o -name \"*$filename*\""
done
query="${query:4}"  # Remove the leading " -o"

# Execute the find command
find "$search_dir" -type f \( $query \)
```

Make sure to replace `"/run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/drone"` with the actual location you want to search in and `"/run/media/thomas/828ca7e5-381d-4149-8fc5-6d6aa26b90f2/trim_queue"` with the location of the trim_queue directory.

This script will generate a find query that searches for files starting with each filename (without the extension) in the specified search directory and its subdirectories.

<details><summary>Metadata</summary>

- Duration: 30317 ms
- Datetime: 2023-10-30T08:56:20.293724
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

