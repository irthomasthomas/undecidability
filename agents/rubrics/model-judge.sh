#!/bin/bash
model_judge="gemini-1.5-pro-latest"
# for i in $(shuf -i 100-230 -n 2); do
# for i in 201 103 221 191 120 177 165 219 160 100 207 122 101 22 92; do
for i in 101 160 165 207; do
    group_id=$i
    evaluation="$(llm -m "$model_judge" --system "$(cat gemini-rubric.md)" "$(python llm-logs-group-getter.py $group_id)
**IMPORTANT NOTE:** Always write numerical score AFTER justifications")"
    
    python import-evaluations-scores.py "$evaluation" ~/shelllm.db $group_id $model_judge
    
done
