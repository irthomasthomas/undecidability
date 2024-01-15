**Prompt:**
<WARN> [16:23:57] Warning: Error on separate thread: The value
  #&lt;QURI.URI.HTTP:URI-HTTPS https://github.com/irthomasthomas&gt;
is not of type
  VECTOR
when binding #:N-ARRAY31
<WARN> [16:24:20] Warning: Error on separate thread: The variable URL is unbound.

(define-command-global pipe-selection-title-url ()
    "Old"
    (let* ((title (title (current-buffer)))
          (render-url (url (current-buffer)))
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
It seems you have two errors reported here: 

1. A type error - The value is not of type VECTOR. This might be caused by providing the wrong type of parameter to a function that expects a VECTOR.
2. An unbound variable error - The variable URL is unbound. This means that you are trying to use a variable that has not been declared or initialized.

For the second error, it seems you assigned the current buffer's URL to the variable `render-url` but then you tried to use a non-existing variable `url`. 

So, in this line:
```
"echo " "'" url "' > " pipe-url "
```
you should replace `url` with `render-url`, since this is where you stored the URL.
```
"echo " "'" render-url "' > " pipe-url "
```

For the first error, without knowing exactly where it's occurring, it's harder to give a direct solution. You'll need to ensure wherever a VECTOR is expected, you're not passing a different type of parameter. It might also help to include some error checking and debugging logs in your code to help identify where and why the error occurs.

<details><summary>Metadata</summary>

- Duration: 26913 ms
- Datetime: 2023-10-24T15:25:26.354518
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

