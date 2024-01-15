**Prompt:**
writescript () {
	current_shell=$(ps -p $$ -ocomm=)
	if [[ $current_shell == "zsh" ]]
	then
		if [[ $1 != *"#!"* ]]
		then
			echo "#!/bin/zsh"
			echo "$1"
		else
			echo "$1"
		fi
	elif [[ $current_shell == "bash" ]]
	then
		if [[ $1 != *"#!"* ]]
		then
			echo "#!/bin/bash"
			echo "$1"
		else
			echo "$1"
		fi
	fi
}
 Think carefully. Rewrite the script to get rid of all the needless branching. There is a much simpler, faster and more performant way to do this! Think about it

**Response:**
Sure, the following script will accomplish the same task without any branching:

```bash
writescript() {
    current_shell=$(ps -p $$ -ocomm=)
    [[ $1 != *"#!"* ]] && echo "#!${current_shell}"
    echo "$1"
}
```

In this script, we check if argument does not contain "#!" and if true, then we output the shell command with its name (which we get by checking the running process). Then we output the input argument itself. This version of the function handles any shell you're currently using, not just bash or zsh, and handles the shebang line in one pass instead of two.

<details><summary>Metadata</summary>

- Duration: 13852 ms
- Datetime: 2023-08-28T16:53:04.454188
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

