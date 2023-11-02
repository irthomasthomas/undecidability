Incorporating GitHub Actions to automate your process would be a fantastic solution. To develop a GitHub Action that carries out your steps, consider the following:

1. **On GitHub Workflow:** Set up a new workflow that triggers on issue creation and label being assigned as 'inbox-url'. Below is a personalized example of how your GitHub workflow `.yml` might look like:



```yml
name: Task Processing

on:
issues:
types: [opened, labeled]

jobs:
process_task:
if: github.event.label.name == 'inbox-url'
runs-on: ubuntu-latest
steps:
- name: Checkout
uses: actions/checkout@v2

- name: Setup Node.js
uses: actions/setup-node@v2
with:
node-version: '14'

- name: Install dependencies
run: | 
npm ci
npm install axios pdf-parse 

- name: Run task processing script
run: node .github/actions/process.js
env:
GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

- name: Assign to owner
uses: peter-evans/create-or-update-comment@v1
with:
token: ${{ secrets.GITHUB_TOKEN }}
issue-number: "${{ github.event.issue.number }}"
assignees: <Your UserName>
    ```


    2. **Node.js Serverless Function:** 

    In this script, you make use of the GitHub Octokit client to make changes to issues, Axios for sending web request to get URL contents, and pdf-parse to parse PDFs from URLs when needed. Note: Make sure to replace `'owner/repo'` placeholder with your repository and `'GITHUB_PAT'` placeholder with your GitHub Personal Access Token.



    ```javascript
    const axios = require('axios');
    const pdf = require('pdf-parse');
    const core = require('@actions/core');
    const github = require('@actions/github');
    const { readFile } = require('fs').promises;

    process()
    .then(() => core.info('Completed task processing'))
    .catch(error => core.setFailed(error.message));

    async function process() {
        const repoToken = process.env.GITHUB_TOKEN;
        const context = github.context;
        const octokit = github.getOctokit(repoToken);

        const { number } = context.issue;
        const { body } = context.payload.issue;

        let url;
        let issueText = body
        .split('\n')
        .filter(line => {
            if (line.startsWith("- [ ]")) {
                url = line.match(/\[.*?\]\((.*?)\)/)[1];
                return false;
            }
            return true;
        })
        .join('\n');

        let text;
        if (url.endsWith('.pdf')) {
            const { data } = await axios.get(url, { responseType: 'arraybuffer' });
            text = await pdf(data);
        } else {
            const { data } = await axios.get(url);
            text = extractTextFromHTML(data);
        }

        issueText += '\n\n' + text;

        await octokit.rest.issues.update({
            owner: context.owner.login,
            repo: context.repo.repo,
            issue_number: number,
            body: issueText
        });

        await octokit.rest.issues.addAssignees({
            owner: context.owner.login,
            repo: context.repo.repo,
            issue_number: number,
            assignees: [context.owner.login]
        });
    }

    function extractTextFromHTML(html) {
        // Add logic to extract text from HTML. This depends largely on the structure of the scraped web pages.
    }
    ```


    3. **Extracting text from HTML:**

    Keep in mind that accurately extracting the text from a webpage is a complex task and it's largely dependent on how the webpage is structured. If you're dealing with different websites then you might want to use a library like [jsdom](https://www.npmjs.com/package/jsdom) or [Cheerio](https://cheerio.js.org/) to help parse and navigate the HTML.

    These above are general guidelines and must be adapted according to specific repository and user's requirements. For specific and sensitive data such as secrets (`GITHUB_PAT`), ensure they are stored in [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) and replaced accordingly to preserve data confidentiality.
    