**Prompt:**
GH-ISSUE(1)                                                                                                                     GitHub CLI manual                                                                                                                     GH-ISSUE(1)

NAME
       gh-issue - Manage issues

SYNOPSIS
       gh issue <command> [flags]

DESCRIPTION
       Work with GitHub issues.

GENERAL COMMANDS
       gh-issue-create(1)
              Create a new issue

       gh-issue-list(1)
              List issues in a repository

       gh-issue-status(1)
              Show status of relevant issues

TARGETED COMMANDS
       gh-issue-close(1)
              Close issue

       gh-issue-comment(1)
              Add a comment to an issue

       gh-issue-delete(1)
              Delete issue

       gh-issue-develop(1)
              Manage linked branches for an issue

       gh-issue-edit(1)
              Edit issues

       gh-issue-lock(1)
              Lock issue conversation

       gh-issue-pin(1)
              Pin a issue

       gh-issue-reopen(1)
              Reopen issue

       gh-issue-transfer(1)
              Transfer issue to another repository

       gh-issue-unlock(1)
              Unlock issue conversation

       gh-issue-unpin(1)
              Unpin a issue

       gh-issue-view(1)
              View an issue

OPTIONS
       -R, --repo <[HOST/]OWNER/REPO>
              Select another repository using the [HOST/]OWNER/REPO format

EXAMPLE
              $ gh issue list
              $ gh issue create --label bug
              $ gh issue view 123 --web

SEE ALSO
       gh(1)

                                                                                                                                     Jul 2023                                                                                                                         GH-ISSUE(1)
 how can I access the man page for the commands listed?


**Response:**
To access the man page for each command listed, you can use the `man` command followed by the command name. For example:

```
man gh-issue-create
man gh-issue-list
man gh-issue-status
man gh-issue-close
man gh-issue-comment
```

Continue this pattern for each command you want to access the man page for.

<details><summary>Metadata</summary>

- Duration: 3972 ms
- Datetime: 2023-08-24T10:57:16.615496
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

