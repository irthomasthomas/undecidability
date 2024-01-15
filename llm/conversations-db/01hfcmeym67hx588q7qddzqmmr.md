**Prompt:**
Write an openai curl call which returns only 'yes' or 'no' to a question using log ...

**Response:**
```bash
curl https://api.openai.com/v1/engines/davinci-codex/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "prompt": "Question: Is rainwater safe to drink? Answer with 'yes' or 'no' only.\nLog:",
  "temperature": 0,
  "max_tokens": 1,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "logprobs": 2,
  "n": 1,
  "stop": ["\n"]
}'
```

Replace `YOUR_API_KEY` with your actual OpenAI API key. The `logprobs` parameter is set to 2 to return the log probabilities of the top 2 tokens, which can be used to analyze the model's decision-making process. The `stop` parameter is set to a newline character to ensure the model stops after generating 'yes' or 'no'. The `max_tokens` is set to 1 to restrict the output to a single word.

<details><summary>Metadata</summary>

- Duration: 10057 ms
- Datetime: 2023-11-16T17:56:52.155981
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

