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

                            
user:(defun save-github-labels ()
  "Save the labels of the repository https://api.github.com/repos/irthomasthomas/undecidability/labels."
  (let* ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
         (response (dex:get url)))
    (with-open-file (file "labels.txt" :direction :output)
      (format file "~a" response))))

This return a file content like:
[{"id":5935764687,"node_id":"LA_kwDOKNgf3c8AAAABYcyUzw","url":"https://api.github.com/repos/irthomasthomas/undecidability/labels/Agents","name":"Agents","color":"fef2c0","default":false,"description":"Autonomous AI agents using LLMs"},{"id":5976028723,"node_id":"LA_kwDOKNgf3c8AAAABZDL2Mw","url":"https://api.github.com/repos/irthomasthomas/undecidability/labels/Algorithms","name":"Algorithms","color":"bfd4f2","default":false,"description":"Sorting, Learning or Classifying. All algorithms go here."}]

Create a list of labels from this and save them to a slot in nyxt
assistant:


**Response:**
(defun save-github-labels ()
  "Save the labels of the repository https://api.github.com/repos/irthomasthomas/undecidability/labels."
  (let* ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
         (response (dex:get url))
         (labels (alexandria:map 'list (lambda (label) (gethash "name" label)) response))
         (local-labels (getf nyxt-buffer:url-data :github-labels)))
    (setf (getf nyxt-buffer:url-data :github-labels) (append local-labels labels))
    (with-open-file (file "labels.txt" :direction :output)
      (format file "~a" response)))))

(save-github-labels)

<details><summary>Metadata</summary>

- Duration: 5372 ms
- Datetime: 2023-12-06T14:15:08.761119
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

