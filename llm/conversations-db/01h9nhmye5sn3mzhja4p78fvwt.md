**Prompt:**
#Arch #Linux #Code #Bash #Shell #ZSH #Terminal #Github #Markdown #Actions #Issues #fzf \n\n In bash, receive instructions from a github repo issues. I want the function to run automatically when a new issue is created with the right label. It retrieve the body text of the issue, pass it to a function, and return the output as a new comment\n\nHere are all of the gh cli tools available. If you want the help page for one you can ask Here are the relevant command reference lines from the paste:

## `gh alias <command>`

Create command shortcuts

## `gh api <endpoint> [flags]`

Make an authenticated GitHub API request

## `gh auth <command>`

Authenticate gh and git with GitHub

## `gh browse [<number> | <path> | <commit-SHA>] [flags]`

Open the repository in the browser

## `gh cache <command>`

Manage Github Actions caches

## `gh changelog`

Extension changelog

## `gh clone-org`

Extension clone-org

## `gh co`

Alias for "pr checkout"

## `gh codeql`

Extension codeql 

## `gh codespace`

Connect to and manage codespaces

## `gh completion -s <shell>`

Generate shell completion scripts

## `gh config <command>` 

Manage configuration for gh

## `gh contribute`

Extension contribute

## `gh cp`

Extension cp

## `gh dash`

Extension dash

## `gh eco`

Extension eco

## `gh extension`

Manage gh extensions

## `gh fire`

Extension fire

## `gh gist <command>`

Manage gists

## `gh gpg-key <command>`

Manage GPG keys

## `gh grep`

Extension grep

## `gh i`

Extension i

## `gh install`

Extension install

## `gh issue <command>`

Manage issues

## `gh label <command>`

Manage labels

## `gh markdown-preview`

Extension markdown-preview

## `gh notify`

Extension notify

## `gh org <command>`

Manage organizations

## `gh pr <command> [flags]`

Manage pull requests

## `gh project <command>`

Work with GitHub Projects.

## `gh quickcs`

Extension quickcs

## `gh release <command>`

Manage releases

## `gh repo <command>`

Manage repositories

## `gh repo-explore`

Extension repo-explore

## `gh ruleset <command>`

View info about repo rulesets

## `gh run <command>`

View details about workflow runs

## `gh s`

Extension s

## `gh search <command>`

Search for repositories, issues, and pull requests

## `gh secret <command>`

Manage GitHub secrets

## `gh ssh-key <command>`

Manage SSH keys

## `gh status [flags]`

Print information about relevant issues, pull requests, and notifications across repositories

## `gh todo`

Extension todo

## `gh triage` 

Extension triage

## `gh user-stars`

Extension user-stars

## `gh userfetch`

Extension userfetch

## `gh variable <command>`

Manage GitHub Actions variables

## `gh workflow <command>`

View details about GitHub Actions workflows

## `gh xplr`

Extension xplr

**Response:**
Here is an example of how to achieve this using GitHub actions and gh cli.

You could have a `.github/workflows/main.yml` file with this. It triggers a GitHub action when an issue with the label `run` is created, runs a shell script, and comments the output back to the issue. 

```yaml
name: Run Script
on:
  issues:
    types: [opened, labeled]

jobs:
  auto-reply:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Check Label
        id: label_check
        run: |
          issue_number=$(jq --raw-output .issue.number "$GITHUB_EVENT_PATH")
          current_label=$(jq --raw-output .label.name "$GITHUB_EVENT_PATH")

          if [[ "$current_label" == "run" ]]; then
            echo "::set-output name=run::true"
            echo "::set-output name=issue_number::$issue_number"
          else
            echo "::set-output name=run::false"
          fi

      - name: Run Script
        id: script
        run: ./script.sh

      - name: Comment
        run: |
            output="${{ steps.script.outputs.result }}"
            issue_number="${{ steps.label_check.outputs.issue_number }}"
            gh issue comment "$issue_number" --repo ${{ github.repository }} --body "$output"
        if: steps.label_check.outputs.run == 'true'
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

This example assumes that you have a file called `script.sh` in your repository root directory that you want to run.

This is a simplified example, the actual implementation would depend on what your script does and how you want to handle errors. 

The authentication is managed by the `secrets.GITHUB_TOKEN` which is automatically made available to GitHub actions. 

You also need to setup gh cli in the GitHub action. Here is the command to do that in a step:

```yaml
- name: Setup GitHub CLI
  uses: cli/setup-gh@v1
``` 

You would then insert it into the job steps like this:

```yaml
jobs:
  auto-reply:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      
      - name: Setup GitHub CLI
        uses: cli/setup-gh@v1

      ...
```

This way, the `gh` command is available within the action and can be used to interact with the issues.

<details><summary>Metadata</summary>

- Duration: 68885 ms
- Datetime: 2023-09-06T15:25:42.958947
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

