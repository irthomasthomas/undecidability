**Prompt:**
When I run this bash script and send a request from nyxt to the pipeline nothing happens. It stays on the Found pipes lines. Is something wrong with the lisp?
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

    TITLE="$(cat $pipe_title)"

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

**Response:**
The bash script and the lisp code seem to be correct. However, there are a few things that you might want to check:

1. Make sure that the `gh` command is installed and available in your PATH. You can check this by running `gh --version` in your terminal.

2. Check if the `nyxt` is sending the data correctly to the pipes. You can do this by manually reading from the pipes using `cat /tmp/nyxt_title`, `cat /tmp/nyxt_url`, and `cat /tmp/nyxt_selection` commands in the terminal.

3. Check if the `nyxt` is running the `pipe-selection-title-url-new` command correctly. You can do this by adding some debug print statements in the lisp code and checking the `nyxt` logs.

4. Check if the `send_note_to_github` function is being called correctly in the bash script. You can do this by adding some debug echo statements in the bash script.

5. Check if the `gh issue create` command is working correctly. You can do this by manually running the command in the terminal with some test data.

6. Make sure that the `nyxt` and the bash script are running with the same user. If they are running with different users, they might not have access to the same `/tmp` directory.

7. Make sure that the `nyxt` and the bash script are running on the same machine. If they are running on different machines, they will not be able to access the same `/tmp` directory.

8. Check the permissions of the `/tmp` directory and the pipes. The user running the `nyxt` and the bash script should have read and write permissions to the `/tmp` directory and the pipes.

9. Check if there are any errors in the `nyxt` logs or the bash script output. These errors might give you a clue about what is going wrong.

<details><summary>Metadata</summary>

- Duration: 38951 ms
- Datetime: 2023-10-26T20:12:10.875807
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

