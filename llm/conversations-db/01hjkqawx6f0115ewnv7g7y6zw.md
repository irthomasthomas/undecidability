**Prompt:**
Write an interesting and unique shell function that uses curl

**Response:**
Function: `github_repo_contributors_statistics`

Purpose: Retrieve and summarize the number of contributors and the total number of contributions (commits) to a given GitHub repository.

Shell: Bash

Dependencies: `curl`, `jq` for JSON parsing.

```bash
function github_repo_contributors_statistics() {
  local repo="$1"
  local page=1
  local per_page=100
  local contributors_url="https://api.github.com/repos/${repo}/contributors"
  local total_contributors=0
  local total_commits=0
  local response=()

  while : ; do
    # Fetch JSON contributor data from GitHub API with pagination
    response=$(curl -sS "${contributors_url}?page=${page}&per_page=${per_page}")

    # Break if no more contributors (empty JSON array)
    [[ "$response" == "[]" ]] && break

    # Count contributors in the current page
    local contributors_count=$(echo "$response" | jq '. | length')
    total_contributors=$((total_contributors + contributors_count))

    # Sum up commits from contributors and sum with total
    total_commits=$((total_commits + $(echo "$response" | jq '[.[] .contributions] | add')))

    ((page++))
  done

  echo "Repository: $repo"
  echo "Total contributors: $total_contribitors"
  echo "Total contributions: $total_commits"
}
```

Usage: `github_repo_contributors_statistics <owner/repo>`

Example: `github_repo_contributors_statistics torvalds/linux`

Explanation:
- The function takes a repository in the form of `<owner/repo>`, using the GitHub API base URL to construct a request for contributor data with pagination.
- The loop fetches data in pages to handle repositories with more than 100 contributors.
- Pagination is handled by the `page` parameter.
- `jq` is used to parse the JSON returned by GitHub and compute the statistics.
- The loop terminates when an empty JSON array is returned.
- The function outputs total numbers of contributors and contributions.

<details><summary>Metadata</summary>

- Duration: 19698 ms
- Datetime: 2023-12-26T18:48:41.907530
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 1.0}
```

