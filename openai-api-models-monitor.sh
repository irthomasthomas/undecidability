#!/bin/bash

# Store your API key.
OPENAI_API_KEY=your_api_key

# Run the API call and generate the initial CSV.
initial_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY")
echo $initial_snapshot | jq -r '.data[] | [.id, .object, .created, .owned_by] | @csv' > old_output.csv

# Go into an infinite loop.
while true; do
    # Request the latest data.
    latest_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY")
    echo $latest_snapshot | jq -r '.data[] | [.id, .object, .created, .owned_by] | @csv' > new_output.csv

    # Compare the CSV files.
    if ! diff -q old_output.csv new_output.csv > /dev/null; then
        # If there's any difference, print it out.
        echo "Change detected:"
        diff -y --suppress-common-lines --color old_output.csv new_output.csv

        # Now, take the latest snapshot as the new initial snapshot.
        mv new_output.csv old_output.csv
    fi

    # Wait for 30 seconds before the next API call.
    sleep 30
done