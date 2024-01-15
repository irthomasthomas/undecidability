**Prompt:**
Write a perfect commit message for: diff --git a/.aider.chat.history.md b/.aider.chat.history.md
new file mode 100644
index 0000000..ab5b238
--- /dev/null
+++ b/.aider.chat.history.md
@@ -0,0 +1,8 @@
+
+# aider chat started at 2023-07-16 18:58:46
+
+> Aider v0.9.0  
+> /home/thomas/.venv/bin/aider helpmecode.py server.py Socket.ahk  
+> Model: gpt-4  
+> Files not tracked in .git:  
+> - helpmecode.py  
diff --git a/helpmecode.py b/helpmecode.py
new file mode 100644
index 0000000..5447478
--- /dev/null
+++ b/helpmecode.py
@@ -0,0 +1,23 @@
+import socket
+import autokey
+
+ipAddress = "192.168.0.3"  # ENTER YOUR IP FROM THE PYTHON SCREEN
+
+myTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+try:
+    myTcp.connect((ipAddress, 8337))
+except Exception as e:
+    print("Either the python server is inaccessible, or you did not edit this script to include its lan IP")
+    exit()
+
+print("Connected. Type helpme and your query in your editor.")
+
+def send_query(query):
+    command = "howdoi;" + query
+    myTcp.send(command.encode())
+    print("let me see ...")
+    return myTcp.recv(2048).decode()
+
+# Set up hotkey
+hotkey = autokey.Hotkey("helpme", send_query)
+hotkey.start()
diff --git a/tests/test_helpmecode.py b/tests/test_helpmecode.py
new file mode 100644
index 0000000..78448a7
--- /dev/null
+++ b/tests/test_helpmecode.py
@@ -0,0 +1,13 @@
+import unittest
+import newfile
+
+class TestNewfile(unittest.TestCase):
+    def setUp(self):
+        self.query = "how to write a python function"
+
+    def test_send_query(self):
+        response = newfile.send_query(self.query)
+        self.assertIsNotNone(response)
+
+if __name__ == '__main__':
+    unittest.main()
. Always keep it concise and brief!

**Response:**
Add new files for aider chat history, helpmecode.py, and test_helpmecode.py.

<details><summary>Metadata</summary>

- Duration: 1473 ms
- Datetime: 2023-07-16T17:59:16.927218
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

