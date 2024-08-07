#!/bin/bash
model_judge="gemini-1.5-pro-latest"
# for i in $(shuf -i 1-230 -n 1000); i=$1
    group_id=$1
    echo "Group ID: $group_id"
    mkdir -p "logs-temp"
    python llm-logs-group-getter.py $group_id > logs-temp/temp.txt
    evaluation="$(files-to-prompt logs-temp | llm -m "$model_judge" --system "$(cat gemini-rubric-xml.md)" "**IMPORTANT NOTE:** Always write numerical score AFTER justifications")"    # make a file to store evaluation
    evaluation_file="evaluation-$group_id.md"
    echo "$evaluation" > "$evaluation_file"
    python import-evaluations-scores-v2.py "$evaluation_file" "/home/ShellLM/Projects/undecidability/agents/rubrics/shelllm.db" "$group_id" "$model_judge"
    rm logs-temp/temp.txt
