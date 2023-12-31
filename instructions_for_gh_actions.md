To proceed with the implementation, follow the steps below:

1. Create a file named `main.yml` in the `.github/workflows/` directory of your repository. The file name and location can be changed based on your preference. 

2. In that file, use the following modified code snippet based on the previous discussion:

```yaml
name: Run Script
on:
   issues:
    types: [opened, labeled]

jobs:
  auto-reply:
    if: github.event.label.name == 'run'
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2
      
      - name: Setup GitHub CLI
        uses: cli/setup-gh@v1

      - name: Run Script
        id: script
        run: |
          try {
            output=$(./script.sh)
            echo "::set-output name=result::$output"
           } catch {
           echo "The script failed to run"
           output="An error has occurred while running the script."
           }

      - name: Post Comment
        id: comment
        uses: actions/github-script@v3.1.0
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const issue_number = context.issue.number;
            const comments = await github.issues.listComments({...context.repo, issue_number});
            const bot_comment_exists = comments.data.some(comment => comment.user.login === 'github-actions[bot]' && comment.body.includes('Your output text here'));
            if (!bot_comment_exists) {
              await github.issues.createComment({...context.repo, issue_number, body: '${{steps.script.outputs.result}}'});
            }
```

Here's what this script does:

1. It's triggered whenever an issue is labeled or created.
2. Checks if the label name equals 'run'.
3. If true, the workflow continues, otherwise, it stops.
4. The script at `./script.sh` is executed.
5. A list of comments on the issue is fetched.
6. It's checked if there exists a comment by the GitHub Actions bot that includes some specific content.
7. If such a comment doesn't exist already, a new comment is created which contains the output of your script.

Make sure to replace `Your output text here` with a string which is representative of the comments made by your action.

Also, please note that this is a simplified example. Exact implementation might depend on specific requirements like the content of the script to run, handling different types of errors, or parsing the output before posting it to GitHub issues.

Lastly, this script assumes that you have a script named `script.sh` at the root of your repository but you can change this to wherever your script resides.
