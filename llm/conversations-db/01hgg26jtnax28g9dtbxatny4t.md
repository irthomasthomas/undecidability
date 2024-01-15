**Prompt:**
write a curl command to demonstrate openai's chatgpt-3.5 API

**Response:**
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" -d '{"model": "openai/chatgpt-3.5-turbo", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won the world series in 2020?"}]}' https://api.openai.com/v1/chat/completions

<details><summary>Metadata</summary>

- Duration: 3648 ms
- Datetime: 2023-11-30T12:10:29.524107
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

