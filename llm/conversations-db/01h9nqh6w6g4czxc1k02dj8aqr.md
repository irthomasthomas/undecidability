**Prompt:**
diff --git a/.github/workflows/issue_comment-claude.yml b/.github/workflows/issue_comment-claude.yml
new file mode 100644
index 0000000..e004b96
--- /dev/null
+++ b/.github/workflows/issue_comment-claude.yml
@@ -0,0 +1,28 @@
+name: Run Script
+
+on: 
+  issues:
+    types: [opened, labeled]
+
+jobs:
+
+  auto-reply:
+  
+    if: github.event.label.name == 'run_1'
+    
+    runs-on: ubuntu-latest
+
+    permissions:
+      issues: write
+    
+    steps:
+    
+      - name: Run Script
+        run: echo "Hello world" | tee script-output.txt
+        
+      - name: Post Comment
+        uses: actions/github-script@v3.1.0
+        script: |
+          const issue_number = context.issue.number;
+          const scriptOutput = readFileSync('script-output.txt', 'utf8').trim();
+          await github.issues.createComment({...context.repo, issue_number, body: scriptOutput});
diff --git a/.github/workflows/issue_comment-gpt4.yml b/.github/workflows/issue_comment-gpt4.yml
new file mode 100644
index 0000000..e322297
--- /dev/null
+++ b/.github/workflows/issue_comment-gpt4.yml
@@ -0,0 +1,41 @@
+name: Run Script
+on:
+   issues:
+    types: [opened, labeled]
+
+jobs:
+  auto-reply:
+    if: github.event.label.name == 'run_1'
+    runs-on: ubuntu-latest
+    permissions:
+        issues: write
+    steps:
+      - name: Checkout
+        uses: actions/checkout@v2
+      
+      - name: Setup GitHub CLI
+        uses: cli/setup-gh@v1
+
+      - name: Run Script
+        id: script
+        run: |
+          try {
+            output=$(./script.sh)
+            echo "::set-output name=result::$output"
+           } catch {
+           echo "The script failed to run"
+           output="An error has occurred while running the script."
+           }
+
+      - name: Post Comment
+        id: comment
+        uses: actions/github-script@v3.1.0
+        with:
+          github-token: ${{ secrets.GITHUB_TOKEN }}
+          script: |
+            const issue_number = context.issue.number;
+            const comments = await github.issues.listComments({...context.repo, issue_number});
+            const bot_comment_exists = comments.data.some(comment => comment.user.login === 'github-actions[bot]' && comment.body.includes('Your output text here'));
+            if (!bot_comment_exists) {
+              await github.issues.createComment({...context.repo, issue_number, body: '${{steps.script.outputs.result}}'});
+            }


**Response:**
Add issue comment workflows for running scripts and posting comments.

<details><summary>Metadata</summary>

- Duration: 1457 ms
- Datetime: 2023-09-06T17:09:39.412229
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

