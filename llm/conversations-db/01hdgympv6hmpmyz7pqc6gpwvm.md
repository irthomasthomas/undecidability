**Prompt:**
Rewrite this nyxt lisp function so that it only emits values. Both should use named pipes, the bash script should block while it waits for the pipe(s)
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


**Response:**
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
echo " "'" selection "' > " temp-selection))
            :output '(:string :stripped))
        (values temp-title temp-url temp-selection)))


<details><summary>Metadata</summary>

- Duration: 22676 ms
- Datetime: 2023-10-24T13:40:08.018109
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.5}
```

