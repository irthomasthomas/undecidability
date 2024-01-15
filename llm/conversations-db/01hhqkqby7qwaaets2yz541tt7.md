**Prompt:**
 
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
This is a Bash script that detects Python code blocks in a text file and gives the user options to either save the code to a separate python file or run it.

The function `save_python_to_file` reads each line of the input file and stores it in the `new_output` variable. It then checks if the `new_output` contains both the opening and closing code block markers ('```') and '```python\n' marker (indicating the start of a Python code block). If the conditions are met, it extracts the Python code between the markers using `awk` and `sed`.

Next, it prompts the user with the message "PYTHON DETECTED, SAVE OR RUN IT? [s/r]" and reads the user's response. If the response starts with 's' or 'S', it saves the extracted Python code to a file named "saved_script.py" and displays a confirmation message. If the response starts with 'r' or 'R', it executes the Python code using the `python` command and captures the output.

Finally, it prints the output (if any) in a formatted manner surrounded by triple backticks ("\`\`\`") and displays it on the terminal.

<details><summary>Metadata</summary>

- Duration: 4783 ms
- Datetime: 2023-12-15T20:47:07.030775
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

