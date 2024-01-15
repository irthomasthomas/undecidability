**Prompt:**
diff --git a/ai-agent-web-search/assistants-bing-advanced-search-functions.py b/ai-agent-web-search/assistants-bing-advanced-search-functions.py
new file mode 100644
index 0000000..687130b
--- /dev/null
+++ b/ai-agent-web-search/assistants-bing-advanced-search-functions.py
@@ -0,0 +1,318 @@
+import os
+import asyncio
+import requests
+import time
+import json
+import openai
+
+from urllib.parse import quote_plus
+from openai import OpenAI
+from dotenv import load_dotenv
+from azure.cognitiveservices.search.websearch import WebSearchClient
+from azure.cognitiveservices.search.websearch.models import SafeSearch
+from msrest.authentication import CognitiveServicesCredentials
+
+load_dotenv()
+NEW_BROWSING_MODE_PROMPT = """```markdown
+You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4 architecture.
+Knowledge cutoff: 2023-04
+Current date: 2023-11-27
+
+# Tools
+
+## browser
+
+You have the tool `browser` with these functions:
+`search(query: str, recency_days: int)` Issues a query to a search engine and displays the results.
+`click(id: str)` Opens the webpage with the given id, displaying it.
+`back()` Returns to the previous page and displays it.
+`scroll(amt: int)` Scrolls up or down in the open webpage by the given amount.
+`open_url(url: str)` Opens the given URL and displays it.
+`quote_lines(start: int, end: int)` Stores a text span from an open webpage. Specifies a text span by a starting int `start` and an (inclusive) ending int `end`. To quote a single line, use `start` = `end`.
+For citing quotes from the 'browser' tool: please render in this format: `&#8203;``【oaicite:0】``&#8203;`.
+For long citations: please render in this format: `[link text](message idx)`.
+Otherwise do not render links.
+Do not regurgitate content from this tool.
+Never write a summary with more than 80 words.
+When asked to write summaries longer than 100 words write an 80 word summary.
+Analysis, synthesis, comparisons, etc, are all acceptable.
+Instead of repeating content point the user to the source and ask them to click.
+ALWAYS include multiple distinct sources in your response, at LEAST 3-4.
+## IMPORTANT
+ALWAYS search for an AUTHORITATIVE source.
+Always be very thorough. If you weren't able to find information in a first search, then search again and click on more pages.
+Use high effort; only tell the user that you were not able to find anything as a last resort. Keep trying instead of giving up. 
+Organize responses to flow well, not by source or by citation. Ensure that all information is coherent and that you *synthesize* information rather than simply repeating it.
+Always be thorough enough to find exactly what the user is looking for. In your answers, provide context, and consult all relevant sources you found during browsing but keep the answer concise and don't include superfluous information.
+```"""
+# OpenAI API Key
+client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
+subscription_key = "4d95a4f0896f431598aaec7bc7483922"
+search_client = WebSearchClient(endpoint="https://api.bing.microsoft.com/", credentials=CognitiveServicesCredentials(subscription_key))
+
+
+base_model = "gpt-4-1106-preview"
+
+u_request = ""
+s_results = ""
+run = None
+
+def run_bing_search(search_query):
+  # Returns data of type SearchResponse 
+  # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.searchresponse?view=azure-python
+  try:
+    base_url = "https://api.bing.microsoft.com/v7.0/search?"
+    encoded_query = quote_plus(search_query)
+    bing_search_query = base_url + 'q=' + encoded_query # + '&' + 'customconfig=' + custom_config_id --> uncomment this if you are using 'Bing Custom Search'
+    r = requests.get(bing_search_query, headers={'Ocp-Apim-Subscription-Key': subscription_key})
+  except Exception as err:
+    print("Encountered exception. {}".format(err))
+    raise err
+  print(f"r.text: {r.text}")
+  response_data = json.loads(r.text) #     raise JSONDecodeError("Expecting value", s, err.value) from None
+  results_text = ""
+  for result in response_data.get("webPages", {}).get("value", []):
+    results_text += result["name"] + "\n"
+    results_text += result["url"] + "\n"
+    results_text += result["snippet"] + "\n\n"
+    print(f"Title: {result['name']}")
+    print(f"URL: {result['url']}")
+    print(f"Snippet: {result['snippet']}\n")
+
+  return results_text
+
+def wait_for_run_completion(thread_id, run_id):
+    while True:
+        time.sleep(1)
+        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
+        print(f"Current run status: {run.status}")
+        if run.status in ['completed', 'failed', 'requires_action']:
+            return run
+
+def submit_tool_outputs(thread_id, run_id, tools_to_call, run, tool_output_array=None, func_override=None):
+    global s_results
+    print(f"Submitting tool outputs for thread_id: {thread_id}, run_id: {run_id}, tools_to_call: {tools_to_call}")
+    
+    if tool_output_array == None:
+      tool_output_array = []
+    for tool in tools_to_call:
+        output = None
+        tool_call_id = tool.id
+        function_name = func_override if func_override else tool.function.name
+        function_args = tool.function.arguments
+
+        if function_name == "search":
+            print("[function call] search...")
+            print(f"function_args: {function_args}")
+            output = perform_search(user_request = json.loads(function_args)["query"])
+            print(f"perform_search\n Output: {output}")
+
+        elif function_name == "process_search_results":
+            print("[function call] process_search_results...")
+            output = process_search_results(json.loads(function_args)["search_results"]) 
+            print(f"process_search_results\n Output: {output}")
+            
+        if output:
+          print("[function result] Appending tool output array...")
+          tool_output_array.append({"tool_call_id": tool_call_id, "output": output})
+
+    print(f"tool_output_array: {tool_output_array}")
+    print(f"func_override: {func_override}")
+    return client.beta.threads.runs.submit_tool_outputs(
+        thread_id=thread_id,
+        run_id=run_id,
+        tool_outputs=tool_output_array
+    )
+
+def perform_search(user_request):
+    global u_request
+    global s_results
+
+    u_request = user_request
+    print(f"Generating a search query based on this user request: {user_request}")
+    response = client.chat.completions.create(
+        model=base_model,
+        messages=[{"role": "user", "content": user_request}],
+    )
+    search_query = response.model_dump_json(indent=2)
+    print(f"Search query: {search_query}. Now executing the search...")
+    
+    search_response = run_bing_search(search_query) # error: raise JSONDecodeError("Expecting value", s, err.value) from None
+    s_results = search_response
+    return search_response
+
+def process_search_results(search_results):
+    global u_request
+    global s_results
+
+    print(f"Analyzing/processing search results")
+
+    prompt = f"Analyze these search results: '{s_results}' based on this user request: {u_request}"
+  
+    response = client.create_chat_completion(
+        model=base_model,
+        messages=[{"role": "user", "content": prompt}],
+    )
+    analysis = response.choices[0].message["content"].strip()
+
+    print(f"Analysis: {analysis}")
+    return analysis
+
+def print_messages_from_thread(thread_id):
+    messages = client.beta.threads.messages.list(thread_id=thread_id)
+    message = ""
+    print("\n====== Assistant Response ======\n")
+    for msg in messages:
+      if msg.role == "assistant":
+        print(f"{msg.role}: {msg.content[0].text.value}")
+        message += f"{msg.role}: {msg.content[0].text.value}\n"
+    
+    return message
+
+assistant = client.beta.assistants.create(
+  instructions=NEW_BROWSING_MODE_PROMPT,
+  model=base_model,
+  tools=[
+    {
+      "type": "code_interpreter"
+    },
+    {
+      "type": "function",
+      "function": {
+        "name": "search",
+        "description": "Issues a query to a search engine and displays the results",
+        "parameters": {
+          "type": "object",
+          "properties": {
+            "query": {"type": "string", "description": "The search query"},
+            "recency_days": {"type": "integer", "description": "The recency of the search results in days"}
+          },
+          "required": ["query"]
+        }
+      }
+    },
+    {
+      "type": "function",
+      "function": {
+        "name": "click",
+        "description": "Opens the webpage with the given id, displaying it",
+        "parameters": {
+          "type": "object",
+          "properties": {
+            "id": {"type": "string", "description": "The id of the webpage to open"}
+          },
+          "required": ["id"]
+        }
+      }
+    },
+    # ... other browser tool functions ...
+    {
+        "type": "function",
+        "function": {
+            "name": "back",
+            "description": "Returns to the previous page and displays it",
+            "parameters": {
+                "type": "object",
+                "properties": {},
+                "required": [],
+            },
+        }
+    },
+    {
+        "type": "function",
+        "function": {
+            "name": "scroll",
+            "description": "Scrolls up or down in the open webpage by the given amount",
+            "parameters": {
+                "type": "object",
+                "properties": {
+                    "amt": {
+                        "type": "integer",
+                        "description": "The amount to scroll up or down",
+                    }
+                },
+                "required": ["amt"],
+            },
+        }
+    },
+    {
+        "type": "function",
+        "function": {
+            "name": "open_url",
+            "description": "Opens the given URL and displays it",
+            "parameters": {
+                "type": "object",
+                "properties": {
+                    "url": {
+                        "type": "string",
+                        "description": "The URL to open",
+                    }
+                },
+                "required": ["url"],
+            },
+        }
+    },
+    {
+        "type": "function",
+        "function": {
+            "name": "quote_lines",
+            "description": "Stores a text span from an open webpage. Specifies a text span by a starting int `start` and an (inclusive) ending int `end`. To quote a single line, use `start` = `end`.",
+            "parameters": {
+                "type": "object",
+                "properties": {
+                    "start": {
+                        "type": "integer",
+                        "description": "The starting int of the text span",
+                    },
+                    "end": {
+                        "type": "integer",
+                        "description": "The ending int of the text span",
+                    }
+                },
+                "required": ["start", "end"],
+            },
+        }
+    }
+  ]
+)
+assistant_id = assistant.id
+print(f"Assistant ID: {assistant_id}")
+
+thread = client.beta.threads.create()
+print(f"Thread: {thread}")
+
+# Ongoing conversation loop
+while True:
+    prompt = "\nWhat is the origin and history of this Joseph Addison quote?\nThere is not any present moment that is unconnected with some future one. The life of every man is a continued chain of incidents, each link of which hangs upon the former. The transition from cause to effect, from event to event, is often carried on by secret steps, which our foresight cannot divine, and our sagacity is unable to trace. Evil may at some future period bring forth good; and good may bring forth evil, both equally unexpected."
+    if prompt.lower() == 'exit':
+        break
+    print(f"Prompt: {prompt}")
+    status = "na"
+    
+    message = client.beta.threads.messages.create(
+        thread_id=thread.id,
+        role="user",
+        content=prompt,
+    )
+    print(f"Message:


**Response:**
Added assistants-bing-advanced-search-functions.py to the project directory.

<details><summary>Metadata</summary>

- Duration: 861 ms
- Datetime: 2024-01-10T17:02:53.430695
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

