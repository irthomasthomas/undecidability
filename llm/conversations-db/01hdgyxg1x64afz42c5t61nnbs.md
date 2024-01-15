**Prompt:**
Rewrite this nyxt lisp function so that it only emits values. Both should use named pipes, the bash script should block while it waits for the pipe(s)
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
echo " "'" selection "' > " temp-selection "
cat " temp-title "
cat " temp-url "
cat " temp-selection)))))
This version of the function will print the title, url, and selection to their respective temporary files as before. Then, it will use the cat command to print the contents of each file to the terminal. Since the cat command does not block, the function will not block either.

<details><summary>Metadata</summary>

- Duration: 28598 ms
- Datetime: 2023-10-24T13:44:50.054787
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.5}
```

