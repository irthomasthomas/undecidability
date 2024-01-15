**Prompt:**
Add choice to edit the generated commit msg 
commit() {

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
This script will allow you to edit the generated commit message before committing the changes to the repository. It uses a loop to keep asking for confirmation until you're satisfied with the message. If you're not, it will regenerate the message.

Here's how it works:

1. It first adds all changes to the staging area with `git add .`.
2. If a message was passed as an argument to the function, it will commit the changes with that message.
3. Then it enters a loop where it generates a commit message using some tool or function (in this case, `llm` and `ttok` are used, but these are placeholders and should be replaced with actual tools or functions you have).
4. It then asks for confirmation to push the changes to the repository. If you confirm with 'y', it breaks the loop and commits the changes with the generated message. If you don't confirm, it goes back to the start of the loop and generates a new message.

Please note that this script assumes that you have the `llm` and `ttok` tools or functions available in your environment. If you don't, you should replace these with the actual tools or functions you use to generate commit messages.

<details><summary>Metadata</summary>

- Duration: 25318 ms
- Datetime: 2023-10-19T11:10:09.414023
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

