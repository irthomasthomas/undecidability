**Prompt:**
Warning: Error on separate thread: The value
  #&lt;QURI.URI.HTTP:URI-HTTPS https://www.google.com/&gt;
is not of type
  SEQUENCE

(define-command-global pipe-selection-title-url ()
    "Old"
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
This piece of Lisp code is a function declaration for a command used in the Nyxt browser, a open-source and customisable web browser for Emacs enthusiasts. 

The problem of this code is that `url` function returns an object rather than a string sequence as expected. It seems this URL object is not convertible to a string directly. 

To convert the URL object of QURI (a library for URL parsing and building) to a string, the `render` function could be used:

```lisp
(define-command-global pipe-selection-title-url ()
    "Old"
    (let* ((title (title (current-buffer)))
          (url (quri:render-uri (url (current-buffer)))) ;; Added render-url function here
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
```

This issue might be a bug in the URL extraction part of the Nyxt browser, it can be considered to be reported to the Nyxt community.

<details><summary>Metadata</summary>

- Duration: 32741 ms
- Datetime: 2023-10-24T15:31:24.541044
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
But the following function works, can you not emulate that?
(define-command-global pipe-selection-title-url-old ()
  (let* ((title (title (current-buffer)))
         (url (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (formatted-output
            (format nil "~a~%~a~%~a" title url selection)))
    (uiop:launch-program
        (list "sh" "-c"
            (concatenate 'string
                         "echo "
                         "'" formatted-output "'"
                         " > /tmp/nyxt_selection_pipe")))))

**Response:**
Yes, the second function works because it uses the `format` function to create a string from separate inputs. LISP's/format function is very flexible, and in this case, it uses "~a~%~a~%~a" format string to create a result string with each "~a" getting replaced with the following arguments (title, url, selection), and "~%" adding a newline after each argument.

You can certainly emulate it in the first function too:

```lisp
(define-command-global pipe-selection-title-url ()
    "Old"
    (let* ((title (title (current-buffer)))
          (url (quri:render-uri (url (current-buffer))))
          (selection (ps-eval (ps:chain window (get-selection) (to-string))))
          (formatted-output
            (format nil "~a~%~a~%~a" title url selection)))
        (uiop:launch-program
            (list "sh" "-c"
                  (concatenate 'string
                               "echo "
                               "'" formatted-output "'"
                               " > /tmp/nyxt_selection_pipe")))))
```

In this emulated function, I have kept the call to `quri:render-uri` to ensure the URL object is correctly converted to a string. If the `url` function in your environment indeed returns a `string`, you can remove `quri:render-uri`. If it returns an URL object depending on the Nyxt version or config, you should add an error handling there. 

However, note that this script writes all the information into one file `/tmp/nyxt_selection_pipe`. If you want to keep the output in separate files as in the first function, you would need to adjust the script accordingly.

<details><summary>Metadata</summary>

- Duration: 37832 ms
- Datetime: 2023-10-24T15:33:33.597952
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

