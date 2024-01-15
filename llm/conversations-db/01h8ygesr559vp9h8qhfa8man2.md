**Prompt:**
writescript () {
	clipboard=$(paste) 
	if [[ $clipboard != *"#!"* ]]
	then
		clipboard="#!/bin/zsh\n$clipboard" 
	fi
	echo "$clipboard" | head -n 5
}
 Rewrite this ZSH function. Remove the clipboard stuff and use stdin. Pipe the new file to stdout

**Response:**
writescript () {
	if [[ $1 != *"#!"* ]]
	then
		echo "#!/bin/zsh"
		echo "$1"
	else
		echo "$1"
	fi
}

# Example usage:
echo "echo Hello, world!" | writescript

<details><summary>Metadata</summary>

- Duration: 1646 ms
- Datetime: 2023-08-28T16:43:28.278763
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
rewrite the script so that it checks which shell is active and uses the correct shebang

**Response:**
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

# Example usage:
echo "echo Hello, world!" | writescript

<details><summary>Metadata</summary>

- Duration: 3814 ms
- Datetime: 2023-08-28T16:45:12.394339
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
rewrite the script so that it checks which shell is active and uses the correct shebang. Allways minimise branching and sub-shells.

**Response:**
writescript() {
	current_shell=$(ps -p $$ -ocomm=)
	shebang="#!/"

	if [[ $current_shell == "zsh" ]]; then
		shebang+="bin/zsh"
	elif [[ $current_shell == "bash" ]]; then
		shebang+="bin/bash"
	fi

	if [[ $1 != *"#!"* ]]; then
		echo "$shebang"
		echo "$@"
	else
		echo "$@"
	fi
}

# Example usage:
echo "echo Hello, world!" | writescript

<details><summary>Metadata</summary>

- Duration: 3026 ms
- Datetime: 2023-08-28T16:49:39.351115
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

