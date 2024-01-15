```bash
cmd_and_output_to_markdown () {
	cmd="$1" 
	title=$(echo $cmd | cut -d' ' -f2) 
	output=$(eval "$cmd") 
	token_count=$(ttok "$output") 
	formatted_output="## Command <a id='command'></a>
    \`\`\`
    ${cmd}
    \`\`\`
    [Link to Command](#command)
    
    ## Token Count <a id='token_count'></a>
    \`\`\`
    ${token_count}
    \`\`\`
    [Link to Token Count](#token_count)
    
    ## Output <a id='output'></a>
    \`\`\`
    ${output}
    \`\`\`
    [Link to Output](#output)
    " 
	echo -e "$formatted_output"
}
```
