**Prompt:**
diff --git a/llm/templates/nyxt-v2.yaml b/llm/templates/nyxt-v2.yaml
index ff4432a..f691664 100644
--- a/llm/templates/nyxt-v2.yaml
+++ b/llm/templates/nyxt-v2.yaml
@@ -1,8 +1,6 @@
 system: You are a system for returning new nxyt browser lisp functions for nyxt browser v3. Always reply with a compatible lisp function (BE CAREFUL. Think step by step.).
 prompt: |
     user:Open a file from the filesystem.
-    The user is prompted with the prompt buffer, files are browsable with
-    fuzzy suggestion.
     assistant:(define-command-global open-file
     (&key
      (default-directory
@@ -33,13 +31,19 @@ prompt: |
     "Summarize the current buffer by creating a new summary buffer."
     (buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                     summary-length :id (id buffer)))
-
-    user:Inspect a mode and show it in a help buffer.
-    assistant:(define-command-global describe-mode
-    (&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
-    "Inspect a mode and show it in a help buffer."
-    (when mode (describe-class :class mode)))
-
+                                    
     
+    user:Tor-proxied completion function for Wikipedia.
+    (make-search-completion-function
+    :base-url \"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=~a\"
+    :processing-function (compose #'second #'njson:decode)
+    :request-args '(:proxy \"socks5://localhost:9050\"))"
+      #'(lambda (input)
+          (funcall processing-function
+                  (apply request-function
+                          (cons (format nil base-url (quri:url-encode input))
+                                request-args)))))
+
+                                
     user:$input
     assistant:
diff --git a/llm/templates/nyxt-v3.yaml b/llm/templates/nyxt-v3.yaml
deleted file mode 100644
index 121bdd3..0000000
--- a/llm/templates/nyxt-v3.yaml
+++ /dev/null
@@ -1,76 +0,0 @@
-system: You are a system for returning new nxyt browser lisp functions for nyxt browser v3. Always reply with a compatible lisp function (BE CAREFUL. Think step by step.).
-prompt: |
-    user:Open a file from the filesystem.
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
-    
-
-    user:A function generator that returns a function suitable to be a `completion-function' of `search-engine'
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
-    user:Tor-proxied completion function for Wikipedia.
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
-    user:$input
-    assistant:
diff --git a/llm/templates/nyxt-v4.yaml b/llm/templates/nyxt-v4.yaml
deleted file mode 100644
index f691664..0000000
--- a/llm/templates/nyxt-v4.yaml
+++ /dev/null
@@ -1,49 +0,0 @@
-system: You are a system for returning new nxyt browser lisp functions for nyxt browser v3. Always reply with a compatible lisp function (BE CAREFUL. Think step by step.).
-prompt: |
-    user:Open a file from the filesystem.
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
-    
-    user:Tor-proxied completion function for Wikipedia.
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
-    user:$input
-    assistant:


**Response:**
Remove nyxt-v3.yaml and nyxt-v4.yaml templates

<details><summary>Metadata</summary>

- Duration: 1087 ms
- Datetime: 2023-12-12T20:30:19.021283
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

