**Prompt:**
Rewrite both to use named pipes, the bash script should block while it waits for the pipe(s)
 cd /home/thomas/Development/linux-stuff

  (define-command-global pipe-selection-title-url ()
      (let* ((title (title (current-buffer)))
            (url (url (current-buffer)))
            (selection (ps-eval (ps:chain window (get-selection) (to-string))))
            (temp-title (uiop:run-program '("mktemp") :output '(:string :stripped)))
            (temp-url (uiop:run-program '("mktemp") :output '(:string :stripped)))
            (temp-selection (uiop:run-program '("mktemp") :output '(:string :stripped))))
          (uiop:launch-program
              (list "sh" "-c"
                    (concatenate 'string
                                "echo " "'" title "' > " temp-title "
  echo " "'" url "' > " temp-url "
  echo " "'" selection "' > " temp-selection)))))


send_note_to_github() {
    target_project="undecidability"
    target_directory=$HOME/"$target_project"
    if [ ! -d "${target_directory}" ]; then
        echo "Cannot find directory ${target_directory}"
        return 1
    fi

    cd "${target_directory}" || return 2

    if [ ! -f "/tmp/nyxt_title" ] || [ ! -f "/tmp/nyxt_url" ] || [ ! -f "/tmp/nyxt_Selection" ]; then
        echo "Cannot find required files"
        return 3
    fi

    TITLE="$(cat /tmp/nyxt_title)"
    BODY="$(cat /tmp/nyxt_url)
$(cat /tmp/nyxt_Selection)"
    LABEL="unclassified"

    if ! command -v gh &>/dev/null; then
        echo "gh could not be found"
        return 4
    fi

    gh issue create --title "$TITLE" --body "$BODY" --label "$LABEL"
    return 0
}

while true
do
    send_note_to_github
done

**Response:**
To use named pipes (FIFO) instead of temporary files, you'll need to create the pipes using `mkfifo` command and then use them in your scripts. Please note that reading from a named pipe is a blocking operation by default. Here's how you can modify your scripts:

```bash
cd /home/thomas/Development/linux-stuff

(define-command-global pipe-selection-title-url ()
    (let* ((title (title (current-buffer)))
          (url (url (current-buffer)))
          (selection (ps-eval (ps:chain window (get-selection) (to-string))))
          (pipe-title "/tmp/nyxt_title")
          (pipe-url "/tmp/nyxt_url")
          (pipe-selection "/tmp/nyxt_selection"))
        (uiop:run-program '("mkfifo" pipe-title))
        (uiop:run-program '("mkfifo" pipe-url))
        (uiop:run-program '("mkfifo" pipe-selection))
        (uiop:launch-program
            (list "sh" "-c"
                  (concatenate 'string
                              "echo " "'" title "' > " pipe-title "
echo " "'" url "' > " pipe-url "
echo " "'" selection "' > " pipe-selection)))))

send_note_to_github() {
    target_project="undecidability"
    target_directory=$HOME/"$target_project"
    if [ ! -d "${target_directory}" ]; then
        echo "Cannot find directory ${target_directory}"
        return 1
    fi

    cd "${target_directory}" || return 2

    pipe_title="/tmp/nyxt_title"
    pipe_url="/tmp/nyxt_url"
    pipe_selection="/tmp/nyxt_selection"

    if [ ! -p "${pipe_title}" ] || [ ! -p "${pipe_url}" ] || [ ! -p "${pipe_selection}" ]; then
        echo "Cannot find required pipes"
        return 3
    fi

    TITLE="$(cat ${pipe_title})"
    BODY="$(cat ${pipe_url})
$(cat ${pipe_selection})"
    LABEL="unclassified"

    if ! command -v gh &>/dev/null; then
        echo "gh could not be found"
        return 4
    fi

    gh issue create --title "$TITLE" --body "$BODY" --label "$LABEL"
    return 0
}

while true
do
    send_note_to_github
done
```

In this modification, I've replaced the temporary files with named pipes by using `mkfifo` command. Also, I've replaced `-f` (file existence check) with `-p` (named pipe existence check) in the bash script.

<details><summary>Metadata</summary>

- Duration: 68434 ms
- Datetime: 2023-10-24T13:46:09.646151
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.5}
```

**Prompt:**
No, you have to make the pipes in the bash script

**Response:**
Sure, here's your revised script where named pipes are created in the bash script:

```bash
define-command-global pipe-selection-title-url ()
    (let* ((title (title (current-buffer)))
          (url (url (current-buffer)))
          (selection (ps-eval (ps:chain window (get-selection) (to-string))))
          (pipe-title "/tmp/nyxt_title")
          (pipe-url "/tmp/nyxt_url")
          (pipe-selection "/tmp/nyxt_selection"))
        (uiop:launch-program
            (list "sh" "-c"
                  (concatenate 'string
                              "echo " "'" title "' > " pipe-title "
echo " "'" url "' > " pipe-url "
echo " "'" selection "' > " pipe-selection)))))

send_note_to_github() {
    target_project="undecidability"
    target_directory=$HOME/"$target_project"
    
    pipe_title="/tmp/nyxt_title"
    pipe_url="/tmp/nyxt_url"
    pipe_selection="/tmp/nyxt_selection"
    
    # create named pipes if they don't exist 
    [ ! -p "${pipe_title}" ] && mkfifo "${pipe_title}"
    [ ! -p "${pipe_url}" ] && mkfifo "${pipe_url}"
    [ ! -p "${pipe_selection}" ] && mkfifo "${pipe_selection}"

    if [ ! -d "${target_directory}" ]; then
        echo "Cannot find directory ${target_directory}"
        return 1
    fi

    cd "${target_directory}" || return 2

    if [ ! -p "${pipe_title}" ] || [ ! -p "${pipe_url}" ] || [ ! -p "${pipe_selection}" ]; then
        echo "Cannot find required pipes"
        return 3
    fi

    TITLE="$(cat ${pipe_title})"
    BODY="$(cat ${pipe_url})
$(cat ${pipe_selection})"
    LABEL="unclassified"

    if ! command -v gh &>/dev/null; then
        echo "gh could not be found"
        return 4
    fi

    gh issue create --title "$TITLE" --body "$BODY" --label "$LABEL"
    return 0
}

while true
do
    send_note_to_github
done
```

In this revision, named pipes are created in the bash script with `mkfifo` before they are used. The script checks if the pipes exist before creating them, avoiding errors if the pipes are already present.


<details><summary>Metadata</summary>

- Duration: 66244 ms
- Datetime: 2023-10-24T13:48:40.369818
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

