## This repository is a testing ground for my ideas. Do not expect anything to work (or even make sense).
### The issues for this repository contain not my repository issues, but my bookmarks, thoughts and ideas
### [https://github.com/irthomasthomas/undecidability/issues](https://github.com/irthomasthomas/undecidability/issues)
### The issues here are operated by an custom-built AI issues assistant, the source-code for which you can find here: [https://github.com/irthomasthomas/label-maker](https://github.com/irthomasthomas/label-maker)

# AI Web Search Agent

This repository contains a web search agent that recreates the sophisticated browsing mode from ChatGPT's December 2023 release. The agent utilizes the OpenAI API and Bing Custom Search API to perform web searches and navigate through search results, providing a ChatGPT-like browsing experience for the Linux terminal or any Python environment.

## Key Features

- `WebBrowser` class to handle search, click, back, scroll, and quote_lines actions
- Integration with OpenAI and Bing Custom Search APIs for web searches and webpage content retrieval
- Generation of relevant Bing search queries based on the user's question using the `generate_bing_queries_for_user_question` function
- Orchestration of the web search process through the `web_search` function, including querying the model, processing search results, and navigating the browser
- Detailed system prompt (`BROWSING_MODE_PROMPT`) to guide the agent's behavior, emphasizing thoroughness, high effort, and synthesis of information

## Repository Structure

- `agents/`: Contains various agent scripts and related files
  - `multi-llm-code-improver-2.sh`: Bash script for multi-LLM code improvement logic
  - `search/`: Directory for web search-related scripts
    - `bing-custom-search-ai-agent.py`: The main web search agent script
    - `web-search-query-resources.md`: Markdown document aggregating web search query resources
  - `sql-agent/`: Directory for SQL-related scripts and files
    - `github-issues.db`: SQLite database for GitHub issues
    - `steampipe-example-md`: Example markdown on database utilization
- `nyxt/`: Contains Nyxt browser configuration and plugin files
  - `config.lisp`: Nyxt's Lisp configuration file
  - `nyxt-browser-gh-issues-plugin.lisp`: Plugin for handling GitHub issues within Nyxt browser
- `groq-chat.py`: Python script demonstrating Groq API interaction for generating chat completions

## Additional Features

- SQL queries for retrieving data from GitHub issues and inserting data into a separate database
- Shell command for embedding data with specified parameters
- `get-buffer-text` Lisp function for retrieving buffer text content in Nyxt browser
- `cmd-result` internal page for displaying command execution results in Nyxt browser
- `buf-text-to-pipe-cmd` command for executing shell commands with buffer text in Nyxt browser
- Enhanced `gh-selection-to-issue` command for creating GitHub issues using escaped selection text via a specified Python script
- KDE system monitor custom page for monitoring system resources
- CLI database entry script with a function for deleting entries
- Guide for running untrusted shell code
- Script for downloading and storing GitHub issues for fast access, with periodic checks and manual triggers
- Hugging Face Transformers and PEFT deep dive guide and code explanation
- Markdown formatting guide for search results and tricks for enhancing GitHub READMEs
- Shell functions and LLM code for various tasks

