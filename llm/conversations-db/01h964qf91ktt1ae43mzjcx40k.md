**Prompt:**
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
 below is the function i want in markdown, but function name is being cut:  

**Response:**
```markdown
## Command <a id='command'></a>
```
```
{cmd}
```
[Link to Command](#command)

## Token Count <a id='token_count'></a>
```
{token_count}
```
[Link to Token Count](#token_count)

## Output <a id='output'></a>
```
{output}
```
[Link to Output](#output)
```

Please note that the placeholder variables {cmd}, {token_count}, and {output} should be replaced with the actual values in your script.

<details><summary>Metadata</summary>

- Duration: 3506 ms
- Datetime: 2023-08-31T15:52:23.150021
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

