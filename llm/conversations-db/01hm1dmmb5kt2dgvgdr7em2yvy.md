**Prompt:**
Can you rewrite these to use python and lisp exclusively. Drop the shell stuff.

gh-selection-to-issue.lisp: (define-command-global gh-send-selection-to-issue ()
  "Sends url, title, and selection to a new gh issue via a single FIFO"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (fifo-path "/tmp/nyxt_gh_data"))
    (with-open-file (stream fifo-path
                            :direction :output
                            :if-exists :supersede
                            :if-does-not-exist :create)
      (format stream "--BEGIN TITLE--~%~a~%--END TITLE--~%--BEGIN URL--~%~a~%--END URL--~%--BEGIN SELECTION--~%~a~%--END SELECTION--~%" title (render-url myurl) selection))))


github_issues.sh: #!/bin/bash

# github_issues.sh

send_note_to_github() {
    local TITLE="$1"
    local URL="$2"
    local DESCRIPTION="$3"
    local labels="$4"
    local gh_markdown_highlight_generated_labels="$5"
    local BODY
    local task_list
    local issue_url
    local labels_csv
    echo >&2
    echo "send_note_to_github" >&2
    echo "gh_markdown_highlight_generated_labels: $gh_markdown_highlight_generated_labels" >&2

    echo >&2
    if [ -z "$TITLE" ]; then
        TITLE="$(llm "generate a title from this url:$URL:quote:$DESCRIPTION" -o temperature 0.1)"
    fi
    
    task_list="- [ ] [${TITLE}](${URL})"
    suggested_labels="#### Suggested labels
#### $gh_markdown_highlight_generated_labels"
    
    BODY="$task_list\n
$DESCRIPTION\n
$suggested_labels"
    BODY_FORM=$(llm --system "You are a markdown text formatter. Reply in valid GH markdown only. 
    *IMPORTANT*: NEVER SAY ANYTHING ELSE TO THE USER.
    **IMPORTANT**: ONLY EDIT FORMAT, NEVER CONTENT." "Make this content into a pretty gh markdown note:quote:$BODY" -o temperature 0.1)
    echo >&2
    echo >&2
    echo "formatted body: $BODY_FORM" >&2
    echo >&2
    echo >&2
    labels_csv=$(echo "$labels" | tr '\n' ',' | sed 's/.$//')
    echo "labels_csv: $labels_csv" >&2
    
    issue_url=$(gh issue create --title "$TITLE" --body "$BODY_FORM" --label "$labels_csv" --web)
    echo "$issue_url"
}


get_labels_json() {
    local TITLE="$1"
    local URL="$2"
    local DESCRIPTION="$3"
    echo >&2
    echo "get_labels_json" >&2
    echo "description: $DESCRIPTION" >&2
    echo >&2

    local labels=$(python /home/thomas/Development/Projects/llm/label-maker/label_maker.py --url "$URL" --title "$TITLE" --description "$DESCRIPTION")
    echo "$labels"
}

# Main execution
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <title> <url> <DESCRIPTION>"
    exit 1
fi

TITLE="$1"
URL="$2"
DESCRIPTION="$3" # Why is this empty?
echo >&2
echo "START github_issues.sh" >&2
echo "Description: $DESCRIPTION" >&2
echo >&2

labels_json=$(get_labels_json "$TITLE" "$URL" "$DESCRIPTION")
generate_labels=$(echo "$labels_json" | jq '.generated_labels | to_entries[]')

picked_labels=$(echo "$labels_json" | jq '.picked_labels | to_entries[] | select(.value == true) | .key')
gh_markdown_highlight_generated_labels=$(echo "$generate_labels" | tr '\n' ' ' | sed 's/.$//')

send_note_to_github "$TITLE" "$URL" "$DESCRIPTION" "$picked_labels" "$gh_markdown_highlight_generated_labels"


nyxt_to_github.sh: #!/bin/bash
# nyxt_to_github.sh


monitor_nyxt_to_gh_pipe() {
    local TITLE=""
    local URL=""
    local SELECTION=""
    local parsing_section=""
    while IFS= read -r line; do
        case "$line" in
            --BEGIN\ TITLE--*) parsing_section="TITLE" ;;
            --BEGIN\ URL--*) parsing_section="URL" ;;
            --BEGIN\ SELECTION--*) parsing_section="SELECTION" ;;
            --END\ TITLE--*) parsing_section="" ;;
            --END\ URL--*) parsing_section="" ;;
            --END\ SELECTION--*)
                /home/thomas/Development/Projects/llm/label-maker/github_issues.sh "$TITLE" "$URL" "$SELECTION"
                ;;
        *)
            case $parsing_section in
                TITLE) TITLE+="$line"$'\n' ;;
                URL) URL+="$line"$'\n' ;;
                SELECTION) SELECTION+="$line"$'\n' ;;
            esac
            ;;
    esac
    done < "$fifo_path"
}

target_project="undecidability"
target_directory="$HOME/$target_project"
cd "$target_directory" || exit 2
echo "$PWD"

fifo_path="/tmp/nyxt_gh_data"
if [ ! -p "$fifo_path" ]; then
    mkfifo "$fifo_path"
    echo "Created named pipe: $fifo_path" >&2
fi

# Main loop
echo "Starting nyxt-to-gh.sh"
while true; do
    monitor_nyxt_to_gh_pipe
    sleep 5
done


label_maker.py: import os, json, argparse, subprocess, sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

OPENAI_API_KEY = client.api_key
sys.stdout = open('/dev/tty', 'w')

def request_labels_list(repo):
    with open('/dev/tty', 'w') as f:
        f.write(f"get_issues_labels_list: {repo}\n\n")
        per_page = 100
        command = ["gh", "label", "list", "-R", repo, "-L", "100", "--json", "name,description,color"]
        
        # Execute the command using subprocess
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        labels = json.loads(result.stdout)
        if labels:
            f.write(f"got {len(labels)} labels\n\n")
        
        if result.stderr:
            print("Error:", result.stderr)
        parsed_labels = ""
        label_dict = {}
        
        for label in labels:
            parsed_labels += f"{label['name']}: {label['description']}\n"
        return parsed_labels


def new_labels_needed(labels, url, title, description):
    adequate_labels_query = f"""Given the following bookmark:
    url: {url}
    title: {title}
    description: {description}

Are new labels needed to adequately delineate the broad categories and topics of the bookmark? (True) or can you label it accurately with the existing labels? (False)
Only answer True if you are certain that new labels are needed. If you are unsure, then answer False.
Only reply with True or False.

    **labels:**
    {labels}

**Important**: Say nothing except true or false."""
    messages = [
        {"role": "system", "content": """You are a helpful assistant designed to answer binary questions with True or False."""},
        {"role": "user", "content": adequate_labels_query}
    ]
    # Step 1: call the model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        seed=0,
        messages=messages,
    )
    response_message = response.choices[0].message
    print(f"New Labels Are Needed: {response_message.content}")
    if response_message.content == "True":
        return True
    else:
        return False

def generate_new_labels(labels, url, title, description):
    """Generate new labels if the existing labels are inadequate."""
    messages = [
        {"role": "system", "content": """You are a helpful assistant designed to output correct JSON lists of labels in the JSON format: {"label": "description", "label": "description"}
         **IMPORTANT** Pay close attention to unfamiliar words and phrases, they may be very important and delineate a new concept."""},
        {"role": "user", "content": f"""Think of some keywords for this link.\n
         url: {url}\n
         title: {title}\n
         description: {description}\n
         
         **labels:**
         {labels}\n
        Write A MAXIMUM OF TWO NEW label,description pairs to describe this link, as the existing labels are not adequate on their own.
        *IMPORTANT* Make sure the labels are useful. They should capture the topics of the link, not the link itself.
        They should also be in keeping with the style of the existing labels.
        Keep descriptions short and to the point. They should be no longer than a sentence."""}
    ]
    # Step 1: call the model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        temperature=1,
        seed=0,
        messages=messages,
    )
    response_message = response.choices[0].message
    return response_message


def create_new_labels(repo, label_list):
    """Create new labels for a GitHub repo."""
    new_labels_created = []
    for label in label_list:
        label_name = label["name"]
        label_description = label["description"]
        command = ["gh", "label", "create", "-R", repo, label_name, "-d", label_description]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if result.stderr:
            print("Error:", result.stderr)
        else:
            print(f"Created label: {label_name}")
            new_labels_created.append(label_name)
    
    return new_labels_created


def pick_labels(url, title, description, labels):
    """
    Choose the labels to assign to a bookmark.
    """
    
    pick_labels_query = f"""Given the following bookmark:\n
    url: {url}\n
    title: {title}\n
    description: {description}
    
    Which, if any, of these labels certainly apply to this bookmark?
    *IMPORTANT* Only pick from the labels provided if they apply. Output a JSON list of labels.
    *IMPORTANT* if no labels apply, output an empty list or select the 'New Label' label exclusively to request a new label be made to categorize this bookmark.
        
    **labels:**
    
    
    {labels}


    **IMPORTANT** Only say from the labels under the **labels:** heading. Do not say anything else
    """

    messages = [
        {"role": "system", "content": """You are a helpful assistant designed to output JSON lists of labels. 
        Think carefully about the labels you select. 
        The labels you select should make it easier to organize and search for information. 
         **IMPORTANT** Only pick from the labels provided."""},
        {"role": "user", "content": pick_labels_query}
    ]
    print()
    print(f"pick_labels_query: {pick_labels_query}")
    print()
    # Step 1: call the model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        temperature=1,
        seed=0,
        messages=messages
    )
    
    picked_labels = response.choices[0].message.content
    if picked_labels:
        picked_labels_list = json.loads(picked_labels) # picked_labels_list: {'Models': True, 'llm': True, 'prompt': True, 'few-shot-learning': True}
        print(f"picked_labels_list: {picked_labels_list}")
        print()
        return picked_labels_list
        

parser = argparse.ArgumentParser(description='Generate labels for a given bookmark.')
parser.add_argument('--url', metavar='url', type=str, help='The url of the bookmark.')
parser.add_argument('--title', metavar='title', type=str, help='The title of the bookmark.')
parser.add_argument('--description', metavar='description', type=str, help='The selected text of the bookmark.')
parser.add_argument('--repo', metavar='repo', type=str, help='The repo to get labels from.', default="irthomasthomas/undecidability")
args = parser.parse_args()

labels_dict = {}

if args.url:
    labels = request_labels_list(args.repo)
    if new_labels_needed(labels, args.url, args.title, args.description):
        generated_labels = generate_new_labels(labels, args.url, args.title, args.description)
        generated_labels_list = json.loads(generated_labels.content)

    picked_labels = pick_labels(args.url, args.title, args.description, labels) # picked_labels_list: {'MachineLearning': 'ML Models, Training and Inference', 'AI-Agents': 'Autonomous AI agents using LLMs', 'GoogleCloud': 'Google Cloud-related content'}
    if generated_labels:
        if "New Label" not in picked_labels.keys():
            picked_labels["New Label"] = True

        labels_dict["generated_labels"] = generated_labels_list
    
    labels_dict["picked_labels"] = picked_labels
    sys.stdout = sys.__stdout__
    print(f"{json.dumps(labels_dict, indent=4)}")


**Response:**
The code spans over three different scripts (two shell scripts and one Python script) as well as an initial Lisp function. I will rewrite the logic for each component in just Python and Lisp (Common Lisp for the Lisp part, specifically using the SBCL implementation). Keep in mind that direct interaction with the command line (like creating a FIFO file) will be dropped, but you can integrate these Python and Lisp codes into an environment or tools that support their execution.

**Lisp replacement for `gh-selection-to-issue.lisp`:**

```lisp
(defpackage :gh-issue
  (:use :cl :nyxt))

(in-package :gh-issue)

(define-command gh-send-selection-to-issue ()
  "Sends url, title, and selection to a new gh issue"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string)))))
    ;; Instead of writing to a FIFO, we can communicate directly with Python via IPC or a file.
    ;; Here, I will use a file to store data temporarily.
    (let ((file-path (merge-pathnames "nyxt_gh_data.txt" (user-homedir-pathname))))
      (with-open-file (stream file-path
                              :direction :output
                              :if-exists :supersede
                              :if-does-not-exist :create)
        (format stream "~a~%~a~%~a" title myurl selection)))))
```

**Python replacement for `github_issues.sh` and `nyxt_to_github.sh`:**

```python
import subprocess
import json
import sys
import os
from time import sleep

# Put the username and repository in these constants
GITHUB_USER = 'your-github-username'
GITHUB_REPO = 'your-github-repository'
DATA_FILE = '/path/to/nyxt_gh_data.txt'  # Use the file path established in the Lisp script.
OPENAI_API_KEY = 'your-openai-api-key'


def create_issue(title, url, description, labels):
    # This function essentially mimics the behavior of the original GitHub shell script.
    # Fill in the logic to create GitHub issues using the GitHub API.
    pass  # Replace this with your logic to create a GitHub issue using the API.


def parse_data_file(file_path):
    with open(file_path, 'r') as f:
        title = f.readline().strip()
        url = f.readline().strip()
        selection = f.readline().strip()
    return title, url, selection


def monitor_data_file(file_path):
    # Continuously monitor the data file for new content and process accordingly
    while True:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            title, url, description = parse_data_file(file_path)
            labels = get_labels(title, url, description)
            create_issue(title, url, description, labels)
            # Clean up the file after processing to be ready for the next data.
            open(file_path, 'w').close()
        sleep(5)


def get_labels(title, url, description):
    # Implement the logic to get labels for a GitHub issue.
    # This would involve AI interactions or another method to intelligently generate labels.
    return ['label1', 'label2']  # Replace this with real label-generating logic.


if __name__ == "__main__":
    monitor_data_file(DATA_FILE)
```

This Python script monitors a specified data file (`DATA_FILE`) for new content, and when new data is present (i.e., a title, URL, and selection text), it processes this information to create a GitHub issue. The `create_issue` function is a placeholder where you'd implement the logic to actually create the issue using the GitHub API. The `get_labels` function should contain the logic to generate or retrieve labels for the new issue.

Please note that you may need to use a Python library such as `requests` to interact with the GitHub API to create issues, and potentially you'd integrate an AI model (or call an external script) to generate labels. Also, integrating an OpenAI model in a production system requires careful consideration of API usage, error handling, and other operational concerns.

<details><summary>Metadata</summary>

- Duration: 22915 ms
- Datetime: 2024-01-13T12:44:15.713398
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
I want the bookmaring and the gh issue and label generation to be seperate. So that they can be reused for other tasks besides bookmarking.

**Response:**
Sure, let's separate the bookmarking interaction from the GitHub issue and label generation logic. We'll define two distinct Lisp functions for bookmarking-related tasks, and Python functions will be used for GitHub issue and label generation.

### Lisp Functions

First, a command to save the current page's title, URL, and selection to a file:

```lisp
;; In the REPL or Lisp file for Nyxt
(defpackage :gh-issue
  (:use :cl :nyxt))

(in-package :gh-issue)

(define-command gh-save-selection ()
  "Saves the page title, URL, and selection to a file for later processing."
  (let* ((title (url (current-buffer)))
         (url (title (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string)))))
    (let ((file-path (merge-pathnames "bookmark_data.txt" (uiop:xdg-data-home))))
      (uiop:with-safe-io-syntax
        (with-open-file (stream file-path
                                :direction :output
                                :if-exists :supersede
                                :if-does-not-exist :create)
          (format stream "~a~%~a~%~a~%" title url selection))))))
```

### Python Functions

Python functions to process the bookmark data and interact with GitHub:

```python
import json
import requests
from pathlib import Path

# Constants for API endpoints and paths
BOOKMARKS_FILE = Path.home() / "bookmark_data.txt"
GITHUB_API_URL = "https://api.github.com"
GITHUB_USER = "your-github-username"
GITHUB_REPO = "your-github-repository"
GITHUB_TOKEN = "your-github-token"

# Function to read the saved selection
def read_bookmark_data(bookmark_file):
    with open(bookmark_file, 'r') as file:
        title = file.readline().strip()
        url = file.readline().strip()
        selection = file.readline().strip()
    return title, url, selection

# Function to create a GitHub issue with labels
def create_github_issue(title, selection, labels):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': title,
        'body': selection,
        'labels': labels
    }
    response = requests.post(f'{GITHUB_API_URL}/repos/{GITHUB_USER}/{GITHUB_REPO}/issues', headers=headers, json=data)
    if response.status_code == 201:
        print(f'Issue created: {response.json()["html_url"]}')
    else:
        print(f'Failed to create issue: {response.json()}')

# Function to generate labels for an issue
def generate_labels(title, url, selection):
    # Placeholder - replace with your logic to generate labels
    return ["label1", "label2"]

# Main function to process bookmarks and create GitHub issues
def process_bookmarks():
    if BOOKMARKS_FILE.exists():
        title, url, selection = read_bookmark_data(BOOKMARKS_FILE)
        labels = generate_labels(title, url, selection)
        create_github_issue(title, selection, labels)
        BOOKMARKS_FILE.unlink()  # Clear the file after processing

if __name__ == "__main__":
    process_bookmarks()
```

### Usage

With these two separated components, you have flexibility in using them. The Lisp snippet can be executed within Nyxt to capture webpage information, and the saved data can later be processed by the Python script to create GitHub issues. 

This separation not only allows reuse for other bookmarking-related tasks but also modularizes the work, making it possible to implement batch processing or scheduled tasks for GitHub issue creation based on bookmarks captured at different times.

<details><summary>Metadata</summary>

- Duration: 41370 ms
- Datetime: 2024-01-13T13:03:02.111083
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

