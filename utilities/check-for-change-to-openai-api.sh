#!/bin/bash
echo "script to alert to new api's"

# Store the initial snapshot of data.
initial_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY")
echo "initial_snapshot"
echo "${initial_snapshot:0:40}"
# Go into an infinite loop.
while true; do
    # Request the latest data.
    latest_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY")
    echo "latest_snapshot"
    echo "${latest_snapshot:0:40}"
    # Compare the initial and latest data.
    if [[ "$initial_snapshot" != "$latest_snapshot" ]]; then
        # If there's any change, print out a message.
        echo "Alert: Detected a change."
        kdialog --msgbox "Alert: Detected a change in OpenAI API."

        # Now, store the latest snapshot as the new initial snapshot.
        initial_snapshot=$latest_snapshot
    else
        echo "No change"
    fi

    # Wait for 30 seconds before the next API call.
    sleep 30
done
