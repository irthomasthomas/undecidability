**Prompt:**
Is there a way to source bash scripts relative to their paths? Suppose file1.sh shares a dir with fileA.sh and fileB.sh, I want to source A and B from 1 but I may not know in advance which dir they may be extracted to.

**Response:**
Yes, it is possible to source bash scripts relative to their paths. You can use the `dirname` command to determine the directory of the currently executing script, and then construct the paths to the other scripts relative to that directory.

Here's an example:

```bash
#!/bin/bash

# Get the directory of the currently executing script
SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"

# Source fileA.sh and fileB.sh using their relative paths
source "$SCRIPT_DIR/fileA.sh"
source "$SCRIPT_DIR/fileB.sh"
```

In this example, the `SCRIPT_DIR` variable will store the directory of the currently executing script. You can then use this variable to construct the paths to the other scripts (`fileA.sh` and `fileB.sh`) by concatenating it with the appropriate relative path.

This way, you don't need to know the absolute paths of the scripts in advance and can source them relative to the location of the main script (`file1.sh` in your example).

<details><summary>Metadata</summary>

- Duration: 16974 ms
- Datetime: 2023-11-05T12:10:28.590422
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

