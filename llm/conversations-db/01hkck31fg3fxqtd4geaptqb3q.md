**Prompt:**
Fix this code to stop it getting stuck in a loop when get_issues_labels_list is called. 
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
The code provided has a recursive call in `openai_pick_labels_function` where it calls itself if the `tool_call.function.name` is `"openai_pick_labels_function"`. This recursive call does not have a base case or termination condition, which can lead to an infinite loop.

To fix this, remove the recursive call and handle the response from the `get_issues_labels_list` function directly. Here's the corrected section of the `openai_pick_labels_function`:

```python
# ... [previous code] ...

if tool_calls:
    tool_calls_copy = tool_calls.copy()
    available_functions = {
        "get_issues_labels_list": get_issues_labels_list,
        # "openai_pick_labels_function": openai_pick_labels_function, # Remove this line to prevent recursion
    }
    messages.append(response_message)
    for tool_call in tool_calls_copy:
        if tool_call.function.name == "get_issues_labels_list":
            tool_calls.remove(tool_call)
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

    # After processing all tool calls, we should have the labels_dict populated
    # Now we can proceed with selecting labels without calling openai_pick_labels_function again

    # ... [rest of the code] ...
```

By removing the recursive call, the function will not call itself again, thus preventing the infinite loop. The function should now process the tool calls, update the `messages` list with the responses, and then proceed with the logic to select labels based on the `labels_dict` obtained from the `get_issues_labels_list` function.

<details><summary>Metadata</summary>

- Duration: 28172 ms
- Datetime: 2024-01-05T10:35:22.467435
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

