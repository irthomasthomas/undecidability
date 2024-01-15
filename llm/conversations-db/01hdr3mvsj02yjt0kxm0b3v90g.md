**Prompt:**
 
Error on separate thread: The value
  #&lt;QURI.URI.HTTP:URI-HTTPS https://stackoverflow.com/questions/42233232/using-scikit-learn-to-classify-multiple-outputs-of-banking-transactions?rq=3&gt;

is not of type
  VECTOR
when binding #:N-ARRAY31


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
The error message suggests that there is a type mismatch when binding the value `#:N-ARRAY31`. It seems like `#:N-ARRAY31` is expected to be of type `VECTOR`, but the actual value provided is a URI object.

To resolve this issue, you need to ensure that `#:N-ARRAY31` is a vector before binding it. You can use the `vector` function to convert the URI object to a vector. Here's an updated version of the code:

```lisp
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
      (write-string selection stream))
    (let ((vectorized-uri (vector url))) ; Convert URI to vector
      ;; Use vectorized-uri as needed
      )))
```

Make sure to replace `;; Use vectorized-uri as needed` with the appropriate code that uses the vectorized URI object.

<details><summary>Metadata</summary>

- Duration: 35570 ms
- Datetime: 2023-10-27T08:22:04.094948
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

