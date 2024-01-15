**Prompt:**
Here is DB schema. How do I delete a given log record so all tables are correctly updated? CREATE TABLE [_llm_migrations] (
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
CREATE TABLE [evaluations] ( [id] INTEGER PRIMARY KEY, [response_id] TEXT REFERENCES [responses]([id]), [evaluation_grade] INTEGER, [evaluation_comment] TEXT, [evaluation_date] TEXT );

**Response:**
To delete a given log record and update all related tables, you need to perform the following steps:

1. Identify the log record you want to delete based on its unique identifier (e.g., `id`).
2. Delete the record from the `logs` table using the following SQL statement:

   ```sql
   DELETE FROM logs WHERE id = <log_id>;
   ```

   Replace `<log_id>` with the actual ID of the log record you want to delete.

3. Delete any related records from the `responses` table that reference the deleted log record. Use the following SQL statement:

   ```sql
   DELETE FROM responses WHERE chat_id = <log_id> OR reply_to_id = <log_id>;
   ```

   Replace `<log_id>` with the actual ID of the log record you want to delete.

4. If necessary, update any other tables that have foreign key references to the deleted log record. For example, if the `conversations` table has a foreign key reference to the `logs` table, you may need to update it accordingly.

   ```sql
   UPDATE conversations SET log_id = NULL WHERE log_id = <log_id>;
   ```

   Replace `<log_id>` with the actual ID of the log record you want to delete.

5. Finally, if you have any full-text search tables or triggers related to the `responses` table, you may need to update or delete corresponding records as well. Refer to the specific schema and triggers for more details.

Remember to replace `<log_id>` with the actual ID of the log record you want to delete in the SQL statements.

<details><summary>Metadata</summary>

- Duration: 25642 ms
- Datetime: 2023-10-26T11:44:49.060647
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

