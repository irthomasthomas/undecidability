**Prompt:**
Add a new choice to edit the generated commit message: commit() {

  msg="$1"

  git add .

  [[ ! -z "$msg" ]] && git commit -m "$msg"

    while true; do
      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached | ttok -t 3000)") # -m 3.5-16k
      echo "Commit Msg: "$msg""
      echo "Confirm push to repo? [y] or regenerate msg? [n]"
      read confirm
      [[ "$confirm" == "y" ]] || continue
      break
    done

    git commit -m ""$msg""
}

**Response:**
Add a new choice to edit the generated commit message:

```bash
commit() {
  msg="$1"

  git add .

  [[ ! -z "$msg" ]] && git commit -m "$msg"

  while true; do
    msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached | ttok -t 3000)") # -m 3.5-16k
    echo "Commit Msg: "$msg""
    echo "Confirm push to repo? [y] or regenerate msg? [n]"
    read confirm
    if [[ "$confirm" == "y" ]]; then
      git commit -m "$msg"
      break
    fi
  done
}
```

This updated code allows you to confirm or regenerate the commit message before pushing it to the repository.

<details><summary>Metadata</summary>

- Duration: 19051 ms
- Datetime: 2023-10-19T11:22:09.927734
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

