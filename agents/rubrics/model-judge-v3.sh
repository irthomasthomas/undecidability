#!/bin/bash
model_judge="gemini-1.5-pro-latest"
for i in $(shuf -i 1-230 -n 2); do
    group_id=$i
    echo "Group ID: $group_id"
    evaluation="$(llm -m "$model_judge" --system "$(cat gemini-rubric-xml.md)" "$(python llm-logs-group-getter.py $group_id)
**IMPORTANT NOTE:** Always write numerical score AFTER justifications")"
    
    python import-evaluations-scores-v3.py "$evaluation" /home/ShellLM/Projects/undecidability/agents/rubrics/shelllm.db $group_id $model_judge
    
done
