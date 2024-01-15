**Prompt:**
diff --git a/github_issues.sh b/github_issues.sh
index 5fbb3ba..13a9249 100755
--- a/github_issues.sh
+++ b/github_issues.sh
@@ -6,41 +6,44 @@ send_note_to_github() {
     local TITLE="$1"
     local URL="$2"
     local DESCRIPTION="$3"
+    local labels="$4"
+    local gh_markdown_highlight_generated_labels="$5"
     local BODY
     local task_list
-    local labels_csv
     local issue_url
+    local labels_csv
+    echo >&2
+    echo "send_note_to_github" >&2
+    echo "gh_markdown_highlight_generated_labels: $gh_markdown_highlight_generated_labels" >&2
 
+    echo >&2
     if [ -z "$TITLE" ]; then
         TITLE="$(llm "generate a title from this url:$URL:quote:$DESCRIPTION" -o temperature 0.1)"
     fi
-
+    
     task_list="- [ ] [${TITLE}](${URL})"
+    suggested_labels="#### Suggested labels
+#### $gh_markdown_highlight_generated_labels"
+    
     BODY="$task_list
 
-    $DESCRIPTION"
-    labels_csv=$(get_labels "$TITLE" "$URL" "$DESCRIPTION")
-    # print to stderr
-    echo "title: $TITLE
-url: $URL 
-description: $DESCRIPTION
-labels: $labels_csv
-" >&2
-    # issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")
-    # echo "$issue_url"
+$DESCRIPTION
+
+$suggested_labels"
+    labels_csv=$(echo "$labels" | tr '\n' ',' | sed 's/.$//')
+    echo "labels_csv: $labels_csv" >&2
+    
+    issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv" --web)
+    echo "$issue_url"
 }
 
 
-get_labels() {
+get_labels_json() {
     local TITLE="$1"
     local URL="$2"
     local DESCRIPTION="$3"
-    local labels
-    local labels_csv
-    labels=$(python /home/thomas/Development/Projects/llm/ai-issues/llm_label_maker/label_maker.py --url "$URL" --title "$TITLE" --description "$DESCRIPTION")
-    labels_csv=$(echo "$labels" | tr -d [])
-    labels_csv=$(echo "$labels_csv" | tr -d \' | tr -d ' ')
-    echo "$labels_csv"
+    local labels=$(python /home/thomas/Development/Projects/llm/label-maker/label_maker.py --url "$URL" --title "$TITLE" --description "$DESCRIPTION")
+    echo "$labels"
 }
 
 # Main execution
@@ -49,4 +52,14 @@ if [ "$#" -ne 3 ]; then
     exit 1
 fi
 
-send_note_to_github "$1" "$2" "$3"
\ No newline at end of file
+TITLE="$1"
+URL="$2"
+DESCRIPTION="$3"
+
+labels_json=$(get_labels_json "$TITLE" "$URL" "$DESCRIPTION")
+generate_labels=$(echo "$labels_json" | jq '.generated_labels | to_entries[]')
+
+picked_labels=$(echo "$labels_json" | jq '.picked_labels | to_entries[] | select(.value == true) | .key')
+gh_markdown_highlight_generated_labels=$(echo "$generate_labels" | tr '\n' ' ' | sed 's/.$//')
+
+send_note_to_github "$TITLE" "$URL" "$DESCRIPTION" "$picked_labels" "$gh_markdown_highlight_generated_labels"
\ No newline at end of file
diff --git a/label_maker.py b/label_maker.py
index 6592697..b3b3be2 100644
--- a/label_maker.py
+++ b/label_maker.py
@@ -1,55 +1,12 @@
-import os, json, argparse, subprocess
+import os, json, argparse, subprocess, sys
 from openai import OpenAI
 
 client = OpenAI(
     api_key=os.environ["OPENAI_API_KEY"],
 )
-OPENAI_API_KEY = client.api_key
-
-def generate_new_labels(labels, url, title, description):
-    """Generate new labels if the existing labels are inadequate."""
-    messages = [
-        {"role": "system", "content": """You are a helpful assistant designed to output JSON lists of labels.
-        Think carefully about the labels you select.
-        The labels you create should make it easier to organize and search for information."""},
-        {"role": "user", "content": f"""Think of some keywords for this link.\n
-         url: {url}\n
-         title: {title}\n
-         description: {description}\n
-         
-         **labels:**
-         {labels}\n
-        Write A MAXIMUM OF TWO label,description pairs to describe this link:\n
-        *IMPORTANT* Make sure the labels are unique and highly descriptive."""}
-    ]
-    # Step 1: call the model
-    response = client.chat.completions.create(
-        model="gpt-3.5-turbo-1106",
-        response_format={"type": "json_object"},
-        temperature=1,
-        seed=0,
-        messages=messages,
-    )
-    response_message = response.choices[0].message
-    return response_message
-
-
-def create_new_labels(repo, label_list):
-    """Create new labels for a GitHub repo."""
-    new_labels_created = []
-    for label in label_list:
-        label_name = label["name"]
-        label_description = label["description"]
-        command = ["gh", "label", "create", "-R", repo, label_name, "-d", label_description]
-        result = subprocess.run(command, capture_output=True, text=True, check=True)
-        if result.stderr:
-            print("Error:", result.stderr)
-        else:
-            print(f"Created label: {label_name}")
-            new_labels_created.append(label_name)
-    
-    return new_labels_created
 
+OPENAI_API_KEY = client.api_key
+sys.stdout = open('/dev/tty', 'w')
 
 def request_labels_list(repo):
     with open('/dev/tty', 'w') as f:
@@ -62,11 +19,7 @@ def request_labels_list(repo):
         labels = json.loads(result.stdout)
         if labels:
             f.write(f"got {len(labels)} labels\n\n")
-        # Print the information or do further processing if needed
-        # for label in labels:
-        #     print(f"Label Name: {label['name']}, Color: {label['color']}")
-
-        # If an error occurs, print the error message
+        
         if result.stderr:
             print("Error:", result.stderr)
         parsed_labels = ""
@@ -74,7 +27,6 @@ def request_labels_list(repo):
         
         for label in labels:
             parsed_labels += f"{label['name']}: {label['description']}\n"
-            # label_dict[label['name']] = label['description']
         return parsed_labels
 
 
@@ -84,7 +36,7 @@ def new_labels_needed(labels, url, title, description):
     title: {title}
     description: {description}
 
-Are new labels needed to adequately delineate this bookmark? (True) or can you label it accurately with the existing labels? (False)
+Are new labels needed to adequately delineate the broad categories and topics of the bookmark? (True) or can you label it accurately with the existing labels? (False)
 Only answer True if you are certain that new labels are needed. If you are unsure, then answer False.
 Only reply with True or False.
 
@@ -111,14 +63,79 @@ Only reply with True or False.
         return False
 
 
+#  Think carefully about the labels you choose. Only output labels in json format.
+        # The labels you create should make it easier to organize and retrieve information by topic and genre.
+        #  They should also be in keeping with the style of the existing labels.
+        #  never create labels for company names, people, or other proper nouns.
+
+
+def generate_new_labels(labels, url, title, description):
+    """Generate new labels if the existing labels are inadequate."""
+    messages = [
+        {"role": "system", "content": """You are a helpful assistant designed to output correct JSON lists of labels in the JSON format: {"label": "description", "label": "description"}
+         **IMPORTANT** Pay close attention to unfamiliar words and phrases, they may be very important and delineate a new concept."""},
+        {"role": "user", "content": f"""Think of some keywords for this link.\n
+         url: {url}\n
+         title: {title}\n
+         description: {description}\n
+         
+         **labels:**
+         {labels}\n
+        Write A MAXIMUM OF TWO NEW label,description pairs to describe this link, as the existing labels are not adequate on their own.
+        *IMPORTANT* Make sure the labels are useful. They should capture the topics of the link, not the link itself.
+        They should also be in keeping with the style of the existing labels.
+        Keep descriptions short and to the point. They should be no longer than a sentence."""}
+    ]
+    # Step 1: call the model
+    response = client.chat.completions.create(
+        model="gpt-3.5-turbo-1106",
+        response_format={"type": "json_object"},
+        temperature=1,
+        seed=0,
+        messages=messages,
+    )
+    response_message = response.choices[0].message
+    return response_message
+
+
+def create_new_labels(repo, label_list):
+    """Create new labels for a GitHub repo."""
+    new_labels_created = []
+    for label in label_list:
+        label_name = label["name"]
+        label_description = label["description"]
+        command = ["gh", "label", "create", "-R", repo, label_name, "-d", label_description]
+        result = subprocess.run(command, capture_output=True, text=True, check=True)
+        if result.stderr:
+            print("Error:", result.stderr)
+        else:
+            print(f"Created label: {label_name}")
+            new_labels_created.append(label_name)
+    
+    return new_labels_created
+
+
 def pick_labels(url, title, description, labels):
     """
     Choose the labels to assign to a bookmark.
     """
     
-    pick_labels_query = f"""Pick A MINIMUM OF THREE (3) labels from the list to describe this link:\n
-    *IMPORTANT* Only pick from the labels provided. Output a JSON list of labels.
-    url: {url}\ntitle: {title}\ndescription: {description}\nlabels: {labels}
+    pick_labels_query = f"""Given the following bookmark:\n
+    url: {url}\n
+    title: {title}\n
+    description: {description}\n
+    
+    Which, if any, of these labels certainly apply to this bookmark?
+    *IMPORTANT* Only pick from the labels provided if they apply. Output a JSON list of labels.
+    *IMPORTANT* if no labels apply, output an empty list or select the 'New Label' label exclusively to request a new label be made to categorize this bookmark.
+        
+    **labels:**
+    
+    
+    {labels}
+
+
+    **IMPORTANT** Only say from the labels under the **labels:** heading. Do not say anything else
     """
 
     messages = [
@@ -136,10 +153,14 @@ def pick_labels(url, title, description, labels):
         seed=0,
         messages=messages
     )
-    # return a list of labels
-    response_message = response.choices[0].message.content
-    print(f"Labels Picked: {response_message}")
-    return response_message
+    
+    picked_labels = response.choices[0].message.content
+    if picked_labels:
+        picked_labels_list = json.loads(picked_labels) # picked_labels_list: {'Models': True, 'llm': True, 'prompt': True, 'few-shot-learning': True}
+        print(f"picked_labels_list: {picked_labels_list}")
+        print()
+        return picked_labels_list
+        
 
 parser = argparse.ArgumentParser(description='Generate labels for a given bookmark.')
 parser.add_argument('--url', metavar='url', type=str, help='The url of the bookmark.')
@@ -148,13 +169,6 @@ parser.add_argument('--description', metavar='description', type=str, help='The
 parser.add_argument('--repo', metavar='repo', type=str, help='The repo to get labels from.', default="irthomasthomas/undecidability")
 args = parser.parse_args()
 
-# Algorithm:
-# 1. Request a list of labels from the repo.
-# 2. Check if the existing labels are adequate.
-# 3. If not, generate new labels.
-# 4. Create the new labels.
-# 5. Pick the labels to assign to the bookmark.
-# 6. Return the labels.
 labels_dict = {}
 
 if args.url:
@@ -163,14 +177,14 @@ if args.url:
     if new_labels_needed(labels, args.url, args.title, args.description):
         generated_labels = generate_new_labels(labels, args.url, args.title, args.description)
         generated_labels_list = json.loads(generated_labels.content)
-        print(f"LABELS REQUESTED:\n {generated_labels_list}")
-    picked_labels = json.loads(pick_labels(args.url, args.title, args.description, labels))
-    #


**Response:**
Refactor code to improve readability and remove unnecessary comments and print statements.

<details><summary>Metadata</summary>

- Duration: 707 ms
- Datetime: 2024-01-08T21:58:03.770307
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

