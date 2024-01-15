**Prompt:**
Write a bash terminal command to perform the following function, or if impossible, write: echo "That request cannot easily be accomplished in a sigle command. Here is spec describing a script that performs the required functions.": get list of issue labels from gh label list  irthomasthomas/undecidability and display them in a kdialog multi selection Be concise.


**Response:**
gh label list irthomasthomas/undecidability | awk '{print $1}' | xargs kdialog --checklist "Select issue labels" 0 0 0

<details><summary>Metadata</summary>

- Duration: 2278 ms
- Datetime: 2023-09-19T22:38:56.256256
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

