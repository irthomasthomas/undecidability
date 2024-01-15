**Prompt:**
llm "Example python script " | ./save_py.sh                                                                                                                                                                    ✔  5s   base  
Error: [Errno 32] Broken pipe
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe 

#!/bin/bash

save_python_to_file() {
    while IFS= read -r line; do
        new_output+=$line$'\n'
    done

    if [[ $new_output == *'```' ]] && [[ $new_output == *'```python\n'* ]]; then
        python_code=$(echo "$new_output" | awk '/```python/,/```/' | sed '1d;$d')
        echo -e "\e[31m <-- PYTHON DETECTED, SAVE OR RUN IT? [s/r] \e[0m"
        read -r response
        case $response in
            [Ss]* )
                echo "$python_code" > saved_script.py
                echo "Script saved to saved_script.py"
                ;;
            [Rr]* )
                result=$(python -c "$python_code" 2>&1)
                echo -e "\nOutput:\n\`\`\`\n$result\`\`\`"
                ;;
            * )
                echo "Action cancelled."
                ;;
        esac
    fi
}

**Response:**
The above script is used to save Python code blocks to a separate file or execute them. It reads the input from stdin and checks if it's a Python code block surrounded by triple backticks (```python ... ```) using regular expressions. If it detects a Python code block, it prompts the user to save or run the code. If the user chooses to save, the code block is saved to a file named `saved_script.py`. If the user chooses to run, the code is executed using the `python` command and the output is displayed.

<details><summary>Metadata</summary>

- Duration: 2581 ms
- Datetime: 2023-12-15T20:48:08.308228
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

