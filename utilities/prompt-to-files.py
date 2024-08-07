import os
import anthropic
import xml.etree.ElementTree as ET

# Initialize the Anthropic client
client = anthropic.Anthropic()

COMPLETION_TOKEN = "<DONE>"
MAX_TOKENS = 1000

def generate_files(prompt):
    full_response = ""
    continuation = ""

    while True:
        # Create the message with XML structure
        message = f"""
        <task>
            <instruction>
            Create the following files based on the given prompt. For each file, provide the content wrapped in XML tags with the filename as the tag name.
            If the content is too long to fit in one response, end your response with an open tag for the next file or continuation of the current file.
            When you have completed all files, end your response with the token {COMPLETION_TOKEN}.
            </instruction>
            <prompt>{prompt}</prompt>
            <continuation>{continuation}</continuation>
        </task>
        """

        # Call the Anthropic API
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": message}
            ]
        )

        response_text = response.content[0].text
        full_response += response_text

        if COMPLETION_TOKEN in response_text:
            break

        # Set continuation for the next iteration
        continuation = "Continue from where you left off."

    # Parse the full response
    try:
        root = ET.fromstring(f"<root>{full_response.replace(COMPLETION_TOKEN, '')}</root>")
        for element in root:
            filename = element.tag
            content = element.text.strip() if element.text else ""
            
            # Append to file if it already exists, otherwise create new file
            mode = 'a' if os.path.exists(filename) else 'w'
            with open(filename, mode) as f:
                f.write(content)
            print(f"{'Updated' if mode == 'a' else 'Created'} file: {filename}")
    except ET.ParseError as e:
        print(f"Error parsing the response: {e}")
        print("Raw response:", full_response)
        

prompt = """Create a Python script that implements a complex algorithm (e.g., a machine learning model or a graph traversal algorithm). 
The script should be well-commented and include error handling. Also, create a comprehensive README.md file explaining the algorithm, 
its implementation, how to use the script, and include examples."""

generate_files(prompt)