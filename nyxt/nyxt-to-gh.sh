#!/bin/bash

create_pipes() {
    # Create named pipes if they don't exist
    if [ ! -p "$pipe_title" ]; then
        mkfifo "$pipe_title" && echo "Created named pipe: $pipe_title"
    fi

    if [ ! -p "$pipe_url" ]; then
        mkfifo "$pipe_url" && echo "Created named pipe: $pipe_url"
    fi

    if [ ! -p "$pipe_selection" ]; then
        mkfifo "$pipe_selection" && echo "Created named pipe: $pipe_selection"
    fi

    if [ ! -d "$target_directory" ]; then
        echo "Cannot find directory $target_directory"
        exit 1
    fi
}

send_note_to_github() {
    echo "Send Note To Github"
    target_project="undecidability"
    target_directory="$HOME/$target_project"

    pipe_title="/tmp/nyxt_title"
    pipe_url="/tmp/nyxt_url"
    pipe_selection="/tmp/nyxt_selection"

    create_pipes

    cd "$target_directory" || return 2
    echo "$PWD"

    if [ ! -p "$pipe_title" ] || [ ! -p "$pipe_url" ] || [ ! -p "$pipe_selection" ]; then
        echo "Cannot find required pipes"
        return 3
    fi
    echo "Found pipes"

    TITLE="$(cat ${pipe_title})"
    URL="$(cat $pipe_url)"
    SELECTION="$(cat $pipe_selection)"
    # If title is blank, set title to URL
    if [ -z "$TITLE" ]; then
        TITLE="$URL"
    fi
    BODY="$URL
$SELECTION"
    echo "$BODY"
    echo "TITLE: $TITLE"
    echo "BODY: $BODY"
    echo "LABEL: $LABEL"
    if ! command -v gh &>/dev/null; then
        echo "gh could not be found"
        return 4
    fi
    task_list="- [ ] [${TITLE}](${URL})"
    #Add $SELECTION text using the <details><summary>Details</summary> pattern

    BODY="$task_list

    $SELECTION"
    echo "Creating gh issue"
    gh issue create --title "$TITLE" --body "$BODY" --web --label "unclassified" --label "inbox-url" &
    return 0
}

while true
do
    send_note_to_github
    sleep 10
done
