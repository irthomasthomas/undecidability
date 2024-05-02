import sqlite3
import sys
import sys

def get_results_as_markdown(db_path, group_id):
  """
  Retrieves results from the 'responses' table for a specific group ID and formats them as a markdown block.

  Args:
    db_path (str): Path to the SQLite database file.
    group_id (int): The ID of the group to retrieve results for.

  Returns:
    str: A markdown-formatted string containing the results.
  """

  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row  # Access rows by column name

  cursor = conn.cursor()
  cursor.execute(
      "SELECT id, prompt, system, response, group_id FROM responses WHERE group_id = ?", (group_id,)
  )
  results = cursor.fetchall()
  conn.close()

  num_results = len(results)
  index = 1
  markdown_output = f"<group_id>{group_id}</group_id>\n\n<total_prompts>{num_results}</total_prompts><**System Prompt**> {results[0]['system']} </**System Prompt**>"
  for result in results:
    markdown_output += f"""
  <prompt_index>{index}</prompt_index>

  <**User Prompt**> {result["prompt"]} </**User Prompt**>


  <**Response**> {result["response"]} </**Response**>

  ---------------------------------------

  """
    index += 1

  return markdown_output

# Example usage:
db_path = "/home/ShellLM/shelllm.db"  # Replace with your actual database path
# group_id from the command line argument
group_id = sys.argv[1]

markdown_results = get_results_as_markdown(db_path, group_id)
print(markdown_results)