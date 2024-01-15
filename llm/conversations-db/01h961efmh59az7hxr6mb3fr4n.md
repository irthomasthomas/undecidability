**Prompt:**
What is the exact zsh command to: view a github markdown in terminal?


**Response:**
glow filename.md

<details><summary>Metadata</summary>

- Duration: 1601 ms
- Datetime: 2023-08-31T14:55:04.783462
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
## Command <a id='command'></a>
    \`\`\`
    ${cmd}
    \`\`\`
    [Link to Command](#command)
    
    ## Token Count <a id='token_count'></a>
    \`\`\`
    ${token_count}
    \`\`\`
    [Link to Token Count](#token_count)
    
    ## Output <a id='output'></a>
    \`\`\`
    ${output}
    \`\`\`
    [Link to Output](#output)
 What is up with this markdown for github?

**Response:**
This markdown seems to be a template for documenting a command, its token count, and its output. It is designed with linkable header IDs for navigation on Github. However, there's an issue. The placeholders (like `${cmd}`) are not correctly replaced with actual values. It might have been intended to be processed by a script or templating tool that replaces these placeholders.

Here is how it should look after replacement:

```markdown
## Command <a id='command'></a>
    ```
    actual-command-goes-here
    ```
    [Link to Command](#command)
    
## Token Count <a id='token_count'></a>
    ```
    actual-token-count-goes-here
    ```
    [Link to Token Count](#token_count)
    
## Output <a id='output'></a>
    ```
    actual-output-goes-here
    ```
    [Link to Output](#output)
```

Obviously, you'd replace `actual-command-goes-here`, `actual-token-count-goes-here` and `actual-output-goes-here` with actual contents.

<details><summary>Metadata</summary>

- Duration: 26530 ms
- Datetime: 2023-08-31T14:56:00.015002
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
will that work within the body of github issue?

**Response:**
Yes, it will. GitHub markdown supports this kind of formatting. The provided anchors (like `#command`) in your template can be used to create internal links within GitHub's documentation. 

When the markdown is rendered on GitHub, you can click on the links and it will take you to the corresponding section in the same document. You can use it in GitHub issues, pull request descriptions, comments, and GitHub's README or wiki pages.

You just need to make sure to replace the placeholder text (`${cmd}`, `${token_count}`, `${output}`) with your actual content before posting it on GitHub.

<details><summary>Metadata</summary>

- Duration: 13467 ms
- Datetime: 2023-08-31T14:57:02.832818
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

