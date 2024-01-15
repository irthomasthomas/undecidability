**Prompt:**
code to search github api

**Response:**


import requests
from typing import List, Dict

url = 'https://api.github.com/search/repositories'

def get_data(query: str) -> dict:
    payload = { 'q': query }
    response = requests.get(url, params=payload)
    return response.json()

def search_user_code(username: str, reponame: str) -> List[dict]:
    data = get_data(f'user:{username} {reponame}')
    if 'items' not in data or not data['items']:
        return []
    items = data['items']

    for item in items:
        if f'{username}/{reponame}' in item['url']:
            return [item]

    return []

def search_file(user: str, repo: str, filename: str) -> Dict[str, any]:
    data = get_data(f'q={filename} path:{repo} user:{user}')
    if 'items' not in data or not data['items']:
        return {}
    items = [item for item in data['items'] if f'{user}/{repo}' in item['url']]

    if len(items) == 1:
        file_data = get_data(f'https://api.github.com/repos/{user}/{repo}/contents{items[0]["path"]}')
        return { 'file_info': items[0], 'content': file_data['content'] }
    else:
        return {}

if __name__ == '__main__':
    print(search_user_code('google', 'guava')) # search for a code in google/guava repo
    print(search_file('google','guava','LICENSE')) # search for the file named "LICENSE" in google/guava repo

<details><summary>Metadata</summary>

- Duration: 52053 ms
- Datetime: 2024-01-11T17:38:28.476744
- Model: dolphin-2.5-mixtral-8x7b

</details>

**Options:**
```json
{}
```

