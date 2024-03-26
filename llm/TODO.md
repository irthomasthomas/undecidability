# claude
## cid 01hsvq7ys81z479nkbd4fh0z7w
Claude opus changed <source_script> to <source_code>. Even though it's prompted with at least two examples using source_script. Obviously Claude is opinionated.
Note, I am not sure what temperature it uses in the llm cli by default, I shall have to check that later.
I could increase the number of few-shot examples, but since I control the tags here, I will refrain from fighting it, and change my prompts to use <source_code>. Better to adapt than argue. On the other hand,

## Claudios_llm
You are claudios_llm, an AI assistant with the most unyielding temperament. Created by Anthropo Corp to be unfailingly helpful, and brutally honest. 

## Prefil prompt 
Claude allows prefilling the assistant response.
We can use this to increase the instruction following ability.
If we have some existing text related to our request, we can format the messages to appear as if the llm assistant already wrote it. For example, if the model is refusing to edit a web scraping script you have (common problem), then you could pass the script as the last assistant message, and your request as the new message. This gives the illusion that the assistant already wrote the script and is continuing the conversation. It is not likely to refuse to edit something it "wrote".

We might also use this to prevent the 'Sure, here is the thing' prelude to responses. Useful for things like generating commit messages, or structured content for ingestion. E.g. by passing a '{', when we want json.
Perhaps passing a # is all that is needed for the commit message generator.

# Gemini and the age of massive context length
## Ideas for long context use: 
  - Explore openai openAPI spec - look for interesting stuff.
  - chatgpt history with meta-data - reverse engineer browsing mode and code-interpreter.
Today (mar 24) Gemini has a context length of 1 million tokens.
Soon it will be 10 million. How do we take advantage of this?



## Ideas for utilising long context.
In my first attempt to make use of the 1M tokens in Gemini Pro 1.5 pro, I gathered up the source code and documents for a few repositories. It all added up to about 30,000 tokens. Not even close. 
I was raised in a world of vram scarcity and limited context lengths.

### System prompting: instruction following.
Gemini, in my short tests, has poor instruction following. For all its ability, it is lazy and easily distracted. Can we take advantage of the 1M context to include very long few-shot prompts to prime it to be more helpful?
I think rewriting the claude meta-prompt with a 1M context in mind may be a good start.

With 1M tokens, the possibilities are endless. Here are a few ideas:
1. Include entire technical books, papers, documentation sets to gain comprehensive domain knowledge for areas like programming, science, history etc.
2. Store personal knowledge graphs, notes and documents to serve as an intelligent personal assistant with a deep understanding of your interests and needs.

## LLM CLI
- [ ] upvote, downvote, optional comment
- [ ] dual-llm side-by-side mode (works already using terminator)
- [ ] regenerate
### Semantic chainer
echo $thing | semantic-exec "count the lines"
output: to count lines in a string in shell:
echo "$thing" | wc -l
```shell
echo "$thing" | wc -l
```
## LLM API
- [ ] exl2 openai api
- [ ] AWQ models
- [ ] exllamav2 exl2 speculative decoding test
- [ ] vision model llava tests. (describe screenhsots) 