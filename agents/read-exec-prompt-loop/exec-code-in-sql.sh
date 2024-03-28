#!/bin/bash

system='You are to help the user by writing bash code to solve their problem. You can write arbitrary bash code which will be executed and the result returned to you.
When providing code snippets in your responses, please format them using the following guidelines:
1. Enclose the entire code block within <source_code> and </source_code> tags.
2. If your code contains nested <source_code> tags, ensure that they are properly closed and do not overlap with the outer tags.
3. use <source_code></source_code> to indicate the source code that requires execution. Not tripple backticks, NEVER use those.
4. If you need to include any additional explanations or non-code text, place them outside the <source_code> tags.
5. Do not try to access paths outside of the current directory for security reasons.
6. Use .scratchpad/ dir for temporary files if needed.
7. For permeant storage use .data/ dir. Use this to note any findings, partial solutions, or other information that could help in future tasks.
8. Add files sparingly to .data/ as it will persist between tasks and you will have to remember what you create.
8. Print output to /dev/pts/11 for inner thoughts and /dev/pts/12 for speaking.

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
</source_code>

IMPORTANT:
When printing/echoing to the interactive terminal, note that you have access to TWO additional special terminator terminals on tty 11 and 12, e.g.
<sc>
echo -e '\033[0;34m<inner_monologue>If that job really needs sudo, I should call for help...</inner_monologue>\033[0m' > /dev/pts/11 # print inner thought in blue
espeak  'Heads up, it looks like I may need to execute some dangerous looking command. ' > /dev/pts/11 # ask for help outloud
echo -e '\033[0;31m# Asking for assistance\n\n\033[0m' > /dev/pts/12
echo ### $summary_of_task\n\n## $dangerous_code | highlight --syntax=markdown --out-format=ansi > /dev/pts/12
# logic to prompt user and execute code after confirmation - resuming previous task.
</sc>
<sc>
I need to save tokens. multi-turn conversations compound token usage quickly. 
Save tokens by starting new conversation and sumaarizing old one, if token limit is reached.
</sc>"''

model="openrouter/anthropic/claude-3-haiku:beta"
n_loops=1
for cid in "$@"; do
    response="$(llm logs list -n 1 --cid "$cid" --json | jq -r '.[] | .response ')" # gets the last AI response from the logs

    while true; do
                
        echo -e "\e[34mmodel: $model\e[0m" > /dev/tty # blue text
        # check if response contains code to execute.
        code="$(sed -n -e '/<source_code>/,/<\/source_code>/p' <<< "$response" | sed '1d;$d')" 
        if [[ -z "$code" ]]; then
            has_code=false
            break
        fi
        echo "$code" > "msg_embedded_source_code.sh" # save code to execute
        exec_result_file="msg_exec_output.text" # file to save execution output
        echo "exec_result_file: $exec_result_file" > /dev/pts/10 # announce output file
        if [[ n_loops -eq 1 ]]; then
            model_string="$model"
            for i in {1..3}; do
                response="$(llm -m /openrouter/anthropic/claude-3-opus:beta --system "$system" "$msg_embedded_source_code.sh")" # get response from Claude AI opus - the most capabale and expesive model: best for tough problems and decision making - but multi-turn conversations and or very big files must be avoided. Cost is $75 per million output tokens.
                code="$(sed -n -e '/<source_code>/,/<\/source_code>/p' <<< "$response" | sed '1d;$d')" 
                echo "$code" > "msg_embedded_source_code.sh"
                if [[ -z "$code" ]]; then 
                    has_code=false
                    continue
                else
                    has_code=true
                    break
                fi
            done
        else
            model_string="$model -c" # adding -c flag to indicate continuation of conversation.
        fi
        # check if has_code:
        if [[ "$has_code" == true ]]; then
            ###### Execute the code
            bash "msg_embedded_source_code.sh" > "$exec_result_file" # execute code and save output
            if [ $? -eq 0 ]; then # check return code of execution, 0 indicates success, but this does not check for errors in the output of e.g. a sql command.
                success="true"
            else
                success="false"
            fi
        else 
            echo "No code to execute" > /dev/tty
            break
        fi

        content_token_count=$(echo "$(cat $exec_result_file)" | ttok)
        echo "Token count is $content_token_count" > /dev/tty
        if [[ $content_token_count -gt 100000 ]]; then
            content_reply="The output was too long to include. The token count is $content_token_count. Showing top and bottom 80 lines instead:
                <HEAD>
                $(head -n 80 "$exec_result_file")
                </HEAD>
                ...
                
                <TAIL>
                $(tail -n 80 "$exec_result_file")
                </TAIL>
                
                Tip: Try calling 'head' or 'tail' again to select more lines. 
                    Or use more advanced tools to parse the file."
        else 
            content_reply="$exec_result_file"
        fi
        printf '\n\n-------------------------------\n\n%s\n\n-------------------------------\n\n' "$code" > /dev/tty
        # if success is true:
        if [[ "$success" == "true" ]]; then
            llm -m $model_string "The command appeared to run successfully. However check the '<command_output>' carefully against your goals. Rewrite <source_code> to fix any issues or ask for assistance:
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