#!/bin/bash


for cid in "$@"; do
    response="$(llm logs list --cid "$cid" --json | jq -r '.[] | .response ')"
    # code="$(sed -n -e '/<source_script>/,/<\/source_script>/p' -e '/<source_code>/,/<\/source_code>/p' <<< "$response" | sed '1d;$d')"
    code="$(sed -n -e '/<source_script>/,/<\/source_script>/p' <<< "$response" | sed '1d;$d')" 
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