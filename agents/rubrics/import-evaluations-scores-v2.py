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
    overall_justification TEXT
);

CREATE TABLE IF NOT EXISTS response_eval (
    evaluation_id INTEGER,
    group_id INTEGER,
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
    for tag in ['goal_completion', 'coherence', 'learning', 'insight', 'creativity', 'emergence']:
        match = re.search(rf'<{tag}>(\d+)</{tag}>', xml_string)
        if match:
            data.append(int(match.group(1)))
        else:
            data.append(None)
            
    # Extract the overall justification if it exists
    justification_match = re.search(r'<justification>(.*?)</justification>', xml_string, re.DOTALL)
    overall_justification = justification_match.group(1).strip() if justification_match else None
    data.append(overall_justification)
    
    return tuple(data)

def extract_response_data(xml_string):
    data = []
    for tag in ['relevance', 'coherence', 'completeness', 'factuality', 'reasoning', 'adaptability', 'creativity', 'emergence']:
        match = re.search(rf'<{tag}>(\d+)</{tag}>', xml_string)
        if match:
            data.append(int(match.group(1)))
        else:
            data.append(None)
    # Extract the response justification if it exists
    justification_match = re.search(r'<justification>(.*?)</justification>', xml_string, re.DOTALL)
    justification = justification_match.group(1).strip() if justification_match else None
    data.append(justification)
    
    return tuple(data)

def parse_and_store(document, database_path, group_id, model_judge):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    print(f"group_id: {group_id}")

    # Extract the conversation portion
    conversation_match = re.search(r'<conversation>(.*?)</conversation>', document, re.DOTALL)
    evaluation_match = re.search(r'<evaluation>(.*?)</evaluation>', document, re.DOTALL)
    
    if conversation_match:
        conversation_xml = conversation_match.group(1)

        # Extract individual responses
        numbered_response_matches = re.finditer(r'<response index="(\d+)">(.*?)</response>', conversation_xml, re.DOTALL)

        responses = [(int(match.group(1)), match.group(2)) for match in numbered_response_matches]
        total_prompts = len(responses)
        
        # Extract overall evaluation
        overall_match = re.search(r'<overall>(.*?)</overall>', conversation_xml, re.DOTALL)
        if overall_match:
            overall_xml = overall_match.group(1)
            overall_data = extract_conversation_data(overall_xml)
            overall_data = (model_judge, group_id, total_prompts) + overall_data
            
            c.execute('INSERT INTO conversation_eval (model_judge, group_id, total_prompts, goal_completion, coherence, learning, insight, creativity, emergence, overall_justification) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', overall_data)
            evaluation_id = c.lastrowid

            for i, response_xml in responses:
                response_data = extract_response_data(response_xml)
                values = (evaluation_id, group_id, i) + response_data
                c.execute('INSERT INTO response_eval (evaluation_id, group_id, response_number, relevance, coherence, completeness, factuality, reasoning, adaptability, creativity, emergence, justification) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)

    if evaluation_match:
        evaluation_xml = evaluation_match.group(1)

        # Extract individual responses
        numbered_response_matches = re.finditer(r'<response index="(\d+)">(.*?)</response>', evaluation_xml, re.DOTALL)

        responses = [(int(match.group(1)), match.group(2)) for match in numbered_response_matches]
        total_prompts = len(responses)

        # Extract overall evaluation
        overall_match = re.search(r'<overall>(.*?)</overall>', evaluation_xml, re.DOTALL)
        if overall_match:
            overall_xml = overall_match.group(1)
            overall_data = extract_conversation_data(overall_xml)
            overall_data = (model_judge, group_id, total_prompts) + overall_data

            c.execute('INSERT INTO conversation_eval (model_judge, group_id, total_prompts, goal_completion, coherence, learning, insight, creativity, emergence, overall_justification) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', overall_data)
            evaluation_id = c.lastrowid

            for i, response_xml in responses:
                response_data = extract_response_data(response_xml)
                values = (evaluation_id, group_id, i) + response_data
                c.execute('INSERT INTO response_eval (evaluation_id, group_id, response_number, relevance, coherence, completeness, factuality, reasoning, adaptability, emergence, justification) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    document_path = sys.argv[1]  # Take the first argument as the input XML document path
    db_path = sys.argv[2]
    group_id = int(sys.argv[3])
    model_judge = sys.argv[4]

    with open(document_path, 'r', encoding='utf-8') as file:
        document = file.read()

    create_database(db_path)
    parse_and_store(document, db_path, group_id, model_judge)