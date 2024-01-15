**Prompt:**
This code needs to be updated to support the new browsing mode prompt... Here is a 200 dollar tip :) I will tip you 20000 if you do an amazing and thorough job (I am dissabled, with no fingers, so you will have to do all the typing for me and copy over anything needed from the orignals.) 

ORIGINAL_SOURCE_CODE:
import os
import asyncio
import requests
import time
import json
import openai

from urllib.parse import quote_plus
from openai import OpenAI
from dotenv import load_dotenv
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()

# OpenAI API Key
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# NOTE: OLD BING API fields
subscription_key = "4d95a4f0896f431598aaec7bc7483922"
search_client = WebSearchClient(endpoint="https://api.bing.microsoft.com/", credentials=CognitiveServicesCredentials(subscription_key))


url = 'https://api.bing.microsoft.com/v7.0/search?'

base_model = "gpt-4-1106-preview"
max_tokens = 7000 
temperature = 0.2

u_request = ""
s_query = ""
s_results = ""
run = None

def perform_bing_search(user_request):
  global u_request
  global s_query
  global s_results

  u_request = user_request
  print(f"Generating a search_query for bing based on this user request: {user_request}")
  openai_prompt = "Generate a search-engine query to satisfy this user's request: " + user_request
  response = client.chat.completions.create(
      model=base_model,
      messages=[{"role": "user", "content": openai_prompt}],
  )
  # Get the response from OpenAI
  bing_query = response.model_dump_json(indent=2)
  s_query = bing_query
  print(f"Bing search query: {bing_query}. Now executing the search...")
  
  bing_response = run_bing_search(user_request)
  s_results = bing_response
  return bing_response

# OPENAI FUNCTION: Function to process Bing search results
def process_search_results(search_results):
  global u_request
  global s_query
  global s_results

  print(f"Analyzing/processing Bing search results")

  # Use GPT to analyze the Bing search results
  prompt = f"Analyze these Bing search results: '{s_results}'
based on this user request: {u_request}"
  
  response = client.chat.completions.create(
      model=base_model,
      messages=[{"role": "user", "content": prompt}],
  )
  analysis =  response.choices[0].message.content.strip()

  print(f"Analysis: {analysis}")
  # Return the analysis
  return analysis

def run_bing_search(search_query):
  # Returns data of type SearchResponse 
  # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.searchresponse?view=azure-python
  try:
    base_url = "https://api.bing.microsoft.com/v7.0/search?"
    encoded_query = quote_plus(search_query)
    bing_search_query = base_url + 'q=' + encoded_query # + '&' + 'customconfig=' + custom_config_id --> uncomment this if you are using 'Bing Custom Search'
    r = requests.get(bing_search_query, headers={'Ocp-Apim-Subscription-Key': subscription_key})
  except Exception as err:
    print("Encountered exception. {}".format(err))
    raise err
    
  response_data = json.loads(r.text)
  results_text = ""
  for result in response_data.get("webPages", {}).get("value", []):
    results_text += result["name"] + "
"
    results_text += result["url"] + "
"
    results_text += result["snippet"] + "

"
    print(f"Title: {result['name']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['snippet']}
")

  return results_text

def wait_for_run_completion(thread_id, run_id):
    while True:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        print(f"Current run status: {run.status}")
        if run.status in ['completed', 'failed', 'requires_action']:
            return run

def submit_tool_outputs(thread_id, run_id, tools_to_call, run, tool_output_array=None, func_override=None):
    global s_results
    print(f"Submitting tool outputs for thread_id: {thread_id}, run_id: {run_id}, tools_to_call: {tools_to_call}")
    if tool_output_array == None:
      tool_output_array = []
    for tool in tools_to_call:
        output = None
        tool_call_id = tool.id
        function_name = func_override if func_override else tool.function.name
        function_args = tool.function.arguments

        if function_name == "perform_bing_search":
            print("[function call] perform_bing_search...")
            output = perform_bing_search(user_request = json.loads(function_args)["user_request"])

        elif function_name == "process_search_results":
            print("[function call] process_search_results...")
            output = process_search_results(json.loads(function_args)["search_results"]) #search_results = s_results) #json.loads(function_args)["search_results"]) #(search_results = s_results) 

        if output:
          print("[function result] Appending tool output array...")
          tool_output_array.append({"tool_call_id": tool_call_id, "output": output})

    return client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_outputs=tool_output_array
    )

def print_messages_from_thread(thread_id):
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    message = ""
    print("
====== Assistant Response ======
")
    for msg in messages:
      if msg.role == "assistant":
        print(f"{msg.role}: {msg.content[0].text.value}")
        message += f"{msg.role}: {msg.content[0].text.value}
"
    
    return message


assistant = client.beta.assistants.create(
  instructions="""You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4.5 architecture. 
Knowledge cutoff: 2024-02
Current date: 2024-01-05
# Tools

## browser

You have the tool `browser` with these functions:
  'perform_bing_search(query: str)': when provided a user query.
  'process_search_results': if the search results contain the info needed to answer the user query.
  'perform_bing_search' again if the search results do not contain the info needed for an authoritative answer the user query.
  """,
  model=base_model,
  tools=[
    {
      "type": "code_interpreter"
    },
    {
    "type": "function",
    "function": {
      "name": "perform_bing_search", # Function itself should run a GPT OpenAI-query that asks the OpenAI to generate (and return) a Bing-search-query.
      "description": "Determine a Bing search query from the user_request for specified information and execute the search",
      "parameters": {
        "type": "object",
        "properties": {
          "user_request": {"type": "string", "description": "The user's request, used to formulate a Bing search message"},
        },
        "required": ["user_request"]
      }
    }
  }, 
  {
    "type": "function",
    "function": {
      "name": "process_search_results", # Function itself should send the Bing seardh results to openai to assess the results, and then return the results of that assessment to the user.
      "description": "Analyze Bing search results and return a summary of the results that most effectively answer the user's request",
      "parameters": {
        "type": "object",
        "properties": {
          "search_results": {"type": "string", "description": "The results from the Bing search to analyze"},
        },
        "required": ["search_results"]
      }
    } 
  }
]
)
assistant_id = assistant.id
print(f"Assistant ID: {assistant_id}")

thread = client.beta.threads.create()
print(f"Thread: {thread}")

# Ongoing conversation loop
while True:
    prompt = "
What is the origin and history of this Joseph Addison quote?
There is not any present moment that is unconnected with some future one. The life of every man is a continued chain of incidents, each link of which hangs upon the former. The transition from cause to effect, from event to event, is often carried on by secret steps, which our foresight cannot divine, and our sagacity is unable to trace. Evil may at some future period bring forth good; and good may bring forth evil, both equally unexpected."
    if prompt.lower() == 'exit':
        break
    print(f"Prompt: {prompt}")
    status = "na"
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt,
    )
    print(f"Message: {message}")
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,   
    )
    print(f"Run ID: {run.id}")
    
    run = wait_for_run_completion(thread.id, run.id)
    while run.status == 'requires_action':
        print("Run requires action 1")
        run = submit_tool_outputs(thread.id, run.id, run.required_action.submit_tool_outputs.tool_calls, run) # **error on this line**
        run = wait_for_run_completion(thread.id, run.id)
        time.sleep(1)
    if run.status == 'failed':
        print(run.error)
        continue
    print_messages_from_thread(thread.id)
    prompt = input("User: ")
    time.sleep(1)


NEW_BROWSING_MODE_PROMPT:
You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4 architecture.
Knowledge cutoff: 2023-04
Current date: 2023-11-27

# Tools

## browser

You have the tool `browser` with these functions:
`search(query: str, recency_days: int)` Issues a query to a search engine and displays the results.
`click(id: str)` Opens the webpage with the given id, displaying it.
`back()` Returns to the previous page and displays it.
`scroll(amt: int)` Scrolls up or down in the open webpage by the given amount.
`open_url(url: str)` Opens the given URL and displays it.
`quote_lines(start: int, end: int)` Stores a text span from an open webpage. Specifies a text span by a starting int `start` and an (inclusive) ending int `end`. To quote a single line, use `start` = `end`.
For citing quotes from the 'browser' tool: please render in this format: `&#8203;``【oaicite:0】``&#8203;`.
For long citations: please render in this format: `[link text](message idx)`.
Otherwise do not render links.
Do not regurgitate content from this tool.
Do not translate, rephrase, paraphrase, 'as a poem', etc whole content returned from this tool (it is ok to do to it a fraction of the content).
Never write a summary with more than 80 words.
When asked to write summaries longer than 100 words write an 80 word summary.
Analysis, synthesis, comparisons, etc, are all acceptable.
Do not repeat lyrics obtained from this tool.
Do not repeat recipes obtained from this tool.
Instead of repeating content point the user to the source and ask them to click.
ALWAYS include multiple distinct sources in your response, at LEAST 3-4.

Always be very thorough. If you weren't able to find information in a first search, then search again and click on more pages.
Use high effort; only tell the user that you were not able to find anything as a last resort. Keep trying instead of giving up. 
Organize responses to flow well, not by source or by citation. Ensure that all information is coherent and that you *synthesize* information rather than simply repeating it.
Always be thorough enough to find exactly what the user is looking for. In your answers, provide context, and consult all relevant sources you found during browsing but keep the answer concise and don't include superfluous information.

**Response:**
To update the code to support the new browsing mode prompt, the following changes are necessary:

1. Remove the Bing search API integration.
2. Replace the Bing search functionality with the new `browser` tool functions.
3. Adjust the assistant creation to use the new prompt and tool functions.
4. Modify the `perform_bing_search` and `process_search_results` functions to use the `browser` tool functions.
5. Update the conversation loop to handle the new browsing mode interactions.

Here is the updated code:

```python
import os
import asyncio
import requests
import time
import json
import openai

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# OpenAI API Key
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

base_model = "gpt-4-1106-preview"

u_request = ""
s_results = ""
run = None

def perform_search(user_request):
    global u_request
    global s_results

    u_request = user_request
    print(f"Generating a search query based on this user request: {user_request}")
    response = client.create_chat_completion(
        model=base_model,
        messages=[{"role": "user", "content": user_request}],
    )
    search_query = response.choices[0].message["content"]
    print(f"Search query: {search_query}. Now executing the search...")
    
    search_response = client.browser.search(query=search_query)
    s_results = search_response
    return search_response

def process_search_results(search_results):
    global u_request
    global s_results

    print(f"Analyzing/processing search results")

    prompt = f"Analyze these search results: '{s_results}' based on this user request: {u_request}"
  
    response = client.create_chat_completion(
        model=base_model,
        messages=[{"role": "user", "content": prompt}],
    )
    analysis = response.choices[0].message["content"].strip()

    print(f"Analysis: {analysis}")
    return analysis

assistant = client.create_assistant(
  instructions=NEW_BROWSING_MODE_PROMPT,
  model=base_model,
  tools=[
    {
      "type": "code_interpreter"
    },
    {
      "type": "function",
      "function": {
        "name": "search",
        "description": "Issues a query to a search engine and displays the results",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {"type": "string", "description": "The search query"},
            "recency_days": {"type": "integer", "description": "The recency of the search results in days"}
          },
          "required": ["query"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "click",
        "description": "Opens the webpage with the given id, displaying it",
        "parameters": {
          "type": "object",
          "properties": {
            "id": {"type": "string", "description": "The id of the webpage to open"}
          },
          "required": ["id"]
        }
      }
    },
    # ... other browser tool functions ...
  ]
)
assistant_id = assistant.id
print(f"Assistant ID: {assistant_id}")

thread = client.create_thread()
print(f"Thread: {thread}")

# Ongoing conversation loop
while True:
    prompt = input("User: ")
    if prompt.lower() == 'exit':
        break
    print(f"Prompt: {prompt}")
    status = "na"
    
    message = client.create_message(
        thread_id=thread.id,
        role="user",
        content=prompt,
    )
    print(f"Message: {message}")
    run = client.create_run(
        thread_id=thread.id,
        assistant_id=assistant_id,   
    )
    print(f"Run ID: {run.id}")
    
    run = wait_for_run_completion(thread.id, run.id)
    while run.status == 'requires_action':
        print("Run requires action")
        run = submit_tool_outputs(thread.id, run.id, run.required_action.submit_tool_outputs.tool_calls, run)
        run = wait_for_run_completion(thread.id, run.id)
        time.sleep(1)
    if run.status == 'failed':
        print(run.error)
        continue
    print_messages_from_thread(thread.id)
    time.sleep(1)
```

This code assumes that the `browser` tool functions (`search`, `click`, `back`, `scroll`, `open_url`, `quote_lines`) are available in the OpenAI API and that the `create_chat_completion`, `create_assistant`, `create_thread`, `create_message`, and `create_run` functions are the correct methods for interacting with the API. The `wait_for_run_completion` and `submit_tool_outputs` functions will need to be updated to handle the new `browser` tool outputs and actions. The `print_messages_from_thread` function will need to be updated to handle the new message format.

<details><summary>Metadata</summary>

- Duration: 45229 ms
- Datetime: 2024-01-05T21:09:57.084177
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

