TODO: add readme about agents.
Agent Tools: 
vision - image to: code, data, diagram. Screen activity: timestamp generation for screen recording.
TRIALS - When the action of an agent is challenged by another agent, trials are held, culminating in a verdict vote using logprobs.
code understanding
code generation
KDE INTEGRATION
git integration
log to markdown: activity, project, task progress, cli i/o, file i/o, web i/o all sent to summariser to append to summary log html/md
READ-ONLY FILESYSTEM ACCESS for the agent.
WRITE ACCESS TO ONE DIRECTORY.
BUDGET: Set $ budgets for each agent. and track costs.
AI Chatbot: Ask for assistance from an AI.

gorilla LLM with API understanding and code generation for connecting to other APIs.

- [ ] color tokens based on logprobs. (red for low, green for high)
- [ ] For code generation, use logit bias to force first token to be a '#'.
- [ ] update label maker to use function calling api.
- [ ] update web search agent to use bing custom search
- [ ] add issues search to issue maker
- [ ] cache github issues in memory for faster searching.
- [ ] sort out undecidabilty of logprobs. # Q: what is this? # A: it's when the logprobs are too close to each other to decide which is the best.
- [ ] # TODO: use logprobs to decide which agent to use.
- [ ] use embeddings to find man pages for commands.
- [ ] upgrade man page llm templates to be dynamic.
- [ ] embed terminal history in llm.
- [ ] 