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

                            
user:2023 - A basic function to save  https://api.github.com/repos/irthomasthomas/undecidability/labels
assistant:


**Response:**
```lisp
(define-command-global save-github-labels ()
  "Save the JSON data from the GitHub API for the labels of the repository 'irthomasthomas/undecidability'."
  (let* ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
         (path (merge-pathnames (make-pathname :name "github-labels"
                                               :type "json")
                                (uiop:getcwd))))
    (dex:get url
             :callback (lambda (data)
                         (when data
                           (with-open-file (stream path
                                                   :direction :output
                                                   :if-exists :supersede
                                                   :if-does-not-exist :create)
                             (write-sequence data stream))
                           (echo "Saved GitHub labels to ~a" path))))))

(save-github-labels)
```

This function, `save-github-labels`, will make a GET request to the specified GitHub API URL to fetch the labels for the repository 'irthomasthomas/undecidability'. It will then save the JSON response to a file named "github-labels.json" in the current working directory. The `dex:get` function is used to perform the HTTP request, and the `:callback` lambda function handles the response data by writing it to a file. The `echo` function is used to output a message indicating the save location of the file.

<details><summary>Metadata</summary>

- Duration: 20447 ms
- Datetime: 2023-12-06T14:11:44.341020
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

