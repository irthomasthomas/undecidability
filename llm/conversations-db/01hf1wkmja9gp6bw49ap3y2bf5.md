**Prompt:**
Format this GH Issues markdown correctly:

- [ ] [Get just the code from code-interpreter (without running the code) - API - OpenAI Developer Forum](https://community.openai.com/t/get-just-the-code-from-code-interpreter-without-running-the-code/490501/2)

<details>
    <summary>Quote</summary>    
    The way code interpreter works is that it outputs its AI generated code as a function call to the tool recipient.

It writes code in response to any user request that would seem best computed or which specifically refers to the python features or the file mount environment.

The function automatically sets up a sandbox environment for the session and runs the code, returning the value of the final output line to the AI. (it actually should output anything generated within the notebook, but the AI seems trained to put its “return value” at the end of all its code writing.

So no, you don’t get unexecuted code unless you ask the AI to write code specifically for you, just as all GPT-4 can do (and likely better on non-turbo).
    
    </details>

**Response:**
Here's the formatted GitHub Issues markdown:

```markdown
- [ ] [Get just the code from code-interpreter (without running the code) - API - OpenAI Developer Forum](https://community.openai.com/t/get-just-the-code-from-code-interpreter-without-running-the-code/490501/2)

<details>
  <summary>Quote</summary>
  
  > The way code interpreter works is that it outputs its AI generated code as a function call to the tool recipient.
  >
  > It writes code in response to any user request that would seem best computed or which specifically refers to the python features or the file mount environment.
  >
  > The function automatically sets up a sandbox environment for the session and runs the code, returning the value of the final output line to the AI. (it actually should output anything generated within the notebook, but the AI seems trained to put its “return value” at the end of all its code writing.
  >
  > So no, you don’t get unexecuted code unless you ask the AI to write code specifically for you, just as all GPT-4 can do (and likely better on non-turbo).

</details>
```

This markdown will create a task list item with a link, and a collapsible section containing a blockquote.

<details><summary>Metadata</summary>

- Duration: 8147 ms
- Datetime: 2023-11-12T13:47:37.462959
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

