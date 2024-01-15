**Prompt:**
Think carefully. Write a complete, fully functional bash script to Get the names of kde activities with qdbus?
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.
WARNING: Your response must NOT include text OUTSIDE of the code block.
SAY NOTHING ELSE!


**Response:**
#!/bin/bash

# Get all available activities using qdbus
activity_list=$(qdbus org.kde.ActivityManager /ActivityManager/Activities ListActivities)

# Print the names of the activities
for activity in $activity_list; do
  echo "$(qdbus org.kde.ActivityManager /ActivityManager/Activities GetName $activity)"
done

<details><summary>Metadata</summary>

- Duration: 3110 ms
- Datetime: 2023-07-19T16:53:34.099808
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

