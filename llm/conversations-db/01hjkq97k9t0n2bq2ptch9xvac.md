**Prompt:**
Write an interesting and unusual shell function

**Response:**
```sh
function forecast {
  local city="${1:-Tokyo}"
  curl -s "wttr.in/${city}?format=3"
}
```
This shell function named `forecast` retrieves the weather forecast for a specified city using the `wttr.in` service. The function uses `curl` for making a GET request to the `wttr.in` API. The usage of `${1:-Tokyo}` allows for an optional argument; if no argument is provided, it defaults to "Tokyo". The query parameter `format=3` requests a short, one-line weather report.

<details><summary>Metadata</summary>

- Duration: 8231 ms
- Datetime: 2023-12-26T18:47:58.785526
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 1.0}
```

