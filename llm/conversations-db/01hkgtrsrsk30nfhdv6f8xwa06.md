**Prompt:**
Fix spelling: I also struggle with how to define it. But I think it's so enigmatic due to the stochastic nature of the beast and unstable prompt following. This morning I saw flashes of AGI, as they say. I implemented a copy of chatgpt browsing mode, as it was last year, before they borked it for efficiency. I kept a copy of their good system prompt from that time and fed it into my own bing search assistants pipeline.

To test it I used a query which old chatgpt browsing mode was able to solve consistently, and current browsing mode fails consistently. Fact checking this quote:

  What is the origin and history of this Joseph Addison quote?
There is not any present moment that is unconnected with some future one...

Every link on page one of google confirms the source as Joseph Addison https://i.imgur.com/wtxW9xS.png

chatgpt with browsing mode says Joseph Addison. My naive replacement using some new assistants api code that someone posted to openai's forum also answered Joseph Addison. https://i.imgur.com/h7XB81c.png

But I knew it could do better. I used a version of the old good prompt and iterated on it, removing all the copyright guardrails cruft. I emplored it to only use authoritative sources and to never give up searching etc. It didn't long before it was telling me that original author was actually NOT Joseph Addison but Hugh Blair. And you would only learn this by reading a book on archive.org https://i.imgur.com/hh6naF7.png 

The problem is it isn't stable, and often fails to find the correct author, even using the exact same prompt and code. Setting to temperature to 0 only works for tokens that are well represented in the training set, using 0 on tokens that it's never seen before will cause it to largely ignore the token. Ask it to right some code for "gpt-3.5-turbo-1106" and it will often reply with "gpt-3.5-turbo" at temperature 0, but increasing to 1 makes it more consistently reply with "gpt-3.5-turbo-1106". It's dropping the 1106 because it's not it's training weights and you kneecapped it's ability to pick uncommon tokens. This is a hard thing to stabalise. New concepts in programming or published research should be given the most attention by us, but the llm's give them the least attention. Tuning it to pick up new terms easier means upping the temperature which also makes it more likely to deviate from the ground truth, which is also undesirable in many tasks.

But I don't think are very far away from stabilising this to a point where I will have no problem calling it AI myself.

Watching the inner monologue of the web search agent was illuminating, and worth implementing just to be able to see and modulate all that. For  example I was shocked to see the way that it detailed the precise quoting it would need to use and advanced keyword modifiers which I didn't even realise where a thing on bing as google dropped those advanced search tools a decade ago.

Watching it's inner monologue is very interesting.

**Response:**
Here's the text with corrected spellings and adjustments for clarity:

I also struggle with how to define it. But I think it's so enigmatic due to the stochastic nature of the beast and unstable prompt-following. This morning, I saw flashes of AGI, as they say. I implemented a copy of ChatGPT browsing mode as it was last year, before they tweaked it for efficiency. I kept a copy of their good system prompt from that time and fed it into my own Bing search assistant's pipeline.

To test it, I used a query which the old ChatGPT browsing mode was able to solve consistently, and current browsing mode fails consistently. Fact-checking this quote:

What is the origin and history of this Joseph Addison quote?
"There is not any present moment that is unconnected with some future one..."

Every link on page one of Google confirms the source as Joseph Addison [image link]

ChatGPT with browsing mode says Joseph Addison. My naive replacement using some new assistant's API code that someone posted to OpenAI's forum also answered Joseph Addison. [image link]

But I knew it could do better. I used a version of the old good prompt and iterated on it, removing all the copyright guardrails cruft. I implored it to only use authoritative sources and to never give up searching, etc. It didn't take long before it was telling me that the original author was actually NOT Joseph Addison but Hugh Blair. And you would only learn this by reading a book on archive.org [image link]

The problem is it isn't stable, and often fails to find the correct author, even using the exact same prompt and code. Setting the temperature to 0 only works for tokens that are well represented in the training set. Using 0 on tokens that it's never seen before will cause it to largely ignore the token. Ask it to write some code for "gpt-3.5-turbo-1106", and it will often reply with "gpt-3.5-turbo" at temperature 0, but increasing to 1 makes it more consistently reply with "gpt-3.5-turbo-1106". It's dropping the 1106 because it's not in its training weights, and you've kneecapped its ability to pick uncommon tokens. Stabilizing this is a hard thing. New concepts in programming or published research should be given the most attention by us, but the LLMs give them the least attention. Tuning it to pick up new terms more easily means upping the temperature, which also makes it more likely to deviate from the ground truth, which is also undesirable in many tasks.

But I don't think we are very far away from stabilizing this to a point where I will have no problem calling it AI myself.

Watching the inner monologue of the web search agent was illuminating, and worth implementing just to be able to see and modulate all that. For example, I was shocked to see the way that it detailed the precise quoting it would need to use and advanced keyword modifiers, which I didn't even realize were a thing on Bing, as Google dropped those advanced search tools a decade ago.

Watching its inner monologue is very interesting.

<details><summary>Metadata</summary>

- Duration: 33979 ms
- Datetime: 2024-01-07T02:06:27.421053
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

