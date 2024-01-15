**Prompt:**
diff --git a/llm/templates/nyxt-instruct-v1.yaml b/llm/templates/nyxt-instruct-v1.yaml
deleted file mode 100644
index f0aa158..0000000
--- a/llm/templates/nyxt-instruct-v1.yaml
+++ /dev/null
@@ -1,43 +0,0 @@
-prompt: |
-    user:Open a file from the filesystem.
-    The user is prompted with the prompt buffer, files are browsable with
-    fuzzy suggestion.
-    assistant:(define-command-global open-file
-    (&key
-     (default-directory
-      (if (quri.uri.file:uri-file-p (url (current-buffer)))
-          (uiop/pathname:pathname-directory-pathname
-           (quri.uri:uri-path (url (current-buffer))))
-          *default-pathname-defaults*)))
-    "Open a file from the filesystem.
-    The user is prompted with the prompt buffer, files are browsable with
-    fuzzy suggestion."
-    (prompt :prompt "Open file" :extra-modes 'file-manager-mode :input
-            (uiop/filesystem:native-namestring default-directory) :sources
-            'open-file-source))
-
-
-    user:Return the list of tags of the bookmark corresponding to URL.
-    assistant:(defun url-bookmark-tags (url)
-    "Return the list of tags of the bookmark corresponding to URL."
-    (let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
-    (alexandria:when-let ((existing
-                           (find url bookmarks :key #'url :test #'url-equal)))
-      (tags existing))))
-
-
-    user:Summarize the current buffer by creating a new summary buffer.
-    assistant:(define-command-global summarize-buffer
-    (&key (summary-length 5) (buffer (current-buffer)))
-    "Summarize the current buffer by creating a new summary buffer."
-    (buffer-load-internal-page-focus 'summarize-buffer :summary-length
-                                    summary-length :id (id buffer)))
-
-    user:Inspect a mode and show it in a help buffer.
-    assistant:(define-command-global describe-mode
-    (&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
-    "Inspect a mode and show it in a help buffer."
-    (when mode (describe-class :class mode)))
-
-    user:$input
-    assistant:
diff --git a/llm/templates/nyxt-instruct-v2.yaml b/llm/templates/nyxt-instruct-v2.yaml
deleted file mode 100644
index 2c88fdf..0000000
--- a/llm/templates/nyxt-instruct-v2.yaml
+++ /dev/null
@@ -1,83 +0,0 @@
-prompt: |
-    user:Command to send selection to named pipe.
-    assistant:(define-command-global pipe-selection ()
-    "Send selection to named pipe"
-    (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
-        (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" selection "'" " > /tmp/nyxt_selection_pipe")))))
-
-
-    user:Send url, title and selection to new linux pipe
-    assistant:(define-command-global pipe-selection-title-url-new ()
-    "Sends url to new gh issue"
-    (let* (myurl (url (current-buffer)))
-            (pipe-url "/tmp/nyxt_url"))
-        (with-open-file (stream pipe-url
-                            :direction :output
-                            :if-exists :supersede
-                            :if-does-not-exist :create)
-        (write-string (render-url myurl) stream))
-        (write-string selection stream))))
-
-
-    user:Return the list of tags of the bookmark corresponding to URL.
-    assistant:(defun url-bookmark-tags (url)
-    "Return the list of tags of the bookmark corresponding to URL."
-    (let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
-    (alexandria:when-let ((existing
-                           (find url bookmarks :key #'url :test #'url-equal)))
-      (tags existing))))
-
-
-    user:Function to summarize the current buffer by creating a new summary buffer.
-    assistant:(define-command-global summarize-buffer
-    (&key (summary-length 5) (buffer (current-buffer)))
-    "Summarize the current buffer by creating a new summary buffer."
-    (buffer-load-internal-page-focus 'summarize-buffer :summary-length
-                                    summary-length :id (id buffer)))
-
-
-    user:Command to inspect a mode and show it in a help buffer.
-    assistant:(define-command-global describe-mode
-    (&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
-    "Inspect a mode and show it in a help buffer."
-    (when mode (describe-class :class mode)))
-
-
-    user: Function to spell check a word.
-    assistant:(define-command spell-check-word
-        (&key (word nil word-supplied-p))
-    "Spell check a word."
-    (let ((word
-            (or (and word-supplied-p word)
-                (prompt1 :prompt "Spell check word" :sources
-                        'prompter:raw-source))))
-        (if (spell-dict-check-p word)
-            (echo "~s is spelled correctly." word)
-            (echo "~s is NOT correctly spelled." word))))
-
-
-    user:Prompt for element hints and bookmark them.
-    assistant:(define-command bookmark-hint
-    nil
-    "Prompt for element hints and bookmark them."
-    (nyxt/mode/hint:query-hints "Bookmark hint"
-                                (lambda (result)
-                                    (dolist (url (mapcar #'url result))
-                                    (let ((tags
-                                            (prompt :prompt "Tag(s)" :sources
-                                                    (list
-                                                    (make-instance
-                                                    'prompter:word-source :name
-                                                    "New tags" :enable-marks-p
-                                                    t)
-                                                    (make-instance 'tag-source
-                                                                    :marks
-                                                                    (url-bookmark-tags
-                                                                    url))))))
-                                        (bookmark-add url :tags tags :title
-                                                    (fetch-url-title url)))))
-                                :selector "a"))
-
-
-    user:$input
-    assistant:
diff --git a/llm/templates/nyxt-instruct-v3.yaml b/llm/templates/nyxt-instruct-v3.yaml
deleted file mode 100644
index d570e12..0000000
--- a/llm/templates/nyxt-instruct-v3.yaml
+++ /dev/null
@@ -1,75 +0,0 @@
-prompt: |
-    User:Open a file from the filesystem.
-    Response:(define-command-global open-file
-    (&key
-     (default-directory
-      (if (quri.uri.file:uri-file-p (url (current-buffer)))
-          (uiop/pathname:pathname-directory-pathname
-           (quri.uri:uri-path (url (current-buffer))))
-          *default-pathname-defaults*)))
-    "Open a file from the filesystem.
-    The user is prompted with the prompt buffer, files are browsable with
-    fuzzy suggestion."
-    (prompt :prompt "Open file" :extra-modes 'file-manager-mode :input
-            (uiop/filesystem:native-namestring default-directory) :sources
-            'open-file-source))
-
-
-    User:Return the list of tags of the bookmark corresponding to URL.
-    Response:(defun url-bookmark-tags (url)
-    "Return the list of tags of the bookmark corresponding to URL."
-    (let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
-    (alexandria:when-let ((existing
-                           (find url bookmarks :key #'url :test #'url-equal)))
-      (tags existing))))
-
-
-    User:Summarize the current buffer by creating a new summary buffer.
-    Response:(define-command-global summarize-buffer
-    (&key (summary-length 5) (buffer (current-buffer)))
-    "Summarize the current buffer by creating a new summary buffer."
-    (buffer-load-internal-page-focus 'summarize-buffer :summary-length
-                                    summary-length :id (id buffer)))
-
-    User:Inspect a mode and show it in a help buffer.
-    Response:(define-command-global describe-mode
-    (&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
-    "Inspect a mode and show it in a help buffer."
-    (when mode (describe-class :class mode)))
-
-    
-
-    User:A function generator that returns a function suitable to be a `completion-function' of `search-engine'
-    (export-always 'make-search-completion-function)
-    (-> make-search-completion-function
-        (&key (:base-url string)
-              (:request-function (function (string &rest list) t))
-              (:request-args list)
-              (:processing-function (function (t) (list-of string))))
-        (function (string) (list-of string)))
-    (defun make-search-completion-function (&key base-url
-                                              (request-function
-                                              #'(lambda (url &rest args)
-                                                  (handler-case (apply #'dex:get url args)
-                                                    (usocket:ns-host-not-found-error ()
-                                                      (echo-warning "There's no Internet connection to make search completion")
-                                                      nil))))
-                                              request-args
-                                              (processing-function (lambda (data) (coerce (j:decode data) 'list))))
-      "Return a function suitable to be a `completion-function' of `search-engine'.
-
-    
-    User:Tor-proxied completion function for Wikipedia.
-    (make-search-completion-function
-    :base-url \"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=~a\"
-    :processing-function (compose #'second #'njson:decode)
-    :request-args '(:proxy \"socks5://localhost:9050\"))"
-      #'(lambda (input)
-          (funcall processing-function
-                  (apply request-function
-                          (cons (format nil base-url (quri:url-encode input))
-                                request-args)))))
-
-                                
-    User:$input
-    Response:
diff --git a/llm/templates/nyxt-instruct.yaml b/llm/templates/nyxt-instruct.yaml
index fa33e36..2c88fdf 100644
--- a/llm/templates/nyxt-instruct.yaml
+++ b/llm/templates/nyxt-instruct.yaml
@@ -1,43 +1,83 @@
 prompt: |
-    User:Open a file from the filesystem.
-    The user is prompted with the prompt buffer, files are browsable with
-    fuzzy suggestion.
-    Response:(define-command-global open-file
-    (&key
-     (default-directory
-      (if (quri.uri.file:uri-file-p (url (current-buffer)))
-          (uiop/pathname:pathname-directory-pathname
-           (quri.uri:uri-path (url (current-buffer))))
-          *default-pathname-defaults*)))
-    "Open a file from the filesystem.
-    The user is prompted with the prompt buffer, files are browsable with
-    fuzzy suggestion."
-    (prompt :prompt "Open file" :extra-modes 'file-manager-mode :input
-            (uiop/filesystem:native-namestring default-directory) :sources
-            'open-file-source))
-
-    User:Return the list of tags of the bookmark corresponding to URL.
-    Response:(defun url-bookmark-tags (url)
+    user:Command to send selection to named pipe.
+    assistant:(define-command-global pipe-selection ()
+    "Send selection to named pipe"
+    (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
+        (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" selection "'" " > /tmp/nyxt_selection_pipe")))))
+
+
+    user:Send url, title and selection to new linux pipe
+    assistant:(define-command-global pipe-selection-title-url-new ()
+    "Sends url to new gh issue"
+    (let* (myurl (url (current-buffer)))
+            (pipe-url "/tmp/nyxt_url"))
+        (with-open-file (stream pipe-url
+                            :direction :output
+                            :if-exists :supersede
+                            :if-does-not-exist :create)
+        (write-string (render-url myurl) stream))
+        (write-string selection stream))))
+
+
+    user:Return the list of tags of the bookmark corresponding to URL.
+    assistant:(defun url-bookmark-tags (url)
     "Return the list of tags of the bookmark corresponding to URL."
     (let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
     (alexandria:when-let ((existing
                            (find url bookmarks :key #'url :test #'url-equal)))
       (tags existing))))
 
-    User:Summarize the current buffer by creating a new summary buffer.
-    SUMMARY-LENGTH allows to list more/less summary items.
-    Response:(define-command-global summarize-buffer
+
+    user:Function to summarize the current buffer by creating a new summary buffer.


**Response:**
(define-command-global summarize-buffer
     (&key (summary-length 5) (buffer (current-buffer)))
     "Summarize the current buffer by creating a new summary buffer."
     (buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                     summary-length :id (id buffer)))
 
-    User:Inspect a mode and show it in a help buffer.
-    Response:(define-command-global describe-mode
+    user:Command to inspect a mode and show it in a help buffer.

<details><summary>Metadata</summary>

- Duration: 5221 ms
- Datetime: 2023-12-12T20:24:24.098286
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

