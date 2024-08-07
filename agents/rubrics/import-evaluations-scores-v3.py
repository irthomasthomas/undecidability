import sqlite3
import re
import sys

# Adjust these SQL commands according to your database schema
CREATE_TABLES_SQL = """
BEGIN;

CREATE TABLE IF NOT EXISTS conversation_eval (
    evaluation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_judge TEXT,
    group_id INTEGER,
    total_prompts INTEGER,
    goal_completion INTEGER,
    coherence INTEGER,
    learning INTEGER,
    insight INTEGER,
    creativity INTEGER,
    emergence INTEGER,
    justification TEXT
);

CREATE TABLE IF NOT EXISTS response_eval (
    evaluation_id INTEGER,
    response_number INTEGER,
    relevance INTEGER,
    coherence INTEGER,
    completeness INTEGER,
    factuality INTEGER,
    reasoning INTEGER,
    adaptability INTEGER,
    creativity INTEGER,
    emergence INTEGER,
    justification TEXT,
    FOREIGN KEY (evaluation_id) REFERENCES conversation_eval (evaluation_id)
);

CREATE TABLE IF NOT EXISTS rubric (
    rubric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rubric_text TEXT,
    model_judge TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
"""

def create_database(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.executescript(CREATE_TABLES_SQL)
    conn.commit()
    conn.close()

def extract_conversation_data(xml_string):
    data = []
    justification = None
    
    for tag in ['goal_completion', 'coherence', 'learning', 'insight', 'creativity', 'emergence']:
        match = re.search(rf'<{tag}>(\d+)</{tag}>', xml_string)
        if match:
            data.append(int(match.group(1)))
        else:
            if tag == "emergence":
                data.append(None)
            else:
                data.append(None)
    
    justification_match = re.search(r'<justification>(.*?)</justification>', xml_string, re.DOTALL)
    if justification_match:
        justification = justification_match.group(1).strip()
    data.append(justification)
    
    return tuple(data)

def extract_response_data(xml_string):
    data = []
    justification = None
    
    for tag in ['relevance', 'coherence', 'completeness', 'factuality', 'reasoning', 'adaptability', 'creativity', 'emergence']:
        match = re.search(rf'<{tag}>(\d+)</{tag}>', xml_string)
        if match:
            data.append(int(match.group(1)))
        else:
            if tag == "emergence":
                data.append(None)
            else:
                data.append(None)
    
    justification_match = re.search(r'<justification>(.*?)</justification>', xml_string, re.DOTALL)
    if justification_match:
        justification = justification_match.group(1).strip()
    data.append(justification)
    
    return tuple(data)

def insert_conversation_overall(c, model_judge, group_id, total_prompts, overall_data):
    query = """
    INSERT INTO conversation_eval (model_judge, group_id, total_prompts, goal_completion, coherence, learning, insight, creativity, emergence, justification) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    c.execute(query, (model_judge, group_id, total_prompts) + overall_data)

def insert_response_eval(c, evaluation_id, response_number, response_data):
    query = """
    INSERT INTO response_eval (evaluation_id, response_number, relevance, coherence, completeness, factuality, reasoning, adaptability, creativity, emergence, justification) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    c.execute(query, (evaluation_id, response_number) + response_data)

def parse_and_store(filepath, database_path, group_id, model_judge):
    with open(filepath, 'r') as file:
        document = file.read()

    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    print(f"group_id: {group_id}")

    matches = re.findall(r'<evaluation_one>(.*?)</evaluation_one>', document, re.DOTALL)
    if not matches:
        matches = re.findall(r'<evaluation_two>(.*?)</evaluation_two>', document, re.DOTALL)
    
    for match in matches:
        # Extract the overall portion
        overall_match = re.search(r'<overall>(.*?)</overall>', match, re.DOTALL)
        if overall_match:
            overall_xml = overall_match.group(1)
            overall_data = extract_conversation_data(overall_xml)
            total_prompts = len(re.findall(r'<response\s*(?:index="\d+")?>.*?</response>', match, re.DOTALL))
            insert_conversation_overall(c, model_judge, group_id, total_prompts, overall_data)
            evaluation_id = c.lastrowid

            # Extract individual responses
            response_matches = re.finditer(r'<response\s*index="(\d+)">(.*?)</response>', match, re.DOTALL)
            for response_match in response_matches:
                response_index = int(response_match.group(1))
                response_xml = response_match.group(2)
                response_data = extract_response_data(response_xml)
                insert_response_eval(c, evaluation_id, response_index, response_data)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    filepath = sys.argv[1]  # Take the first argument as the input XML document path
    db_path = sys.argv[2]
    group_id = sys.argv[3] 
    model_judge = sys.argv[4]
    
    create_database(db_path)
    parse_and_store(filepath, db_path, group_id, model_judge)