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
 In the fewest words, explain changes: 

**Response:**
Lines 68-74 have been moved to lines 68-77. Line 84 has been deleted. Lines 89-131 have been moved to lines 81-124. Line 132 has been added.

<details><summary>Metadata</summary>

- Duration: 2509 ms
- Datetime: 2023-08-22T15:36:09.505675
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

