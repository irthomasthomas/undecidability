**Prompt:**
68,74c68
< alias issues='gh issue list'
< export funcs=$HOME/Development/scripts/shell_functions.sh
< export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
< 
< 
< [[ -z "$RECORDING_ON" ]] || source /home/tommy/Development/scripts/session-recorder.sh
< 
---
> #
84d77
< 
89d81
< 
131a124,127
> alias issues='gh issue list'
> export funcs=$HOME/Development/scripts/shell_functions.sh
> export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
> 
132a129
> [[ -z "$RECORDING_ON" ]] || source /home/tommy/Development/scripts/session-recorder.sh
 explain changes: 

**Response:**
The changes made in the code are as follows:

1. Line 68: Added an alias "issues" which is set to the command "gh issue list".
2. Line 74: Exported the variable "funcs" with the value "$HOME/Development/scripts/shell_functions.sh".
3. Line 77: Exported the variable "llmfuncs" with the value "$HOME/Development/scripts/llm_shell_functions.sh".
4. Line 84-89: Removed some empty lines.
5. Line 124-131: Added a conditional statement to check if the variable "RECORDING_ON" is empty. If it is not empty, it sources the file "/home/tommy/Development/scripts/session-recorder.sh".

<details><summary>Metadata</summary>

- Duration: 4409 ms
- Datetime: 2023-08-22T15:37:53.562025
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

