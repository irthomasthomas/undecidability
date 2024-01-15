**Prompt:**
The following is a user comment about using chatgpt for programming. Based on the user feedback, right a collection of prompt templates. Pay special attention to knowledge you have from 2022 and 2023, as this is likely to be most relevant to prompt engineering. You may also provide advice on the best use of parameters with these prompt templates.


I've been using the openai apis to write and edit code for 3-4 months now. So I think that makes me an old timer (ha!). I have also been building tooling for improving the chat based coding experience [0]. All of this work has given me an opportunity to think about how to work best with GPTs on coding, and I've shared some thoughts about this in the past [1].
Here are some of my thoughts on how to code with chatgpt. Many overlap with topics covered in the Nature article.
  - It really does help to think of chatgpt as a junior coder. I mentioned this in the writeup about my first AI coding project [2]. A bunch of things in this list would also be helpful when working with a junior dev.
  - GPT isn't good at code architecture. It will repeat code and take the shortest, laziest path to coding up your request. You need to walk it through changes like you might with a junior dev. Ask for a refactor to prepare, then ask for the actual change. Spend the time to ask for code quality/structure improvements.
  - Don't copy-and-paste between a chat session and your files. Use a tool like Copilot [3] or aider [0] that will give GPT your code to edit and apply its changes automatically. This is critical as it removes friction and lets you iterate quickly on code with GPT.
  - GPT is amazing at generating fresh new self-contained code. It takes more skill and better tools to work with it to edit existing code.
  - Break down a big change and ask for a series of smaller, self contained steps. This is a smart way to code solo, but really helps GPT succeed at more complex code modifications.
  - GPT has a wide breadth of coding knowledge, and impeccable command of syntax... but it is sometimes overconfident about details. So it will usually choose the right library for a task, but sometimes make an error about the details of the api/method/params. Paste doc snippets or error messages into the chat and it will fix those bugs.
  - GPT is really strong at churning out good boilerplate and roughing in a solution. This reduces the activation energy required to start larger changes or changes which will require unfamiliar libraries/packages/languages. GPT can can quickly prepare the ground for you to do the interesting work.
  - If you can, use gpt-4 (not gpt-3.5-turbo) since it can successfully generate larger, more complicated code changes.

**Response:**
Based on the user feedback provided, I have constructed a collection of prompt templates that can be utilized to harness OpenAI's models for programming tasks. Users should consider their specific needs and modify these templates to best fit their context.

### 1. Code Component Generation Template
```
Please generate a [language] function to achieve [functionality description]. Ensure the function is optimally structured for [performance/scalability/readability]. Include appropriate error handling and comments to explain the logic.
```
_Parameters Advice: Adjust temperature to allow creativity if the task isn't strictly defined but lower it for more precise outputs._

### 2. Code Refactoring Template
```
Here's a snippet of [language] code: [code snippet]. Could you refactor this for better [performance/maintainability/scalability], following [specific code principles or patterns]?
```
_Parameters Advice: Use a lower temperature setting to get more precise and conservative refactoring._

### 3. Integration of Tooling and APIs Template
```
I'm using [tool/AI assistant] for coding and have this code snippet: [code snippet]. How would you integrate changes directly from the tool rather than copying and pasting between sessions?
```
_Parameters Advice: Set the temperature medium to allow for some creative integration solutions._

### 4. Error Debugging Template
```
I'm encountering this issue when running my [language] code: [error message]. The code snippet causing the issue is: [code snippet]. Can you identify the problem and suggest a correction?
```
_Parameters Advice: Keep a low temperature to prioritize accuracy in debugging._

### 5. Step-by-Step Code Modification Template
```
I need to make changes to my code base for [feature/functionality]. Can we break this down into smaller, manageable steps? What would be the first step you would recommend?
```
_Parameters Advice: Allow for a medium temperature to balance structure and creativity in the stepwise approach._

### 6. Library and API Usage Template
```
Could you provide an example of how to use [library/API] in [language] for [task]? Please include the correct usage of methods and parameters as they are described in the official documentation.
```
_Parameters Advice: A lower temperature is preferred for accuracy regarding library/API specifications._

### 7. Boilerplate Code Generation Template
```
I am starting a new project that involves [project description]. Can you write the initial boilerplate code in [language], using [framework/library] that sets up a basic structure for the project?
```
_Parameters Advice: Temporarily increase temperature to facilitate the generation of diverse boilerplate structures._

### 8. Complex Code Change Template (for GPT-4)
```
Using GPT-4, I would like to implement a complex change involving [describe change]. The current code base is structured as follows: [brief description or code snippet]. Can you outline a plan for this implementation and start with the first step in the code?
```
_Parameters Advice: GPT-4 may handle complexity better; however, keep a moderate temperature to ensure controlled outputs while still leveraging its capabilities.

### General Advice
- Be explicit with your requests and provide clear context.
- Include any specific coding standards or patterns you want to adhere to in your prompt.
- Break down large tasks into smaller prompts to allow for more focused code outputs.
- Continuously validate the code provided by the AI before integrating it into your project.
- Utilize iterative prompting for refactoring and improvements—don't expect perfection in the first response.
- Be cautious of overconfidence in the AI's responses and always validate against your knowledge and official documentation.

<details><summary>Metadata</summary>

- Duration: 15487 ms
- Datetime: 2023-11-08T21:55:01.980894
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

