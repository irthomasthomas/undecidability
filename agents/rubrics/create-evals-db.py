import sqlite3

# Define database file path
db_file = "evaluation.db"

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS response_scores (
    index INTEGER PRIMARY KEY,
    justification TEXT,
    relevance INTEGER,
    coherence INTEGER,
    completeness INTEGER,
    factuality INTEGER,
    reasoning INTEGER,
    adaptability INTEGER,
    emergence INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS session_scores (
    id INTEGER PRIMARY KEY,
    justification TEXT,
    goal_completion INTEGER,
    coherence INTEGER,
    learning INTEGER,
    insight INTEGER,
    creativity INTEGER,
    emergence INTEGER
)
''')