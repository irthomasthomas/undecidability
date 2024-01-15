**Prompt:**

Reply only with the text of the bash script and nothing else. Use code comments if you need to say anything else.
Think it through step-by-step.
Requirements (If the line is blank after this, then the user input failed. Tell the user that they did not provide any input.): Open this app: /usr/lib/brave-browser/brave --profile-directory=SuperPower --app-id=gckfnpnnlacoefkmgdopeamcabnkffaa 
Then, wait for window to be active
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer APIs and tools and app versions from 2015, 2016, 2017, 2018, 2019, 2020, 2021 or later.
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
#!/bin/bash

# Open Brave browser with the specified profile and app ID
/usr/lib/brave-browser/brave --profile-directory=SuperPower --app-id=gckfnpnnlacoefkmgdopeamcabnkffaa

# Wait for the window to become active
while ! pgrep -x "brave" >/dev/null; do
  sleep 1
done

<details><summary>Metadata</summary>

- Duration: 3283 ms
- Datetime: 2023-07-20T12:54:27.389359
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

