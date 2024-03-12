#!/bin/bash

# Default values
model="groq"
task="code-review"
temperature=0.5
output_dir=".scratchpad/groq"
num_reviews=3

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--model)
      model="$2"
      shift 2
      ;;
    -t|--task)
      task="$2"
      shift 2
      ;;
    -o|--output-dir)
      output_dir="$2"
      shift 2
      ;;
    -n|--num-reviews)
      num_reviews="$2"
      shift 2
      ;;
    -T|--temperature)
      temperature="$2"
      shift 2
      ;;
    -s|--system-prompt)
      system_prompt="$2"
      shift 2
      ;;
    -p|--prompt)
      prompt="$2"
      shift 2
      ;;
    -*)
      echo "Unknown option: $1"
      exit 1
      ;;
    *)
      break
      ;;
  esac
done

# Check if at least one file path is provided
if [[ $# -eq 0 ]]; then
  echo "Usage: $0 [-m MODEL] [-t TASK] [-o OUTPUT_DIR] [-n NUM_REVIEWS] [-T TEMPERATURE] [-s SYSTEM_PROMPT] [-p PROMPT] FILE [FILE...]"
  exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"
# if no prompt is provided, use the default prompt
if [[ -z $prompt ]]; then
  prompt="The date is $(date) 
You are senior software engineer. An expert in high-performance programming.
Study the code reviews from each of the reviewers carefully.
Pay attention to the suggestions and the reasoning behind them. 
Pick the best suggestions from each of them, and ignore unsuitable proposals. 
Synthesize a new, final proposal, incorporating the best suggestions from the group. 
Include your reasoning"
else
  prompt="Current datetime: $(date)\n\n$prompt"
fi
# Generate code reviews in parallel
for ((i=1; i<=num_reviews; i++)); do
  for file in "$@"; do
    (
      file_name=$(basename "$file")
      file_content=$(cat "$file")
      llm -m "$model" "$prompt\n
$file_name:
$file_content
end_$file_name
\n\n$(date)" -o temperature "$temperature" > "$output_dir/$model-review-$i-$file_name.md" 
    ) &
  done
done

# Wait for all code review processes to finish
wait

# Generate the final proposal
llm -m "$model-llama" --system "You are senior software engineer. An expert in high-performance programming." -o temperature "$temperature" "
$(date)\nStudy the code reviews from each of the three reviewers. 
Pick the best suggestions from each of them, and ignore unsuitable proposals.
Synthesize a new, final proposal, incorporating the best suggestions from the group.
Include your reasoning." > "$output_dir/$model-bot.md"

for ((i=1; i<=num_reviews; i++)); do
  echo "user_${i}_proposed_changes:" >> "$output_dir/$model-bot.md"
  for file in "$@"; do
    file_name=$(basename "$file")
    echo "File: $file_name" >> "$output_dir/$model-bot.md"
    cat "$output_dir/$model-review-$i-$file_name.md" >> "$output_dir/$model-bot.md"
    echo "end_user_${i}_proposed_changes_for_$file_name" >> "$output_dir/$model-bot.md"
  done
done

echo "\n\n$(date)" >> "$output_dir/$model-bot.md"
