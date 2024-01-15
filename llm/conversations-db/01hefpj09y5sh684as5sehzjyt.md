**Prompt:**
Is there a way to source bash scripts relative to their paths? Suppose file1.sh shares a dir with fileA.sh and fileB.sh, I want to source A and B from 1 but I may not know in advance which dir they may be extracted to.

**Response:**
Yes, you can source a script relative to the path of the script doing the source.

You can achieve this by using a script directory in bash.

Here's how you can do it:

```Bash
# Get the directory path of the current script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Source other scripts relative to the current script's directory
source "${DIR}/fileA.sh"
source "${DIR}/fileB.sh"
```

In this script, `${BASH_SOURCE[0]}` holds the path of the script being executed. The `dirname` command gets the directory path portion of this, and `cd` changes to this directory. The `pwd` command then prints out the full path of the current directory. Finally, we use this directory path for sourcing other files.

This will ensure you're always sourcing from the same location as the original script, regardless of where you run it from.

<details><summary>Metadata</summary>

- Duration: 16989 ms
- Datetime: 2023-11-05T12:15:23.872376
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

