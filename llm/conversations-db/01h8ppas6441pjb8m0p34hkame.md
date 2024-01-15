**Prompt:**
cllm() {
  echo "$1" | claude --key /home/tommy/Development/ai/claude-sessionkey
  }

mkfilename() {
  file_content="$1"
  # Truncate to <=400 tokens
  trunc_content=ttok "$file_content" -t 400
  llm_template="makefilename"
  echo "$trunc_content" -m 3.5  "Generate a good file name For use on UNIX and Linux systems for the following content:"  
  }

commit() {

  msg="$1"

  git add .

  [[ ! -z "$msg" ]] && git commit -m "$msg"

    while true; do
      #     msg="$(llm -t commit335 -p comm1 $(git diff --cached | llm -t commit135 -o temperature 0.3) -p comm2 $(git diff --cached | llm -t commit135 -o temperature 0.3) -p comm3 $(git diff --cached | llm -t commit135 -o temperature 0.3))"

      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached)") # -m 3.5-16k
      echo "Commit Msg: "$msg""
      echo "Confirm push to repo? [y] or regenerate msg? [n]"
      read confirm
      [[ "$confirm" == "y" ]] || continue
      break
    done

    git commit -m ""$msg""
}

# TODO
nolog() { llm  }

help() { print -z $(llm -t shellhelp "$1" -o temperature 0) }

help4() { print -z $(llm -t shellhelp "$1" -m 4 -o temperature 0) }

mkscript() {
  input="$1"
  model="$2"
  llm -t shellscript "$input" "$model" -o temperature 0.2
}

advisor() {
  model="$2"
  llm -t advisor "$1" "$model" -o temperature 0.2
  }

klippy() {
  model="$2"
  llm -t kde "$1" "$model" -o temperature 0.2
  }

**Response:**
generate_file_name.sh

<details><summary>Metadata</summary>

- Duration: 663 ms
- Datetime: 2023-08-25T15:52:13.612525
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

