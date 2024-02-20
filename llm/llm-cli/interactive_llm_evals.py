import sqlite3
import subprocess
import os
import sys
from getpass import getuser

# Function to execute a SQL query and return results
def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Function to interactively search prompts or responses using fzf
def search_entries(search_column):
    search_term = input(f"Enter search term for {search_column}: ") if search_column else input("Enter search term: ")

    # Add '%' wildcard for partial matching
    query = f"SELECT id, model, prompt, response FROM responses WHERE {search_column} LIKE '%{search_term}%' ORDER BY datetime_utc DESC;"
    results = query_db(query)

    if not results:
        print("No results found.")
        return

    for index, (id, model, prompt, response) in enumerate(results, start=1):
        short_prompt = prompt[:40]
        short_response = response[:40]
        print(f"{index}. {id} | {short_prompt[:30]}... | {short_response[:30]}...")

    choice = int(input("Enter the number of the desired entry: ")) - 1
    if 0 <= choice < len(results):
        return results[choice]

# Function to copy to clipboard
def copy_to_clipboard(response):
    try:
        subprocess.run(["xclip", "-selection", "clipboard"], input=response.encode(), check=True)
        print("Response copied to clipboard.")
    except subprocess.CalledProcessError as e:
        print(f"Error copying to clipboard: {e}")

# Function to open in a new terminal
def open_in_terminal(response):
    try:
        tempfile = f"/tmp/{getuser()}_temp_response_{os.getpid()}.txt"
        with open(tempfile, "w") as f:
            f.write(response)
        subprocess.run(["terminator", "-e", f"bash -c 'cat {tempfile}; exec bash'"], check=True)
        print("Response opened in new terminal.")
    except subprocess.CalledProcessError as e:
        print(f"Error opening in new terminal: {e}")

# Function to score a response
def score_response(response_id):
    scores = {"-2": -2, "-1": -1, "0": 0, "1": 1, "2": 2}
    score = input("Choose a score (-2 to +2): ")
    comment = input("Enter a comment (Good/Average/Poor): ")

    query = f"INSERT INTO evaluations (response_id, evaluation_grade, evaluation_comment) VALUES ('{response_id}', '{scores[score]}', '{comment}');"
    query_db(query)
    print("Response scored successfully.")

# Function to evaluate a response
def evaluate_response():
    chosen_entry = search_entries("prompt")
    if not chosen_entry:
        return

    response_id, _, _, response = chosen_entry
    print(f"Chosen response ID: {response_id}")

    actions = {
        "Copy to Clipboard": lambda: copy_to_clipboard(response),
        "Open in Terminal": lambda: open_in_terminal(response),
        "Score Response": lambda: score_response(response_id),
    }

    action_str = "\n".join([f"{i + 1}. {action}" for i, action in enumerate(actions.keys())])
    action_num = int(input(f"Choose action ({action_str}): ")) - 1
    if 0 <= action_num < len(actions):
        actions[list(actions.keys())[action_num]]()

# Text-based main menu function for the interactive LLM evaluations.
def main_menu():
    while True:
        print("\nMenu Options:")
        print("1) Search prompt")
        print("2) Search responses")
        print("3) Evaluate response")
        print("4) Exit")
        action = input("Please choose an option: ")

        
        if action == "1":
            search_entries("prompt") # Todo: Next steps after choosing a prompt (e.g. search responses, evaluate response, etc.)
        elif action == "2":
            search_entries("response")
        elif action == "3":
            evaluate_response()
        elif action == "4":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option, please try again.")

# Set the path to the database
DB_PATH = subprocess.check_output(["llm", "logs", "path"], universal_newlines=True).strip()

# Run the main menu
main_menu()