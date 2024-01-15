**Prompt:**
User:Open a file from the filesystem.

The user is prompted with the prompt buffer, files are browsable with
fuzzy suggestion.
Response:(define-command-global open-file
(&key
 (default-directory
  (if (quri.uri.file:uri-file-p (url (current-buffer)))
      (uiop/pathname:pathname-directory-pathname
       (quri.uri:uri-path (url (current-buffer))))
      *default-pathname-defaults*)))
"Open a file from the filesystem.

The user is prompted with the prompt buffer, files are browsable with
fuzzy suggestion.

DEFAULT-DIRECTORY specifies which directory to start from. Defaults to user home
directory.

By default, it uses the `xdg-open' command. The user can override the
`open-file-function' of `file-source' which takes the filename (or
directory name) as parameter.

`file-source' also has `supported-media-types'. You can append new types to
it. Every type in `supported-media-types' will be opened directly in Nyxt."
(prompt :prompt "Open file" :extra-modes 'file-manager-mode :input
        (uiop/filesystem:native-namestring default-directory) :sources
        'open-file-source))

User:Return the list of tags of the bookmark corresponding to URL.
Response:(defun url-bookmark-tags (url)
"Return the list of tags of the bookmark corresponding to URL."
(let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
(alexandria:when-let ((existing
                       (find url bookmarks :key #'url :test #'url-equal)))
  (tags existing))))
User:Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items.
Response:(define-command-global summarize-buffer
(&key (summary-length 5) (buffer (current-buffer)))
"Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items."
(buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                summary-length :id (id buffer)))
User:Inspect a mode and show it in a help buffer.
Response:(define-command-global describe-mode
(&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
"Inspect a mode and show it in a help buffer."
(when mode (describe-class :class mode)))
User:Function caches and displays list of labels from https://api.github.com/repos/irthomasthomas/undecidability/labels 
Response:


**Response:**
```lisp
(define-configuration buffer
  ((default-modes (append '(auto-mode) %slot-default%))))

(defvar *github-labels-cache* (make-hash-table :test 'equal)
  "Cache for storing GitHub labels.")

(defun fetch-github-labels (repository)
  "Fetch GitHub labels for the given REPOSITORY."
  (let ((url (format nil "https://api.github.com/repos/~a/labels" repository)))
    (if (gethash url *github-labels-cache*)
        (gethash url *github-labels-cache*)
        (let ((response (dex:get url :headers '(("User-Agent" . "Nyxt")))))
          (when (eq (dex:status-code response) 200)
            (let ((labels (mapcar (lambda (label)
                                    (gethash "name" label))
                                  (json:decode-json-from-source (dex:body response)))))
              (setf (gethash url *github-labels-cache*) labels)
              labels))))))

(define-command-global display-github-labels ()
  "Display GitHub labels for the repository 'irthomasthomas/undecidability'."
  (let ((labels (fetch-github-labels "irthomasthomas/undecidability")))
    (if labels
        (with-result (buffer (make-buffer :title "GitHub Labels"))
          (with-data-access (buffer)
            (setf (body buffer)
                  (markup:markup
                   (:html
                    (:head
                     (:title "GitHub Labels"))
                    (:body
                     (:h1 "GitHub Labels")
                     (:ul
                      (loop for label in labels
                            collect (markup:markup (:li label)))))))))
          (switch-buffer :buffer buffer))
        (echo "Failed to fetch GitHub labels."))))
```

This function defines a command `display-github-labels` that fetches and displays the list of labels from the GitHub repository "irthomasthomas/undecidability". It uses a cache to store the labels and avoid fetching them multiple times. If the labels are successfully fetched, they are displayed in a new buffer. If the fetch fails, an error message is displayed.

<details><summary>Metadata</summary>

- Duration: 27625 ms
- Datetime: 2023-11-28T14:16:49.441432
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

**Prompt:**
Error on separate thread: Symbol &quot;STATUS-CODE&quot; not found in the DEXADOR package. Stream: #&lt;dynamic-extent STRING-INPUT-STREAM (unavailable) from &quot;(define-...&quot;&gt;

**Response:**
I apologize for the oversight. It seems the `dex:status-code` function is not available, and I mistakenly referenced `DEXADOR` assuming it was a package in Nyxt. Please find the corrected function below, which uses the `dex:get` function correctly:

```lisp
(defvar *github-labels-cache* (make-hash-table :test 'equal)
  "Cache for storing GitHub labels.")

(defun fetch-github-labels (repository)
  "Fetch GitHub labels for the given REPOSITORY."
  (flet ((extract-name (label)
           (gethash "name" label)))
    (let ((url (format nil "https://api.github.com/repos/~a/labels" repository)))
      (if-let ((cached-labels (gethash url *github-labels-cache*)))
          cached-labels
          (let ((response (ignore-errors (dex:get url :headers '(("User-Agent" . "Nyxt"))))))
            (if response
                (let ((labels (mapcar #'extract-name (json:decode-json-from-source (dex:body response)))))
                  (setf (gethash url *github-labels-cache*) labels)
                  labels)
                (warn "Failed to fetch GitHub labels for ~a" url)
                nil))))))

(define-command-global display-github-labels ()
  "Display GitHub labels for the repository 'irthomasthomas/undecidability'."
  (let ((labels (fetch-github-labels "irthomasthomas/undecidability")))
    (if labels
        (with-result (buffer (make-buffer :title "GitHub Labels"))
          (with-data-access (buffer)
            (setf (body buffer)
                  (markup:markup
                   (:html
                    (:head
                     (:title "GitHub Labels"))
                    (:body
                     (:h1 "GitHub Labels")
                     (:ul
                      (loop for label in labels
                            collect (markup:markup (:li label)))))))))
          (switch-buffer :buffer buffer))
        (echo "Failed to fetch GitHub labels."))))
```

This corrected version should work without the erroneous `dex:status-code` reference, and instead checks if the `response` is not `nil` to proceed with extracting and caching labels. If there's any error during the `dex:get` request, it will simply warn about the failure.

<details><summary>Metadata</summary>

- Duration: 37042 ms
- Datetime: 2023-11-28T14:43:09.840633
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
Warning: Error on separate thread: The symbol &quot;BODY&quot; is not external in the DEXADOR package. Stream: #&lt;dynamic-extent STRING-INPUT-STREAM (unavailable) from &quot;(defvar ...&quot;&gt;

**Response:**
I apologize for the previous confusion and the incorrect usage of DEXADOR's non-existing external symbols. In the Nyxt browser, the correct usage would typically involve Nyxt's own utilities for making HTTP requests, handling JSON, and rendering HTML pages. Below is the corrected and updated function for Nyxt version 3:

```lisp
(defvar *github-labels-cache* (make-hash-table :test 'equal)
  "Cache for storing GitHub labels.")

(defun fetch-github-labels (repository)
  "Fetch GitHub labels for the given REPOSITORY."
  (let ((url (format nil "https://api.github.com/repos/~a/labels" repository)))
    (or (gethash url *github-labels-cache*)
        (nyxt::with-data (rep (nyxt::get-json url :headers '(("User-Agent" . "Nyxt"))))
          (when rep
            (let ((labels (mapcar (lambda (label) (gethash "name" label)) rep)))
              (setf (gethash url *github-labels-cache*) labels)
              labels))))))

(define-command display-github-labels ()
  "Display GitHub labels for the repository 'irthomasthomas/undecidability'."
  (let ((labels (fetch-github-labels "irthomasthomas/undecidability")))
    (if labels
        (with-result (buffer (make-buffer :title "GitHub Labels"))
          (with-current-html-document (buffer)
            (markup:markup
             (:html
              (:head
               (:title "GitHub Labels"))
              (:body
               (:h1 "GitHub Labels")
               (:ul
                (loop for label in labels
                      collect (markup:markup (:li label)))))))))
      (echo "Failed to fetch GitHub labels"))))
```

This version uses `nyxt::get-json` to fetch the data and `nyxt::with-current-html-document` to render the HTML data within Nyxt. Please adjust this code if there are any deviations in the actual packages and functions available to your specific version of Nyxt.

<details><summary>Metadata</summary>

- Duration: 26385 ms
- Datetime: 2023-11-28T14:59:10.174809
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
Warning: Error on separate thread: Lock on package NYXT violated when interning WITH-DATA while in package NYXT-USER.
See also:
  The SBCL Manual, Node &quot;Package Locks&quot;
<WARN> [15:18:37] Warning: Error on separate thread: The function NYXT-USER::HTTP-REQUEST is undefined.

**Response:**
I apologize for the earlier confusion, and I appreciate your patience.

Nyxt has undergone significant changes since version 2, and in version 3, the package structure and available functions are different. The interning problem likely indicates an issue related to referencing functions that are either internal to the Nyxt package or have been changed in version 3.

Nyxt now uses our `cl-webkit` library to handle network requests. Please see the code below on how to properly retrieve and display the data from GitHub API:

```lisp
(defvar *github-labels-cache* (make-hash-table :test 'equal)
  "Cache for storing GitHub labels.")

(defun fetch-github-labels (repository)
  "Fetch GitHub labels for the given REPOSITORY."
  (let ((url (format nil "https://api.github.com/repos/~a/labels" repository)))
    (or (gethash url *github-labels-cache*)
        (multiple-value-bind (body status-code)
            (cl-webkit:http-get url :headers '(("User-Agent" . "Nyxt/User"))))
          (when (= 200 status-code)
            (let ((labels (mapcar (lambda (label) (gethash "name" label))
                                  (json:decode-json-from-string body))))
              (setf (gethash url *github-labels-cache*) labels)
              labels))))))

(define-command display-github-labels ()
  "Display GitHub labels for the repository 'irthomasthomas/undecidability'."
  (let ((labels (fetch-github-labels "irthomasthomas/undecidability")))
    (if labels
        (with-result (buffer (make-buffer :title "GitHub Labels"))
          (with-html (buffer)
            (:html (:head (:title "GitHub Labels"))
                   (:body (:h1 "GitHub Labels")
                          (:ul (loop for label in labels
                                     collect (:li label)))))))
      (echo "Failed to fetch GitHub labels."))))
```

This function uses `cl-webkit:http-get` to perform the HTTP GET request, and `with-html` to prepare the HTML document within a new buffer.

Before using this function, make sure your Nyxt is built with `cl-webkit` support. You may also need to make modifications if your specific version of Nyxt browser has different APIs or requires some other adjustments.

As of my last update, I have no information on a function `http-request` for Nyxt browser version 3 or recent developments in newer versions. Make sure to double-check the latest documentation or inquire with the Nyxt maintainers for the most up-to-date APIs.

<details><summary>Metadata</summary>

- Duration: 27233 ms
- Datetime: 2023-11-28T15:19:02.714153
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

