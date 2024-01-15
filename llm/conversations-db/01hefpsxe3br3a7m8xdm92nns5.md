**Prompt:**
bASH SCRIPT file1.sh shares a dir with fileA.sh and fileB.sh, I want to source A and B from 1 but I may not know in advance which dir they may be extracted to.

**Response:**
You can use "$(dirname "$0")" to extract the directory of the current script in bash. Here's how you could source fileA.sh and fileB.sh from file1.sh using this approach:

```bash
#!/bin/bash
# This is within file1.sh

# Get the directory of the current script
DIR="$(dirname "$0")"

# Source fileA.sh and fileB.sh
source "$DIR/fileA.sh"
source "$DIR/fileB.sh"
```
This script will work regardless of where the scripts are located because it dynamically figures out the directory of the current script (file1.sh) and then uses that to provide the paths to fileA.sh and fileB.sh.

<details><summary>Metadata</summary>

- Duration: 12722 ms
- Datetime: 2023-11-05T12:19:47.344948
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

