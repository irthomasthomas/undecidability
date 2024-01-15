**Prompt:**
 Warning: Error on separate thread: The value
  #&lt;QURI.URI.HTTP:URI-HTTPS https://github.com/irthomasthomas&gt;
is not of type
  SEQUENCE

(define-command-global pipe-selection-title-url ()
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

**Response:**
This code defines a global command `pipe-selection-title-url` that launches a separate thread to execute a shell command. The shell command echoes the title, URL, and selection of the current buffer to three separate temporary files (`pipe-title`, `pipe-url`, and `pipe-selection`).

<details><summary>Metadata</summary>

- Duration: 5753 ms
- Datetime: 2023-10-24T14:22:29.153789
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

