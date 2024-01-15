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
The changes made in the shell script are as follows:

1. Line 68: Added an alias "issues" that lists all the GitHub issues.
2. Line 74: Exported the variable "funcs" with the path to the shell functions script.
3. Line 68: Exported the variable "llmfuncs" with the path to the LLM shell functions script.
4. Lines 68-77: Commented out the session recorder script sourcing, denoted by the "#" symbol at the beginning of each line.

Please let me know if you need any further clarification or if there are any other questions.

<details><summary>Metadata</summary>

- Duration: 2401 ms
- Datetime: 2023-08-22T15:35:34.735283
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

