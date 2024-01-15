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
commit() {

  msg="$1"

  git add .

  [[ ! -z "$msg" ]] && git commit -m "$msg"

    while true; do
      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached | ttok -t 3000)") 
      echo "Commit Msg: "$msg""
      echo "Confirm push to repo? [y], edit msg? [e] or regenerate msg? [n]"
      read confirm
      if [[ "$confirm" == "y" ]]; then
        break
      elif [[ "$confirm" == "e" ]]; then
        echo "Enter your customized commit message:"
        read custom_msg
        msg="$custom_msg"
        echo "Commit Msg: "$msg""
        echo "Confirm push to repo with edited message? [y] or regenerate msg? [n]"
        read confirm_edited
        [[ "$confirm_edited" == "y" ]] && break
      else
        continue
      fi 
    done

    git commit -m ""$msg""
}

<details><summary>Metadata</summary>

- Duration: 22968 ms
- Datetime: 2023-10-19T11:39:50.518947
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

