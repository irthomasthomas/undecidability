**Prompt:**
user:Open a file from the filesystem.
assistant:(define-command-global open-file
(&key
 (default-directory
  (if (quri.uri.file:uri-file-p (url (current-buffer)))
      (uiop/pathname:pathname-directory-pathname
       (quri.uri:uri-path (url (current-buffer))))
      *default-pathname-defaults*)))
"Open a file from the filesystem.
The user is prompted with the prompt buffer, files are browsable with
fuzzy suggestion."
(prompt :prompt "Open file" :extra-modes 'file-manager-mode :input
        (uiop/filesystem:native-namestring default-directory) :sources
        'open-file-source))


user:Return the list of tags of the bookmark corresponding to URL.
assistant:(defun url-bookmark-tags (url)
"Return the list of tags of the bookmark corresponding to URL."
(let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
(alexandria:when-let ((existing
                       (find url bookmarks :key #'url :test #'url-equal)))
  (tags existing))))


user:Summarize the current buffer by creating a new summary buffer.
assistant:(define-command-global summarize-buffer
(&key (summary-length 5) (buffer (current-buffer)))
"Summarize the current buffer by creating a new summary buffer."
(buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                summary-length :id (id buffer)))

user:Inspect a mode and show it in a help buffer.
assistant:(define-command-global describe-mode
(&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
"Inspect a mode and show it in a help buffer."
(when mode (describe-class :class mode)))



user:A function generator that returns a function suitable to be a `completion-function' of `search-engine'
(export-always 'make-search-completion-function)
(-> make-search-completion-function
    (&key (:base-url string)
          (:request-function (function (string &rest list) t))
          (:request-args list)
          (:processing-function (function (t) (list-of string))))
    (function (string) (list-of string)))
(defun make-search-completion-function (&key base-url
                                          (request-function
                                          #'(lambda (url &rest args)
                                              (handler-case (apply #'dex:get url args)
                                                (usocket:ns-host-not-found-error ()
                                                  (echo-warning "There's no Internet connection to make search completion")
                                                  nil))))
                                          request-args
                                          (processing-function (lambda (data) (coerce (j:decode data) 'list))))
  "Return a function suitable to be a `completion-function' of `search-engine'.


user:Tor-proxied completion function for Wikipedia.
(make-search-completion-function
:base-url \"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=~a\"
:processing-function (compose #'second #'njson:decode)
:request-args '(:proxy \"socks5://localhost:9050\"))"
  #'(lambda (input)
      (funcall processing-function
              (apply request-function
                      (cons (format nil base-url (quri:url-encode input))
                            request-args)))))

                            
user:2023 - A basic function to show the raw result from https://api.github.com/repos/irthomasthomas/undecidability/labels
assistant:


**Response:**
```lisp
(define-command-global show-github-repo-labels ()
  "Fetch and show the raw JSON result from the GitHub API for the labels of a specific repository."
  (let ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels"))
    (echo "Fetching labels...")
    (dex:get url
             :headers '(("User-Agent" . "Nyxt"))
             :callback (lambda (data)
                         (let ((buffer (make-buffer :title "*github-repo-labels*")))
                           (with-current-buffer buffer
                             (setf (source buffer) (make-instance 'base-source
                                                                  :buffer buffer))
                             (insert data)
                             (setf mode-list (list (make-instance 'base-mode))))
                           (switch-buffer :buffer buffer)))
             :error-callback (lambda (condition)
                               (echo "Error fetching GitHub labels: ~a" condition)))))
```

This function, `show-github-repo-labels`, will make an HTTP GET request to the GitHub API for the labels of the repository "irthomasthomas/undecidability" and display the raw JSON result in a new buffer. It uses the `dex:get` function to perform the request, specifying a User-Agent header as required by the GitHub API. The response data is inserted into a new buffer, which is then displayed to the user. If there is an error during the request, an error message is displayed instead.

<details><summary>Metadata</summary>

- Duration: 27677 ms
- Datetime: 2023-12-06T13:54:58.858935
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
<INFO> [13:57:24] Fetching labels...
<WARN> [13:57:24] Warning: Error on separate thread: Unknown &amp;KEY argument: :CALLBACK

**Response:**
I apologize for the oversight. It seems there might have been a change in the API or an error in the code snippet where `:callback` and `:error-callback` are not recognized as valid keywords. Let's correct the function by removing the erroneous keywords and handling the response in the main thread:

```lisp
(define-command-global show-github-repo-labels ()
  "Fetch and show the raw JSON result from the GitHub API for the labels of a specific repository."
  (let ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
        (buffer (make-buffer :title "*github-repo-labels*")))
    (echo "Fetching labels...")
    (handler-case
        (with-result (response (dex:get url :headers '(("User-Agent" . "Nyxt"))))
          (with-current-buffer buffer
            (setf (source buffer) (make-instance 'base-source :buffer buffer))
            (insert (cl-json:decode-json-from-string (dex:payload response)))
            (setf mode-list (list (make-instance 'base-mode)))
            (switch-buffer :buffer buffer)))
      (error (condition)
        (echo "Error fetching GitHub labels: ~a" condition)))))
```

In this function, we're using the `handler-case` to handle any potential errors from the `dex:get` request synchronously. If there's an error, an error message will be displayed using `echo`. Otherwise, the buffer will be updated with the parsed JSON data, and then the buffer will switch to display the results.

<details><summary>Metadata</summary>

- Duration: 29363 ms
- Datetime: 2023-12-06T13:58:03.519634
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

