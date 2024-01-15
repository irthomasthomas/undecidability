**Prompt:**
write a curl command to demonstrate openai's chatgpt-3.5 API

**Response:**
```bash
curl https://api.openai.com/v1/engines/gpt-3.5-turbo/completions \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "model": "gpt-3.5-turbo",
        "prompt": "Translate the following English text to French: 'Hello, how are you?'",
        "temperature": 0.7,
        "max_tokens": 60
      }'
```

Replace `YOUR_API_KEY` with your actual OpenAI API key.

<details><summary>Metadata</summary>

- Duration: 8663 ms
- Datetime: 2023-11-30T12:19:12.797541
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
"error": {
        "message": "Cannot specify both model and engine",

**Response:**
Remove "model" from the payload:

```bash
curl https://api.openai.com/v1/engines/gpt-3.5-turbo/completions \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "prompt": "Translate the following English text to French: 'Hello, how are you?'",
        "temperature": 0.7,
        "max_tokens": 60
      }'
```

<details><summary>Metadata</summary>

- Duration: 7526 ms
- Datetime: 2023-11-30T12:21:01.776930
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
"error": {
    "message": "This is a chat model and not supported in the v1/completions endpoint. Did you mean to use v1/chat/completions?",

**Response:**
Use the `v1/chat/completions` endpoint:

```bash
curl https://api.openai.com/v1/chat/completions \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Translate 'Hello, how are you?' to French."}]
      }'
```

<details><summary>Metadata</summary>

- Duration: 8805 ms
- Datetime: 2023-11-30T12:21:49.745545
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

