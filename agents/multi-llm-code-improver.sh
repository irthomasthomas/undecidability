#!/bin/bash

# Function to generate code reviews in parallel
generate_code_reviews() {
  local model="$1"
  local task="$2"
  local output_dir="$3"
  local num_reviews="$4"
  local temperature="$5"
  local prompt="$6"
  shift 6

  # Create the output directory if it doesn't exist
  mkdir -p "$output_dir"

  if [[ "$model" == claude-3* ]]; then
    temperature_string=""
  else
    temperature_string="-o temperature $temperature"
  fi
    echo "temperature_string $temperature_string"
  # Generate code reviews in parallel
  for ((i=1; i<=num_reviews; i++)); do
    for file in "$@"; do
      (
        file_name=$(basename "$file")
        file_content=$(cat "$file")
        llm -m "$model" "Current datetime: $(date)
$prompt

filename: $file_name

$file_content
end_$file_name
\n\n$(date) $temperature_string" > "$output_dir/$model-review-$i-$file_name.md"
      ) &
    done
    wait
  done
}

# Function to merge code reviews into a single file
merge_code_reviews() {
  local model="$1"
  local output_dir="$2"
  local num_reviews="$3"
  shift 3

  echo "# Code Reviews" > "$output_dir/$model-code-reviews-merged.md"
  for ((i=1; i<=num_reviews; i++)); do
    echo "## Review $i" >> "$output_dir/$model-code-reviews-merged.md"
    for file in "$@"; do
      file_name=$(basename "$file")
      echo "### $file_name" >> "$output_dir/$model-code-reviews-merged.md"
      cat "$output_dir/$model-review-$i-$file_name.md" >> "$output_dir/$model-code-reviews-merged.md"
    done
  done

  echo "\n\n$(date)
(Dear assistant, remember to pay attention to ALL the text.)" >> "$output_dir/$model-code-reviews-merged.md"
}

# Function to merge input files into a single file
merge_input_files() {
  local output_dir="$1"
  shift

  echo "# Original Source Code" > "$output_dir/code-input-files-merged.md"
  for file in "$@"; do
    echo "## $(basename "$file")" >> "$output_dir/code-input-files-merged.md"
    cat "$file" >> "$output_dir/code-input-files-merged.md"
  done
}

# Function to generate the final review
generate_final_review() {
  local model="$1"
  local output_dir="$2"
  local temperature="$3"

  if [[ "$model" == claude-3* ]]; then
    temperature_string=""
  else
    temperature_string="-o temperature $temperature"
  fi
    echo "temperature_string $temperature_string"

  llm -m "$model" --system "You are a senior software engineer. An expert in high-performance programming." "Current date: $(date)
Study the code reviews from each of the reviewers.
Pick the best suggestions from each, and ignore unsuitable proposals.

Your job is to consider the advice of the reviewers, but not be constrained by them. Try to go beyond them.
Produce a final report with a detailed plan to improve the robustness, efficiency and maintainability of the source code.
Always consider the most up-to-date best practices and the latest technologies.
Include your reasoning.
Remember, this proposal will be read by the team, so be detailed and use appropriate nomenclature. Avoid long bullet points, use paragraphs instead. If you do need lists, keep them to a maximum of 3 items.
**IMPORTANT** Pay close attention to ALL of the source code. Mention every part of the code even if it requires no changes, so that I can be sure you studied it thoroughly.

ORIGINAL_SOURCE_CODE:
$(cat "$output_dir/code-input-files-merged.md")
END_ORIGINAL_SOURCE_CODE

PROPOSED_CHANGES:
$(cat "$output_dir/$model-code-reviews-merged.md")
END_PROPOSED_CHANGES

**IMPORTANT**: Assistant, please make sure that the final review is complete and that it includes all the code. If the code is too long, please include the first and last 100 lines, and mention that the code has been truncated. If the code is too short, please mention that the code is complete. Thank you.
FINAL_REVIEW: $temperature_string" > "$output_dir/$model-final-review.md"
}

# Main function
main() {
  # Default values
  model="groq"
  task="code-review"
  temperature=0.5
  output_dir=".scratchpad/$model"
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
      -P|--prompt)
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
    echo "Usage: $0 [-m MODEL] [-t TASK] [-o OUTPUT_DIR] [-n NUM_REVIEWS] [-T TEMPERATURE] [-P PROMPT] file1 [file2 ...]"
    exit 1
  fi

  # Set default prompt if not provided
  if [[ -z "$prompt" ]]; then
    prompt="You are an expert linux programmer, proficient in all the languages and shell tools. Review the prototype source code and propose changes to improve reliability, performance and maintainability, with a view to creating a finished product for distribution. Study the code carefully. Avoid long bullet points, use paragraphs instead. Always include code samples under each suggestion."
  fi

  prompt="Current date: $(date)
$prompt"

  # Generate code reviews
  generate_code_reviews "$model" "$task" "$output_dir" "$num_reviews" "$temperature" "$prompt" "$@"

  # Merge code reviews
  merge_code_reviews "$model" "$output_dir" "$num_reviews" "$@"

  # Merge input files
  merge_input_files "$output_dir" "$@"
    echo "step one done"
  # Generate final review
  generate_final_review "$model" "$output_dir" "$temperature"
}

# Call the main function
main "$@"
