**Prompt:**
Here is a sqlite db schema for the llm-cli tool database. When a request is made from llm-cli to openai gpt3 completions api, the result is stored in this database. I wish to update the schema to support a new feature: Human grading of the output. We will start with a basic feature set to support HUMAN EVALS. Propose a schema change. 

CREATE TABLE [_llm_migrations] (
   [name] TEXT PRIMARY KEY,
   [applied_at] TEXT
);
CREATE TABLE IF NOT EXISTS "logs" (
   [id] INTEGER PRIMARY KEY,
   [model] TEXT,
   [prompt] TEXT,
   [system] TEXT,
   [prompt_json] TEXT,
   [options_json] TEXT,
   [response] TEXT,
   [response_json] TEXT,
   [reply_to_id] INTEGER REFERENCES [logs]([id]),
   [chat_id] INTEGER REFERENCES [logs]([id]),
   [duration_ms] INTEGER,
   [datetime_utc] TEXT
);
CREATE TABLE [conversations] (
   [id] TEXT PRIMARY KEY,
   [name] TEXT,
   [model] TEXT
);
CREATE TABLE [responses] (
   [id] TEXT PRIMARY KEY,
   [model] TEXT,
   [prompt] TEXT,
   [system] TEXT,
   [prompt_json] TEXT,
   [options_json] TEXT,
   [response] TEXT,
   [response_json] TEXT,
   [conversation_id] TEXT REFERENCES [conversations]([id]),
   [duration_ms] INTEGER,
   [datetime_utc] TEXT
);
CREATE VIRTUAL TABLE [responses_fts] USING FTS5 (
    [prompt], [response],
    content=[responses]
)
/* responses_fts(prompt,response) */;
CREATE TABLE IF NOT EXISTS 'responses_fts_data'(id INTEGER PRIMARY KEY, block BLOB);
CREATE TABLE IF NOT EXISTS 'responses_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS 'responses_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);
CREATE TABLE IF NOT EXISTS 'responses_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;
CREATE TRIGGER [responses_ai] AFTER INSERT ON [responses] BEGIN
  INSERT INTO [responses_fts] (rowid, [prompt], [response]) VALUES (new.rowid, new.[prompt], new.[response]);
END;
CREATE TRIGGER [responses_ad] AFTER DELETE ON [responses] BEGIN
  INSERT INTO [responses_fts] ([responses_fts], rowid, [prompt], [response]) VALUES('delete', old.rowid, old.[prompt], old.[response]);
END;
CREATE TRIGGER [responses_au] AFTER UPDATE ON [responses] BEGIN
  INSERT INTO [responses_fts] ([responses_fts], rowid, [prompt], [response]) VALUES('delete', old.rowid, old.[prompt], old.[response]);
  INSERT INTO [responses_fts] (rowid, [prompt], [response]) VALUES (new.rowid, new.[prompt], new.[response]);
END;

**Response:**
Based on the requirement to support human grading of responses, you can add a new table named "evaluations". Here is how the schema change might look:

CREATE TABLE [evaluations] (
   [id] INTEGER PRIMARY KEY,
   [response_id] TEXT REFERENCES [responses]([id]),
   [evaluator_id] TEXT,
   [evaluation_grade] INTEGER,
   [evaluation_comment] TEXT,
   [evaluation_date] TEXT
);
Explanation:
1. `id`: The primary identifier for each evaluation.
2. `response_id`: This is a foreign key referencing the responses on which the evaluation was done.
3. `evaluator_id`: This field can hold the identifier of the user who did the evaluation.
4. `evaluation_grade`: This field will store the grade given by the evaluator. For simplicity, it can be an integer (e.g., 1-5 for a five-point scale evaluation).
5. `evaluation_comment`: This is a text field where evaluators can optionally leave a comment about their evaluation.
6. `evaluation_date`: The date when the evaluation was made.

This schema allows for each response to be graded by multiple evaluators, and it records who made the evaluation and when. If necessary, it can be extended to include more information about the context or content of the evaluation.

<details><summary>Metadata</summary>

- Duration: 27513 ms
- Datetime: 2023-10-19T11:19:00.350453
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
Add that to a bash script. Before making changes, backup the db which can be found at: $(llm logs path)

**Response:**
#!/bin/bash

# Get the path to the llm logs
DB_PATH=$(llm logs path)

# Create a backup of the db
cp $DB_PATH ${DB_PATH}_bak_$(date +%Y%m%d%H%M%S)

# Apply the sql schema changes
# Store the sql command in a variable
SQL_COMMAND="CREATE TABLE [evaluations] (
[id] INTEGER PRIMARY KEY,
[response_id] TEXT REFERENCES [responses]([id]),
[evaluator_id] TEXT,
[evaluation_grade] INTEGER,
[evaluation_comment] TEXT,
[evaluation_date] TEXT
);"

# Run the sql command
echo $SQL_COMMAND | sqlite3 $DB_PATH

# Print a success message
echo "Database schema updated successfully. A backup of the original database was created at path: ${DB_PATH}_bak_$(date +%Y%m%d%H%M%S)"

<details><summary>Metadata</summary>

- Duration: 18709 ms
- Datetime: 2023-10-19T11:20:17.768778
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

