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
To create a function in Nyxt browser that caches and displays a list of labels from a GitHub repository, you would need to use Nyxt's Common Lisp environment to make an HTTP request to the GitHub API, parse the JSON response, and then display the results in a buffer. Here's an example of how you might define such a function:

```lisp
(define-command-global fetch-and-display-github-labels ()
  "Fetches and displays list of labels from a GitHub repository."
  (let ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels"))
    (nyxt::with-data-unsafe (response (dex:get url))
      (when (eq (dex:status-code response) 200)
        (let ((labels-json (dex:body-as-json response)))
          (if labels-json
              (let ((labels (mapcar (lambda (label)
                                       (gethash "name" label))
                                     labels-json)))
                (with-result-buffer ((title "GitHub Labels"))
                  (markup:markup
                   (:h1 "Labels")
                   (:ul (loop for label in labels
                              do (markup:markup (:li label))))))
              (echo "Failed to parse GitHub labels.")))))))
```

This function uses the `dex:get` function from the `dexador` HTTP client library to make a GET request to the specified URL. It then checks the response status code and, if successful, parses the JSON response body to extract the label names. These names are then displayed in a new result buffer.

Please note that this example assumes you have the `dexador` library available in your Nyxt environment and that you have defined the necessary helper functions like `with-data-unsafe`, `with-result-buffer`, and `echo`. You may need to adapt the code to fit the actual Nyxt environment and the libraries you have installed.

<details><summary>Metadata</summary>

- Duration: 33858 ms
- Datetime: 2023-11-28T14:12:12.657347
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.3}
```

