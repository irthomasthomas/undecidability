**Prompt:**
writescript () {
	clipboard=$(paste) 
	if [[ $clipboard != *"#!"* ]]
	then
		clipboard="#!/bin/zsh\n$clipboard" 
	fi
	echo "$clipboard" | head -n 5
}
 Rewrite this ZSH function. Remove the clipboard stuff and use stdin. return the new file to stdout

**Response:**
#!/bin/zsh

writescript() {
    while IFS= read -r line; do
        if [[ $line != *"#!"* ]]
        then
            line="#!/bin/zsh\n$line"
        fi
        echo "$line"
        count=$((count + 1))
        if [ $count -eq 5 ]
        then
            break
        fi
    done
}

# Example usage:
# cat input.txt | writescript > output.txt

<details><summary>Metadata</summary>

- Duration: 2781 ms
- Datetime: 2023-08-28T16:43:13.907934
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

