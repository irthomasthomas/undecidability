**Prompt:**
Write a bash terminal command to perform the following function, or if impossible, write: echo "That request cannot easily be accomplished in a sigle command. Here is spec describing a script that performs the required functions.": get list of issue labels from gh irthomasthomas/undecidability and display them in a kdialog multi selection Be concise.


**Response:**
echo "$(gh issue list -R irthomasthomas/undecidability --label | awk '{print $NF}' | sort -u)" | kdialog --multiple --checklist "Select issue labels"

<details><summary>Metadata</summary>

- Duration: 2007 ms
- Datetime: 2023-09-19T22:37:23.595574
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

