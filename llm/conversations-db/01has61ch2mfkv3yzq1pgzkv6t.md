**Prompt:**
Write a bash terminal command to perform the following function, or if impossible, write: echo "That request cannot easily be accomplished in a sigle command. Here is spec describing a script that performs the required functions.": How can I diagnose why my cpu governor is being set to ondemand? Be concise.


**Response:**
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

<details><summary>Metadata</summary>

- Duration: 1058 ms
- Datetime: 2023-09-20T11:36:35.071667
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

