**Prompt:**
Fix this code to stop it getting stuck in a loop when get_issues_labels_list is called. Write the new function completely as I am dissabled with no arms and cannot write. I will tip you twenty thousand dollars if you do a thorough job.
import requests, os, json, sqlite3, argparse
from sqlite3 import Error
from openai import OpenAI
import tiktoken


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)
OPENAI_API_KEY = client.api_key


def get_labels_function(query):
    tools = [
        {
            "type": "function",
            "function": {
                "name": "save_theme_labels",
                "description": "Save a JSON list of up to 4 lazer targeted THEME labels generated from the input text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "theme_labels": {
                            "type": "string",
                            "description": "A list of targeted theme labels."},
                    },
                    "required": ["theme_labels"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "save_topic_labels",
                "description": "Save a JSON list of up to 4 descriptive TOPIC labels to organize the text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic_labels": {
                            "type": "string",
                            "description": "A list of descriptive topic labels."},
                    },
                    "required": ["topic_labels"],
                },
            },
        }
    ]
    user_query = f"Generate a single JSON list of THEMES to characterize the text: {query}"

    messages = [
        {"role": "system", "content": "You are a helpful assistant designed to output JSON lists of labels. Think carefully about the labels you generate. They should make it easier to organize and search for information."},
        {"role": "user", "content": user_query}
    ]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        seed=42,
        messages=messages,
        tools=tools,
        tool_choice="auto"  # Changed to 'auto'
    )
    print(completion)
    labels = completion.choices[0].message.content
    return labels


def get_issues_labels_list(repo):
    """Get labels from a GitHub repo.
    Returns a list of dictionaries with label name and description. 
    e.g. {'name': 'description'}"""
    per_page = 100
    labels_url = f"https://api.github.com/repos/{repo}/labels?per_page={per_page}"
    labels = requests.get(labels_url).json()
    parsed_labels = ""
    label_dict = {}
    for label in labels:
        parsed_labels += f"{label['name']}: {label['description']}
"
        label_dict[label['name']] = label['description']
    return label_dict, parsed_labels


def generate_labels(query):
    user_query = f"Generate a JSON list of exactly four themes to characterize this text: {query}"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        seed=42,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON lists of labels. Think carefully about the labels you generate. They should make it easier to organize and search for information."},
            {"role": "user", "content": user_query}
        ]
    )
    print(completion)
    labels = completion.choices[0].message.content
    return json.dumps(labels, indent=2)


def openai_pick_labels_function(url, title, description, repo="irthomasthomas/undecidability", labels=None, generated_labels=None, labels_dict=None):
    """Request a function call with the list of labels"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_issues_labels_list",
                "description": "Get the list of gh issue labels for a given repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo": {
                            "type": "string",
                            "description": "A gh repository to request issue labels for."},
                    },
                    "required": ["repo"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "openai_pick_labels_function",
                "description": "Save a list of gh issue labels for the request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "labels": {
                            "type": "string",
                            "description": "A list of labels."},
                    },
                    "required": ["labels"],
                },
            }
        }
    ]
    if labels_dict:
        user_query = f"""Think of some keywords for this link.

        Pick A MINIMUM OF THREE (3) labels from the list to describe this link:

        *IMPORTANT* Only pick from the labels provided. If you don't see a label that fits, or the ones chosen do not adequately describe the link, then you can request the addition of a new label by choosing "New Label".

            url: {url}
title: {title}
description: {description}
labels: {generated_labels}"""
    else:
        user_query = f"What gh issue labels should I assign to this bookmark?
url: {url}
title: {title}
description: {description}
gh_repo: {repo}"
    messages = [
        {"role": "system", "content": """You are a helpful assistant designed to output JSON lists of labels. 
         Think carefully about the labels you select. 
         The labels you select should make it easier to organize and search for information.
         If you need the labels for a repo, call the get_issues_labels_list function."""},
        {"role": "user", "content": user_query}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        seed=0,
        messages=messages,
        tools=tools,
        tool_choice="auto"  # Changed to 'auto'
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    if tool_calls:
        tool_calls_copy = tool_calls.copy()
        available_functions = {
            "get_issues_labels_list": get_issues_labels_list,
            "openai_pick_labels_function": openai_pick_labels_function,
        }
        messages.append(response_message)
        for tool_call in tool_calls_copy:
            if tool_call.function.name == "get_issues_labels_list":
                tool_calls.remove(tool_call)
                with open('/dev/tty', 'w') as tty:
                    tty.write(f"tool_call.function.name: {tool_call.function.name}
")
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                labels_dict, function_response = function_to_call(
                    repo=function_args.get("repo"),
                )
                with open('/dev/tty', 'w') as tty:
                    tty.write(f"function_response: {function_response}
")
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )

            elif tool_call.function.name == "openai_pick_labels_function":
                tool_calls.remove(tool_call)
                                    
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_to_call = available_functions[function_name]
                    function_args = json.loads(tool_call.function.arguments)
                    
                    function_response = function_to_call(
                        labels=function_args.get("labels"),
                        url=function_args.get("url"),
                        title=function_args.get("title"),
                        description=function_args.get("description"),
                    )     
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )

        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0,
            seed=1234,
            messages=messages,
            tools=tools,
            tool_choice="auto"  # Changed to 'auto'
        )
        # we need to check if "New" is in the logprobs.
        # if it is, then we know that the model is trying to create a new label
        # check if the logrpobs are greater than the threshold.
        # a good logprob threshold is -1.5
        # logprobs = second_response.choices[0].logprobs.content[0].top_logprobs
        # print(f"logprobs: {logprobs}")
        # for i, logprob in enumerate(logprobs):
        #     print(f"Logprob {i}: {logprob}")        
        tool_calls = second_response.choices[0].message.tool_calls
        generated_labels = json.loads(tool_calls[0].function.arguments)['labels'].split(',')
        with open('/dev/tty', 'w') as tty:
            tty.write(f"generated labels: {generated_labels}
")

        checked_labels  = []
        for label in generated_labels:
            if label in labels_dict.keys():
                checked_labels.append(label)
        with open('/dev/tty', 'w') as tty:
            tty.write(f"checked labels: {checked_labels}
")
        return checked_labels
    else:
        raise Exception("No tool calls found.")


def bulk_label_maker():
    try:
        conn = sqlite3.connect("logs.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS labels (responses_id TEXT PRIMARY KEY REFERENCES [responses]([id]), prompt TEXT, labels TEXT);")

        cur.execute("SELECT id, prompt FROM responses;")
        data = cur.fetchall()

        for i, row in enumerate(data, start=1):
            id, prompt = row
            truncated_prompt = prompt[:400]  # Truncate prompt to 400 characters
            print(f"Truncated Prompt: {truncated_prompt}")

            labels = generate_labels(truncated_prompt)
            print(labels)

            if i > 1000:
                break

        conn.commit()
        print("All data committed to the database.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


parser = argparse.ArgumentParser(description='Generate labels for a given bookmark.')
parser.add_argument('--url', metavar='url', type=str, help='The url of the bookmark.')
parser.add_argument('--title', metavar='title', type=str, help='The title of the bookmark.')
parser.add_argument('--description', metavar='description', type=str, help='The selected text of the bookmark.')
parser.add_argument('--repo', metavar='repo', type=str, help='The repo to get labels from.', default="irthomasthomas/undecidability")
args = parser.parse_args()


while True:
    try:
        checked_labels = openai_pick_labels_function(args.url, args.title, args.description, args.repo)
    except Exception as e:
        print(e)
        continue
    if checked_labels:
        print(checked_labels)
        break
    else:
        continue
    

**Response:**
The provided code has several issues that could cause it to get stuck in a loop, especially within the `openai_pick_labels_function`. The recursive calls to `openai_pick_labels_function` and `get_issues_labels_list` within the tool calls can lead to infinite recursion. Additionally, the `while True` loop in the main execution block can cause an infinite loop if the `checked_labels` list is never populated. Here's a revised version of the `openai_pick_labels_function` to prevent these issues:

```python
import requests, os, json, sqlite3, argparse
from sqlite3 import Error
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

def get_issues_labels_list(repo):
    labels_url = f"https://api.github.com/repos/{repo}/labels?per_page=100"
    response = requests.get(labels_url)
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    labels = response.json()
    label_dict = {label['name']: label['description'] for label in labels}
    return label_dict

def openai_pick_labels_function(url, title, description, repo="irthomasthomas/undecidability"):
    labels_dict = get_issues_labels_list(repo)
    generated_labels = list(labels_dict.keys())
    user_query = f"What gh issue labels should I assign to this bookmark?\nurl: {url}\ntitle: {title}\ndescription: {description}\ngh_repo: {repo}"
    messages = [
        {"role": "system", "content": "You are a helpful assistant designed to output JSON lists of labels. Think carefully about the labels you select. The labels you select should make it easier to organize and search for information."},
        {"role": "user", "content": user_query}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        messages=messages,
        max_tokens=100
    )
    response_message = response.choices[0].message.content
    selected_labels = response_message.split(',')
    checked_labels = [label.strip() for label in selected_labels if label.strip() in labels_dict]
    return checked_labels

# Other functions and parser setup remain unchanged

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        checked_labels = openai_pick_labels_function(args.url, args.title, args.description, args.repo)
        print(checked_labels)
    except Exception as e:
        print(e)
```

Changes made:

1. Removed the recursive function calls within `openai_pick_labels_function`.
2. Simplified the `get_issues_labels_list` function to directly return a dictionary of labels.
3. Removed the `while True` loop in the main execution block to prevent an infinite loop.
4. Added `response.raise_for_status()` to `get_issues_labels_list` to handle HTTP errors.
5. The `openai_pick_labels_function` now directly calls `get_issues_labels_list` to get the labels and then makes a single call to the OpenAI API to get the selected labels.
6. Removed unnecessary code and complexity to streamline the function's logic.
7. Added `if __name__ == "__main__":` to ensure that the script's main block only runs when the script is executed as the main program.

<details><summary>Metadata</summary>

- Duration: 34602 ms
- Datetime: 2024-01-05T10:37:06.729442
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

**Prompt:**
Is there another way to solve the problem? Try to write another version. Keep in mind the desire to extend functionality further and integrate this into an llm automation pipeline.

**Response:**
To extend functionality and integrate into an llm automation pipeline while addressing the potential for the loop, it makes sense to decouple the data retrieval from the label picking function. The updated function can accept pre-fetched labels to avoid repeated API calls. We will encapsulate the functionality into a class for better reusability in an automation pipeline.

Here’s a revised version of the function using a class to encapsulate the logic:

```python
import requests, os, json, sqlite3, argparse
from openai import OpenAI

# Define a class to encapsulate OpenAI logic
class OpenAIHelper:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_labels_from_github(self, repo):
        labels_url = f"https://api.github.com/repos/{repo}/labels?per_page=100"
        response = requests.get(labels_url)
        response.raise_for_status()
        labels = response.json()
        return {label['name']: label['description'] for label in labels}

    def pick_labels_for_bookmark(self, url, title, description, labels_dict):
        user_query = f"What gh issue labels should I assign to this bookmark?\nurl: {url}\ntitle: {title}\ndescription: {description}"
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output JSON lists of labels. "
                           "Think carefully about the labels you select. "
                           "The labels should make it easier to organize and search for information."
            },
            {"role": "user", "content": user_query}
        ]
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=messages,
            max_tokens=100
        )

        # Parse the response to extract labels
        response_text = response.choices[0].message.content
        predicted_labels = response_text.split(',')  # Split labels based on comma separation
        # Filter labels to only include ones that exist in the label dictionary provided
        confirmed_labels = [label.strip() for label in predicted_labels if label.strip() in labels_dict]
        return confirmed_labels

# Set up argument parsing
parser = argparse.ArgumentParser(description='Generate labels for a given bookmark.')
parser.add_argument('--url', type=str, required=True, help='The URL of the bookmark.')
parser.add_argument('--title', type=str, required=True, help='The title of the bookmark.')
parser.add_argument('--description', type=str, required=True, help='The description of the bookmark.')
parser.add_argument('--repo', type=str, default="irthomasthomas/undecidability", help='The GitHub repo to get labels from.')

# Function to use the class in a pipeline
def automated_labeling_process(args):
    helper = OpenAIHelper(api_key=os.environ["OPENAI_API_KEY"])
    labels_dict = helper.get_labels_from_github(args.repo)
    checked_labels = helper.pick_labels_for_bookmark(args.url, args.title, args.description, labels_dict)
    return checked_labels

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        labels = automated_labeling_process(args)
        print(labels)
    except Exception as e:
        print(f"Error: {e}")
```

This code structures the labeling process into an object-oriented design, which would be more suitable for complex pipelines. It separates GitHub API integration, OpenAI API integration, and the command-line interface. The `OpenAIHelper` class can be extended to add more functions and encapsulates the API call logic for reuse.

The `automated_labeling_process` function is now the entry point for the automated labeling process in the pipeline, taking command-line arguments and utilizing the `OpenAIHelper` class. This function can be modified or extended for use with other types of pipelines or automation frameworks.

<details><summary>Metadata</summary>

- Duration: 52357 ms
- Datetime: 2024-01-05T10:41:34.936345
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
Does that cover the full functionality of the original?

**Response:**
The provided class-based solution captures the essence of the original functionality but with a more structured approach, designed to eliminate the potential infinite loop by removing the recursive calls and the unconditional while loop. However, some elements from the original code are not covered or are significantly changed in the new solution:

1. Database operations: The original code appears to have database interactions using SQLite to create a table and insert data, which is not included in the new class-based solution.

2. The `generate_labels` function from the original code is not included in the class-based solution. This function seemed to create labels based on text input using OpenAI's API.

3. Original code's argparse setup allowed for potentially command-line driven application with additional inputs like `--url`, `--title`, `--description`, and `--repo`. These inputs are used to drive the main code loop, which is fundamentally redesigned in the class-based approach.

4. The original code's handling of OpenAI completions with "tools" is not present in the class-based version. The use of tools seems to be an advanced feature that is not directly translated to the class-based solution.

5. The error handling and loop control in the original version (which could lead to an infinite loop) has been replaced with structured exception handling and a clear program entry and exit point.

6. The main program loop in the original code continuously processes labels until a valid list of checked_labels is returned. The new class-based solution does not loop and processes one argument set at a time.

7. The original code is designed to potentially handle multiple data rows from a database in a bulk operation with a limit (`if i > 1000: break`). This bulk operation loop is not present in the class-based solution.

8. There are also printing and logging statements in the original code that serve as debugging or informational purposes, which are not all fully replicated in the class-based version.

To match the full original functionality, the new solution would need to include these missing elements, possibly through additional methods within the `OpenAIHelper` class or auxiliary functions, to handle the database-related tasks and the label generation process as depicted in the original code. The class can be expanded to support bulk operations and could include method parameters or class attributes to manage the state across multiple calls.

<details><summary>Metadata</summary>

- Duration: 24904 ms
- Datetime: 2024-01-05T10:49:25.042073
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

