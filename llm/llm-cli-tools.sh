commit() {
    # Generate commit messages using llm and commit changes to git repo.
    # Usage: commit <commit message> # Manually enter commit message
    # Usage: commit # Generate commit message using llm

    local commit_msg="$1"

    git add .

    [[ ! -z "$commit_msg" ]] && git commit -m "$commit_msg"

        while true; do
        # Must be a better way than git diff --cached
        commit_msg=$(llm -t commit135 -o temperature 0.6 "$(git diff --cached | ttok -t 10000)")
        # What other git commands can be used to generate a commit message?
        
        echo "Commit message... "
        echo "$commit_msg"
        echo "CONFIRM: [y] push to repo, [e] edit manually, [n] regenerate commit message"
        read confirm
        if [[ "$confirm" == "y" ]]; then
            break
        elif [[ "$confirm" == "e" ]]; then
            echo "Enter your customized commit message:"
            read custom_msg
            commit_msg="$custom_msg"
            echo "Commit commit_msg: "$commit_msg""
            echo "Confirm push to repo with edited message? [y] or regenerate msg? [n]"
            read confirm_edited
            [[ "$confirm_edited" == "y" ]] && break
        else
            continue
        fi
        done

        git commit -m ""$commit_msg""
        git push
}


help2 () {
    # Use llm to generate help for a command.
    # Usage: help2 <command> <args>
    # Example: help2 "How do I use the terminator terminal?"
    # Example: help2 exec "How do I use the terminator terminal?" 
    
    local cmd="$1"
    # if cmd is 'exec', execute the command and return
    if [[ "$cmd" == "exec" ]]; then # we execute the command and return
      cmd="$2"
      shift 2
      cmd_to_exec="$(llm -o temperature 0 -t shellhelp "$cmd" "${@:2}")"
      echo "Executing: $cmd_to_exec"
      eval "$cmd_to_exec"
      return
    fi
      
    if [[ "$cmd" == "-c" ]]; then # continueing
      cmd="$2"
      shift 2
      print -z $(llm -c "$cmd" "${@:2}")
    else
      print -z $(llm -o temperature 0 -t shellhelp "$cmd" "${@:2}")
    fi
}

help () {
    # Use llm to generate help for a command.
    # Usage: help <command> <args>
    # Example: help "How do I use the terminator terminal?"
    # Example: help "How do I use the terminator terminal?" -m 3.5

    local cmd="$1"
    if [[ "$cmd" == "-c" ]]; then # continueing
      cmd="$2"
      shift 2
      print -z $(llm -c "$cmd" "${@:2}")
    else
      print -z $(llm -o temperature 0 -t shellhelp "$cmd" "${@:2}")
    fi
     # print -z $(llm -o temperature 0 -t shellhelp "$1" "${@:2}")
}