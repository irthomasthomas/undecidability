#!/bin/bash

while true; do
llm -m openrouter/anthropic/claude-3-opus:beta --system  'When providing code snippets in your responses, please format them using the following guidelines:
1. Enclose the entire code block within <source_code> and </source_code> tags.
2. If your code contains nested <source_code> tags, ensure that they are properly closed and do not overlap with the outer tags.
3. use <source_code></source_code> to indicate the source code that requires execution. Not tripple backticks, NEVER use those.
4. If you need to include any additional explanations or non-code text, place them outside the <source_code> tags.

Example:
<source_code>

</source_code>

This is an example of a properly formatted code block.' "Improve the source_script so that the markdown_output it would produce is improved. beware of correct syntax.

<source_script>
$(cat temp_script.sh)
</source_script>

<markdown_output>
$(cat exec_test_output.md)
</markdown_output>

<description_of_screen># description of screenshot of vs code showing terminal, source code and the rendered markdown document.
$(cat screen_description.md)
</description_of_screen>" > response.md &&
cat response.md | sh execute.sh > exec_test_output.md &&
import -window 0x2c00006 screenshot.png &&
python /home/thomas/Development/LLMs/llm-vision-toolkit/GPT4-vision-toolkit.py describe 'screenshot.png' "Included is a screenshot of the computer showing visual studio code and terminal open but we dont need to mention that, instead focus on the content of the open document. Describe the image in your head, For markdown documents, describe the layout and style of the document, and any markdown elements. Can the presentation be improved? If so, mention that very very briefly/concisely." --output text > screen_description.md &&
done


for cid in "$@"; do
    response="$(llm logs list --cid "$cid" --json | jq -r '.[] | .response ')"
    # code="$(sed -n -e '/<source_script>/,/<\/source_script>/p' -e '/<source_code>/,/<\/source_code>/p' <<< "$response" | sed '1d;$d')"
    code="$(sed -n -e '/<source_code>/,/<\/source_code>/p' <<< "$response" | sed '1d;$d')" 
    echo "code: $code" > /dev/tty
    sleep 5
    filename="$cid.sh"
    echo "$filename" > /dev/tty
    # echo "$code" > /dev/tty
    echo "$code" > "$filename"
    bash "$filename" "01has61ch2mfkv3yzq1pgzkv6t"
    if [ $? -eq 0 ]; then
        printf '\n\n-------------------------------\n\n%s\n\n-------------------------------\n\n' "$response"
    else
        printf '\n\nThere was an error running the command. Please check the syntax and try again.\n\n'
    fi
done