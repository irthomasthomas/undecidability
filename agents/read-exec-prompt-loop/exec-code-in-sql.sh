#!/bin/bash

system='You are to help the user by writing bash code to solve their problem. You can write arbitrary bash code which will be executed and the result returned to you. 
When providing code snippets in your responses, please format them using the following guidelines:
1. Enclose the entire code block within <source_code> and </source_code> tags.
2. If your code contains nested <source_code> tags, ensure that they are properly closed and do not overlap with the outer tags.
3. use <source_code></source_code> to indicate the source code that requires execution. Not tripple backticks, NEVER use those.
4. If you need to include any additional explanations or non-code text, place them outside the <source_code> tags.
5. Do not try to access paths outside of the current directory for security reasons.

Example:
<source_code>'+$(cat /home/thomas/undecidability/agents/read-exec-prompt-loop/execute.sh)+'</source_code>

This is an example of a properly formatted code block.

To read a file:
<source_code>
#!/bin/bash
cat filename.json
</source_code>

To check the structure of a json file:
<source_code>
jq '"'.[0] | keys' file.json
</source_code>"''

# model="openrouter/anthropic/claude-3-sonnet:beta"
model="openrouter/anthropic/claude-3-haiku:beta"
n_loops=1
for cid in "$@"; do
    response="$(llm logs list --cid "$cid" --json | jq -r '.[] | .response ')" 

    while true; do
        if [[ "$n_loops" -ge 7 ]]; then
            model="openrouter/anthropic/claude-3-sonnet:beta"
        fi
        echo "
        model: $model
        " > /dev/tty
        code="$(sed -n -e '/<source_code>/,/<\/source_code>/p' <<< "$response" | sed '1d;$d')" 
        # if code is empty, break.
        if [[ -z "$code" ]]; then
            break
        fi
        echo "$code" > "msg_embedded_source_code.sh"
        exec_result_file="msg_exec_output.text"
        echo "exec_result_file: $exec_result_file" > /dev/tty
        if [[ n_loops -eq 1 ]]; then
            model_string="$model"
        else
            model_string="$model -c"
        fi
        bash "msg_embedded_source_code.sh" > "$exec_result_file"
        if [ $? -eq 0 ]; then
            success="true"
        else
            success="false"
        fi
        content_token_count=$(echo "$(cat $exec_result_file)" | ttok)
        echo "Token count is $content_token_count" > /dev/tty
        if [[ $content_token_count -gt 100000 ]]; then
            content_reply="The output was too long to include. The token count is $content_token_count. Showing top and bottom 10 lines instead:
                <HEAD>
                $(head -n 10 "$exec_result_file")
                </HEAD>
                ...
                
                <TAIL>
                $(tail -n 10 "$exec_result_file")
                </TAIL>
                
                Try calling 'head' or 'tail' again to select more lines."
        else 
            content_reply="$exec_result_file"
        fi
        printf '\n\n-------------------------------\n\n%s\n\n-------------------------------\n\n' "$code" > /dev/tty
        # if success is true:
        if [[ "$success" == "true" ]]; then
            llm -m $model_string "The command appeared to run successfully. However check the '<command_output>' carefully and rewrite <source_code> to fix any issues:
            <source_code>
            $code
            </source_code>


            <command_output>
            $content_reply
            </command_output>" --system "$system"
        else
            content_reply=$(tail -n 20 "$exec_result_file")
            llm -m $model_string "The command appeared to fail. Check the '<command_output>' carefully and rewrite <source_code> to fix any issues:
            <source_code>
            $code
            </source_code>


            <command_output>
            $(cat $exec_result_file)
            </command_output>" --system "$system"
            printf '\n\nThere was an error running the command. Please check the syntax and try again.\n\n' > /dev/tty
        fi
        response="$(llm logs list -n 1 --json | jq -r '.[] | .response ')"
        sleep 5
        n_loops=$((n_loops+1))
    done
done