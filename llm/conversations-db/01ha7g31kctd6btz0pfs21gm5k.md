**Prompt:**
Add the field names to the output so it looks pretty:  jq '.stargazers_count','.forks_count','.open_issues_count','.size','.created_at','.updated_at','.html_url','.description','.organization.avatar_url'

**Response:**
To add field names to the output using `jq`, you can use the `--arg` option to define the field names as variables and then use string interpolation to include them in the output. Here's how you can modify the command:

```shell
jq --arg star "Stargazers Count" \
   --arg fork "Forks Count" \
   --arg open "Open Issues Count" \
   --arg size "Size" \
   --arg created "Created At" \
   --arg updated "Updated At" \
   --arg url "HTML URL" \
   --arg desc "Description" \
   --arg avatar "Avatar URL" \
  '{
    ($star): .stargazers_count, 
    ($fork): .forks_count, 
    ($open): .open_issues_count, 
    ($size): .size, 
    ($created): .created_at, 
    ($updated): .updated_at, 
    ($url): .html_url, 
    ($desc): .description, 
    ($avatar): .organization.avatar_url
  }'
```

This command creates variables for each field name and then includes them in the output along with the corresponding field values. Note that you need to escape the double quotes inside the `jq` script to ensure correct string interpolation.

Keep in mind that this assumes you have an input JSON object with the required fields.

<details><summary>Metadata</summary>

- Duration: 14706 ms
- Datetime: 2023-09-13T14:45:41.753383
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

