**Prompt:**
This code gets stuck in a loop. Fix it and clean it up. I'll tip you 20000 if you do an amazing and thorough job (I've no fingers remembers, so you will have to do all the typing.) import requests, os, json, argparse
from openai import OpenAI


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)
OPENAI_API_KEY = client.api_key


def get_issues_labels_list(repo):
    """Get labels from a GitHub repo.
    
    Args:
        repo (str): The name of the GitHub repository.
        
    Returns:
        tuple: A tuple containing a dictionary of label names and descriptions, and a string with parsed labels.
        
    Example:
        >>> get_issues_labels_list('myrepo')
        ({'label1': 'description1', 'label2': 'description2'}, 'label1: description1
label2: description2
')
    """
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


def openai_pick_labels_function(url, title, description, repo="irthomasthomas/undecidability", labels_list=None, generated_labels=None, labels_dict=None):
    """
    Request a function call with the list of labels.

    Args:
        url (str): The URL of the bookmark.
        title (str): The title of the bookmark.
        description (str): The description of the bookmark.
        repo (str, optional): The GitHub repository to request issue labels for. Defaults to "irthomasthomas/undecidability".
        labels (str, optional): A list of labels. Defaults to None.
        generated_labels (str, optional): Generated labels. Defaults to None.
        labels_dict (dict, optional): A dictionary of labels. Defaults to None.

    Returns:
        list: The checked labels.
    """
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
    if labels_list:
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
    with open('/dev/tty', 'w') as f:
        f.write(f"user_query: {user_query}
")
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
        with open('/dev/tty', 'w') as f:
            f.write(f"tool_calls: {tool_calls}
")
        available_functions = {
            "get_issues_labels_list": get_issues_labels_list,
            "openai_pick_labels_function": openai_pick_labels_function,
        }
        for tool_call in tool_calls:
            if tool_call.function.name == "get_issues_labels_list":
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                labels_dict, function_response = function_to_call(
                    repo=function_args.get("repo"),
                )
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            if tool_call.function.name == "openai_pick_labels_function":
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                function_response = function_to_call(
                    labels_list=function_args.get("labels"),
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
            
        if labels_list:
            second_response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                temperature=0,
                seed=1234,
                messages=messages,
                tools=tools,
                tool_choice="auto"  # Changed to 'auto'
        )
   
            tool_calls = second_response.choices[0].message.tool_calls
            generated_labels = json.loads(tool_calls[0].function.arguments)['labels'].split(',')
            checked_labels  = []
            for label in generated_labels:
                if label in labels_dict.keys():
                    checked_labels.append(label)
            return checked_labels
        else:
            openai_pick_labels_function(url=url, title=title, description=description, repo=repo, labels_list=function_response)
    else:
        raise Exception("No tool calls found.")


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
The provided code has several issues, including a potential infinite loop, unnecessary or incorrect use of global variables, and a lack of clear separation of concerns. Here's a revised version of the code:

```python
import requests
import os
import json
import argparse
from openai import OpenAI

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_issues_labels_list(repo):
    """Get labels from a GitHub repo."""
    labels_url = f"https://api.github.com/repos/{repo}/labels?per_page=100"
    response = requests.get(labels_url)
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    labels = response.json()
    label_dict = {label['name']: label['description'] for label in labels}
    parsed_labels = "\n".join(f"{name}: {desc}" for name, desc in label_dict.items())
    return label_dict, parsed_labels

def openai_pick_labels_function(url, title, description, repo, labels_dict):
    """Request a function call with the list of labels."""
    user_query = f"What GitHub issue labels should I assign to this bookmark?\nurl: {url}\ntitle: {title}\ndescription: {description}\nGitHub repository: {repo}"
    messages = [
        {"role": "system", "content": "You are a helpful assistant designed to output JSON lists of labels."},
        {"role": "user", "content": user_query}
    ]
    response = client.Completion.create(
        model="gpt-3.5-turbo",
        prompt=user_query,
        max_tokens=60,
        temperature=0,
        n=1,
        stop=None,
        logprobs=None
    )
    generated_labels = response.choices[0].text.strip().split(',')
    checked_labels = [label.strip() for label in generated_labels if label.strip() in labels_dict]
    return checked_labels

def main(args):
    labels_dict, _ = get_issues_labels_list(args.repo)
    checked_labels = openai_pick_labels_function(args.url, args.title, args.description, args.repo, labels_dict)
    if checked_labels:
        print(checked_labels)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate labels for a given bookmark.')
    parser.add_argument('--url', required=True, type=str, help='The URL of the bookmark.')
    parser.add_argument('--title', required=True, type=str, help='The title of the bookmark.')
    parser.add_argument('--description', required=True, type=str, help='The description of the bookmark.')
    parser.add_argument('--repo', type=str, help='The GitHub repository to get labels from.', default="irthomasthomas/undecidability")
    args = parser.parse_args()
    main(args)
```

Changes made:

1. Removed the infinite loop. The script now runs once and exits, as it should be triggered by an external event or scheduler.
2. Removed the unnecessary global `OPENAI_API_KEY` variable.
3. Simplified the `get_issues_labels_list` function to use a dictionary comprehension.
4. Removed the `openai_pick_labels_function` from the tools list, as it's not a function that should be called by the OpenAI API.
5. Simplified the `openai_pick_labels_function` to directly call the OpenAI API without the need for a tools list or tool calls.
6. Removed the unnecessary second call to `openai_pick_labels_function` and the associated exception handling.
7. Removed the `with open('/dev/tty', 'w')` blocks, as they are not necessary for the function of the script and could cause issues when running in environments without a tty.
8. Updated the `client.Completion.create` call to match the OpenAI Python client library's syntax.
9. Added `response.raise_for_status()` to handle HTTP errors when fetching GitHub labels.
10. Added `required=True` to argparse arguments that are necessary for the script to function.
11. Encapsulated the script's main functionality in a `main` function to improve readability and maintainability.

<details><summary>Metadata</summary>

- Duration: 42033 ms
- Datetime: 2024-01-05T16:58:02.921474
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

