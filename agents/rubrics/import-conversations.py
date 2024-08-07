import sqlite3
import sys

def fetch_conversation_data_from_main_db(main_db_path, conversation_ids):
    conn_main = sqlite3.connect(main_db_path)
    c_main = conn_main.cursor()

    query = "SELECT * FROM responses WHERE conversation_id IN ({seq})".format(
        seq=','.join(['?']*len(conversation_ids))
    )
    c_main.execute(query, conversation_ids)
    conversations = c_main.fetchall()

    conn_main.close()
    return conversations

def insert_conversations_into_target_db(target_db_path, conversations, group_id):
    conn_target = sqlite3.connect(target_db_path)
    c_target = conn_target.cursor()

    insert_query = """INSERT INTO responses
                      (id, model, prompt, system, prompt_json, options_json, response, response_json, conversation_id, duration_ms, datetime_utc, human_vote, human_note, bookmark, group_id)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    conversations_with_group_id = [(*conv[:14], group_id) for conv in conversations]

    c_target.executemany(insert_query, conversations_with_group_id)
    conn_target.commit()
    conn_target.close()

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: python import-conversations.py <main_db_path> <target_db_path> <group_id> <conversation_id1> <conversation_id2> ...")
        exit(1)

    main_db_path = sys.argv[1]
    target_db_path = sys.argv[2]
    group_id = int(sys.argv[3])
    conversation_ids = sys.argv[4:]

    conversations = fetch_conversation_data_from_main_db(main_db_path, conversation_ids)
    if not conversations:
        print("No conversations found for the provided conversation IDs")
    else:
        insert_conversations_into_target_db(target_db_path, conversations, group_id)
        print(f"Inserted {len(conversations)} records into the target database with group_id {group_id}.")