**Prompt:**
use gh to create a new github project from the cli


**Response:**
To create a new GitHub project from the command-line using the `gh` tool, you can follow these steps:

1. Install `gh` if you haven't already. `gh` is the official GitHub CLI tool.
   - On Manjaro, you can install it using the following command:
     ```
     sudo pacman -S github-cli
     ```

2. Run the `gh repo create` command followed by the desired project name and, optionally, the repository description:
   ```
   gh repo create <project-name> --description "<description>"
   ```

   For example, to create a project named "my-project" with a description "This is my project," you would run:
   ```
   gh repo create my-project --description "This is my project"
   ```

3. If you haven't already authenticated with your GitHub account, you will be prompted to provide your GitHub credentials.

4. The `gh` tool will create a new GitHub repository with the given name and description using the credentials of the authenticated user. You should see the URL of the newly created repository printed in the output.

Please note that the `gh` command-line tool is an external tool developed by GitHub and may have its own limitations and requirements. Ensure that you have the latest version of `gh` installed and consult the `gh` documentation for more information on usage and available options.

<details><summary>Metadata</summary>

- Duration: 7092 ms
- Datetime: 2023-08-27T09:33:50.818946
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

