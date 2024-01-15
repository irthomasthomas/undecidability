**Prompt:**
When I run this bash script and send a request from nyxt to the pipeline nothing happens. It stays on the Found pipes lines. There is something wrong with the bash, as the lisp is writing the pipes ok.

(define-command-global pipe-selection-title-url-new ()
    "New pipe selection to gh"
  (let* ((title (title (current-buffer)))
         (url (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (pipe-title "/tmp/nyxt_title")
         (pipe-url "/tmp/nyxt_url")
         (pipe-selection "/tmp/nyxt_selection"))
    (with-open-file (stream pipe-title
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
      (write-string title stream))
    (with-open-file (stream pipe-url
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
      (write-string url stream))
    (with-open-file (stream pipe-selection
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
      (write-string selection stream))))


 #!/bin/bash

send_note_to_github() {
    echo "Send Note To Github"
    target_project="undecidability"
    target_directory="$HOME/$target_project"

    pipe_title="/tmp/nyxt_title"
    pipe_url="/tmp/nyxt_url"
    pipe_selection="/tmp/nyxt_selection"

    # Delete named pipes if they exist
    rm "$pipe_title" && echo "Deleted named pipe: $pipe_title"
    sleep 1
    rm "$pipe_url" && echo "Deleted named pipe: $pipe_url"
    sleep 1
    rm "$pipe_selection" && echo "Deleted named pipe: $pipe_selection"
    sleep 1

    # Create named pipes if they don't exist
    if [ ! -p "$pipe_title" ]; then
        sleep 1
        mkfifo "$pipe_title" && echo "Created named pipe: $pipe_title"
    fi

    if [ ! -p "$pipe_url" ]; then
        mkfifo "$pipe_url" && echo "Created named pipe: $pipe_url"
        sleep 1
    fi

    if [ ! -p "$pipe_selection" ]; then
        mkfifo "$pipe_selection" && echo "Created named pipe: $pipe_selection"
    fi

    if [ ! -d "$target_directory" ]; then
        echo "Cannot find directory $target_directory"
        return 1
    fi

    cd "$target_directory" || return 2
    echo "$PWD"

    if [ ! -p "$pipe_title" ] || [ ! -p "$pipe_url" ] || [ ! -p "$pipe_selection" ]; then
        echo "Cannot find required pipes"
        return 3
    fi
    echo "Found pipes"

    TITLE="$(cat ${pipe_title})"

    BODY="$(cat $pipe_url)
$(cat $pipe_selection)"

    LABEL="unclassified"
    echo "TITLE: $TITLE"
    echo "BODY: $BODY"
    echo "LABEL: $LABEL"
    if ! command -v gh &>/dev/null; then
        echo "gh could not be found"
        return 4
    fi

    echo "Creating gh issue"
    gh issue create --title "$TITLE" --body "$BODY" --label "$LABEL"
    return 0
}

while true
do
    send_note_to_github
    sleep 10
done

**Response:**
The issue seems to be that the bash script is trying to delete the named pipes before reading from them. This is causing the script to hang because it's waiting for data on a pipe that no longer exists.

The Lisp code is writing to the pipes correctly, but the bash script deletes them before it has a chance to read the data. The bash script then recreates the pipes and waits for data, but at this point the Lisp code has already finished writing and won't write again until the next request.

To fix this, you should remove the lines that delete the pipes at the start of the `send_note_to_github` function. The bash script should create the pipes if they don't exist, then read from them. If the pipes already exist and contain data, the script will read this data and then wait for more. The pipes should not be deleted until the script is finished with them.

Here's how the start of your function should look:

```bash
send_note_to_github() {
    echo "Send Note To Github"
    target_project="undecidability"
    target_directory="$HOME/$target_project"

    pipe_title="/tmp/nyxt_title"
    pipe_url="/tmp/nyxt_url"
    pipe_selection="/tmp/nyxt_selection"

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
    ...
```

This way, the bash script will always read the data that the Lisp code writes to the pipes.

<details><summary>Metadata</summary>

- Duration: 40558 ms
- Datetime: 2023-10-26T20:18:47.936856
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

