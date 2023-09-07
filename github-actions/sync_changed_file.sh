#!/bin/bash

# Define the repository owner, repository name, and file path
owner="dave1010"
repo="hubcap"
file_path="hubcap.php"
sha_file="latest_sha.txt" # File to store the latest commit SHA

# Define your own repository information
own_owner="irthomasthomas"
own_repo="undecidability"
echo "Running Synch Changed Files"
# Intermediate local path to temporarily store the updated file
temp_file_path="/tmp/${file_path}"

# Read the previously stored SHA from the file
previous_sha=$(cat "$sha_file" 2>/dev/null)
echo "previous_sha: $previous_sha"
# Make a GET request to retrieve the latest commit information
response=$(curl -s "https://api.github.com/repos/$owner/$repo/commits?path=$file_path")

# Check if the request was successful
if [[ $(echo "$response" | jq -r "length") -gt 0 ]]; then
    latest_commit_sha=$(echo "$response" | jq -r ".[0].sha")

  # Compare the latest commit SHA with the previously stored SHA
  if [[ "$latest_commit_sha" != "$previous_sha" ]]; then
    echo "shas are different!"

    # Download the updated file
    curl -s "https://raw.githubusercontent.com/$owner/$repo/$latest_commit_sha/$file_path" -o "$temp_file_path"
    echo "https://raw.githubusercontent.com/$owner/$repo/$latest_commit_sha/$file_path $temp_file_path"
    echo "$PWD"
    echo "$file_path"
     # Copy the downloaded file to your local workspace
    cp "$temp_file_path" "$file_path"

    # Commit and push the changes to your own repository
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
    git add "$file_path"
    git commit -m "Update $file_path via GitHub Action"
    git push

    # Save the latest commit SHA to the file for future comparisons
    echo "$latest_commit_sha" > "$sha_file"

    echo "File copied successfully."
  else
    echo "No changes detected."
  fi
else
  echo "Error retrieving commit information."
fi
