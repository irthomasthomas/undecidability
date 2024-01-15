**Prompt:**
68c68,74
< #
---
> alias issues='gh issue list'
> export funcs=$HOME/Development/scripts/shell_functions.sh
> export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
> 
> 
> [[ -z "$RECORDING_ON" ]] || source /home/tommy/Development/scripts/session-recorder.sh
> 
77a84
> 
81a89
> 
124,127d131
< alias issues='gh issue list'
< export funcs=$HOME/Development/scripts/shell_functions.sh
< export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
< 
129d132
< [[ -z "$RECORDING_ON" ]] || source /home/tommy/Development/scripts/session-recorder.sh
 explain changes: 

**Response:**
The changes made in the code are as follows:

1. Line 68: Added an alias "issues" which runs the command "gh issue list".
2. Line 69: Exported the variable "funcs" with the value "$HOME/Development/scripts/shell_functions.sh".
3. Line 70: Exported the variable "llmfuncs" with the value "$HOME/Development/scripts/llm_shell_functions.sh".
4. Line 74: Added a conditional statement to check if the variable "RECORDING_ON" is empty. If not empty, it sources the file "/home/tommy/Development/scripts/session-recorder.sh".
5. Line 77: Added an empty line.
6. Line 81: Added an empty line.
7. Lines 124-127: Removed the alias "issues", the export of "funcs" and "llmfuncs", and the conditional statement for sourcing "session-recorder.sh".
8. Line 129: Removed the conditional statement for sourcing "session-recorder.sh".

These changes add an alias, export two variables, and modify the conditional statement for sourcing a file.

<details><summary>Metadata</summary>

- Duration: 3445 ms
- Datetime: 2023-08-22T15:38:52.563688
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

