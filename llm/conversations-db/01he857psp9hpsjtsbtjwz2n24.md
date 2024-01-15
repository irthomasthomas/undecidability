**Prompt:**
diff --git a/nyxt/get-current-url-from-nyxt.sh b/nyxt/get-current-url-from-nyxt.sh
new file mode 100644
index 0000000..46a8efd
--- /dev/null
+++ b/nyxt/get-current-url-from-nyxt.sh
@@ -0,0 +1,28 @@
+#!/bin/bash
+
+# Define the path of the named pipe file
+pipe_file="/tmp/nyxt_pipe"
+
+# Create a named pipe at the specified path
+mkfifo "$pipe_file"
+
+# # Run Nyxt browser in remote mode, execute a Lisp expression to print the URL of the current buffer to the named pipe, and then quit Nyxt
+
+nyxt -r -e "(let* ((url (url (current-buffer)))
+                   (formatted-output
+                    (format nil \"~a\" url)))
+              (uiop:launch-program
+                (list \"sh\" \"-c\"
+                    (concatenate 'string
+                                 \"echo \"
+                                 \"'\" formatted-output \"'\"
+                                 \" > /tmp/nyxt_pipe\"))))" -q
+
+# Set a trap to remove the named pipe file when the script exits
+# trap "rm -f $pipe_file" EXIT
+
+# Read the URL from the named pipe and store it in a variable
+url=$(cat "$pipe_file")
+
+# Print the URL
+echo "The URL is: $url"


**Response:**
Add script to get current URL from Nyxt browser

<details><summary>Metadata</summary>

- Duration: 9075 ms
- Datetime: 2023-11-02T13:58:07.554000
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

