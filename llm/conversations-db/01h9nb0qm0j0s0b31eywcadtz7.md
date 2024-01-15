**Prompt:**
diff --git a/shell_functions.sh b/shell_functions.sh
index ec5faee..8cb911a 100644
--- a/shell_functions.sh
+++ b/shell_functions.sh
@@ -1,7 +1,4 @@
-##############################################################################################################################
-##############################################################################################################################
-##############################################################################################################################
-##############################################################################################################################
+
 # LLM stuff
 echo "FUNCTION CALLING"
 echo "FUNCTION CALLING"
@@ -126,9 +123,7 @@ commit() {
   [[ ! -z "$msg" ]] && git commit -m "$msg"
 
     while true; do
-      #     msg="$(llm -t commit335 -p comm1 $(git diff --cached | llm -t commit135 -o temperature 0.3) -p comm2 $(git diff --cached | llm -t commit135 -o temperature 0.3) -p comm3 $(git diff --cached | llm -t commit135 -o temperature 0.3))"
-
-      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached)") # -m 3.5-16k
+      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached | ttok -t 3000)") # -m 3.5-16k
       echo "Commit Msg: "$msg""
       echo "Confirm push to repo? [y] or regenerate msg? [n]"
       read confirm
@@ -223,26 +218,16 @@ did() {
   echo "$1" >> "/$HOME/DONE.txt"
 }
 
-get_current_activity() {
-  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
-  active_activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
-  echo $active_activity_id
-}
-
-get_current_activity_name() {
-  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
-  active_activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
-  echo $active_activity_name
-}
+current_activity_id() {
+  qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity
+  }
 
-get_activity_name() {
-  # This function fetches the name of the activity with id passed as parameter
-  # $1 - Activity id
+activity_name_from_id() {
+  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$1"
+  }
 
-  activity_id="$1"
-  activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$activity_id")
-  echo $activity_name
-}
+# get_current_activity_name()
+# get_activity_name()
 
 cnttkn() {
   # ToDo: Deprecate this for simonw's ttok.


**Response:**
Refactor shell_functions.sh: remove unnecessary code and update function names.

<details><summary>Metadata</summary>

- Duration: 1487 ms
- Datetime: 2023-09-06T13:30:56.559592
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

**Prompt:**
1: Yes. \n
2: Activities are a way to have multiple Plasma setups, with each a different set of widgets and themes. Some activities can be private. Such activities do not track your actions. For example, they do not track what recent document you opened.\n2A: Functions - current_activity_id() {
  qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity
  }

activity_name_from_id() {
  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$1"
  }
\n\n
3: Yes, git, and the github cli gh. On activity change, if not HOME/MyRepos/$Activity_name, prompt user to clone a repo. Or, if the user has already cloned a repo in another dir, ask if they want to move that repo folder into Managed Repos, or Download a new copy. If move, also make symlink so that links to old path dont break.
\n\n
4. Terminal: That would be a good start. \n
5..@ Your last message cut off here, and I did not see question 5 on.

**Response:**
Refactor shell_functions.sh: remove unnecessary code and update function names. These changes simplify the script and improve readability.

<details><summary>Metadata</summary>

- Duration: 2297 ms
- Datetime: 2023-09-06T14:08:16.198129
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

