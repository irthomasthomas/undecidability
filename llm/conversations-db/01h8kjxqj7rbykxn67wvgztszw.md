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
 how can I tell what other man pages are available and go to them?

**Response:**
To find other available man pages and navigate to them, you can use the `man` command followed by the name of the desired page. Here's how you can do it:

1. Open your terminal.
2. Type `man` followed by the name of the command or topic you want to explore. For example, if you want to learn about Git, you can type `man git`.

   ```
   man git
   ```

3. Press Enter, and the manual page for the specified command or topic will be displayed.

   ```
   GIT(1)                                                          Git Manual                                                          GIT(1)

   NAME
       git - the stupid content tracker

   SYNOPSIS
       git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
   ...
   ```

4. To navigate within a man page, you can use the following commands:
   - Use the Up and Down arrow keys to scroll through the content.
   - Press the Spacebar to scroll down by one screen.
   - Press the B key to scroll up by one screen.
   - Press the G key to go to the beginning of the page.
   - Press the Q key to exit the man page.

By using the `man` command and specifying the appropriate name, you can easily explore and navigate through different manual pages.

<details><summary>Metadata</summary>

- Duration: 16122 ms
- Datetime: 2023-08-24T10:54:41.484246
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

