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
- Lines 68-74: Added an alias `issues` which will run the command `gh issue list`.
- Lines 68: Exported the variable `funcs` with the value set to `/home/tommy/Development/scripts/shell_functions.sh`.
- Lines 69: Exported the variable `llmfuncs` with the value set to `/home/tommy/Development/scripts/llm_shell_functions.sh`.
- Lines 77-84: Removed the code block starting with `[[ -z "$RECORDING_ON" ]]` and ending with `session-recorder.sh`.
- Line 84: Added a comment indicating the start of a new section.
- Lines 89-131: Removed the empty lines.
- Lines 124-127: Added an alias `issues` which will run the command `gh issue list`.
- Line 129: Exported the variable `funcs` with the value set to `/home/tommy/Development/scripts/shell_functions.sh`.

<details><summary>Metadata</summary>

- Duration: 5079 ms
- Datetime: 2023-08-22T15:36:21.020209
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

