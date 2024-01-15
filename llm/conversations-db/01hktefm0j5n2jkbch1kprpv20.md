**Prompt:**
Make this content into a pretty gh markdown note:quote:- [ ] [Support for plugins that implement vector indexes · Issue #216 · simonw/llm](https://github.com/simonw/llm/issues/216)

@simonw happy to help here

Here is how Chroma's roadmap aligns with your goals.

The internals of Chroma are set up to have pluggable indexes on top of collections - we haven't yet exposed this to end users. But will fairly soon. We also plan to have a "smart index" that does KNN brute force and then a cutover to ANN.
Indexes over multiple collections - while I do understand the use case - we've chosen to not prioritize this as it adds a lot of DX complexity. We instead encourage users to eat the "read amplification" and query multiple collections/indexes and then cull/rerank themselves client side.
You may also enjoy reading this chroma proposal where we have put a lot of thought into the pipelines to support index/collection creation and access - chroma-core/chroma#1110
  dave1010 mentioned this issue 
Add option for RAG-style augmentation dave1010/clipea#1
Open

IvanVas commented 
If someone ever need to move data from llm to Chroma, below is a simple script to do so. Needs a little more work to productise it though.

@simonw, hope it would help if you ever need to create smth like llm embed-multi migrate --chroma

import sqlite3
import struct
import chromadb


def decode(binary):
    if not isinstance(binary, bytes):
        raise ValueError("Binary data must be of bytes type")
    return struct.unpack("<" + "f" * (len(binary) // 4), binary)


client = chromadb.PersistentClient(path="chroma.db") # FIXME

collectionName = "collection" # FIXME
collection = client.get_or_create_collection(collectionName)

# Path to your SQLite database
db_path = "/Users/username/Library/Application Support/io.datasette.llm/embeddings.db" # FIXME

# Query to retrieve embeddings
llm_collection = "fixme" # FIXME
query = f"""
SELECT id, embedding, content FROM embeddings WHERE collection_id = (
    SELECT id FROM collections WHERE name = "{llm_collection}" 
)
"""


def parse_id(id_str):
    # FIXME parse metadata

    return {
        "meta1": "meta1",
    }


def main(db_path, batch_size=1000):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query the embeddings table
    cursor.execute(query)
    rows = cursor.fetchall() # FIXME assumes there is not MUCH data, works fine for x100k records

    # Initialize batch variables
    batch_embeddings = []
    batch_documents = []  # You'll need to adjust how you handle documents
    batch_metadatas = []  # You'll need to adjust how you handle metadatas
    batch_ids = []

    for i, (id, embedding, content) in enumerate(rows):
        idParsed = parse_id(id)

        # Decode the binary data
        decoded_embedding = decode(embedding)

        # Append to the batch
        batch_embeddings.append(list(decoded_embedding))
        batch_documents.append(content)
        batch_metadatas.append({"meta1": idParsed['meta1']}) # FIXME
        batch_ids.append(id)

        # When batch size is reached or end of rows
        if len(batch_embeddings) == batch_size or i == len(rows) - 1:
            collection.add(
                embeddings=batch_embeddings,
                documents=batch_documents,
                metadatas=batch_metadatas,
                ids=batch_ids
            )

            print(f"Added {len(batch_embeddings)} rows to chromaDb (Total: {i + 1})")

            # Reset batch variables
            batch_embeddings = []
            batch_documents = []
            batch_metadatas = []
            batch_ids = []

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main(db_path)

#### Suggested labels
#### {   "key": "llm-experiments",   "value": "Experiment results and tools related to Large Language Models" } {   "key": "llm-inference-engines",   "value": "Software for running inference on Large Language Models" }

**Response:**
> **Note:**
> 
> - [ ] [Support for plugins that implement vector indexes · Issue #216 · simonw/llm](https://github.com/simonw/llm/issues/216)
> 
> @simonw happy to help here
> 
> Here is how Chroma's roadmap aligns with your goals.
> 
> The internals of Chroma are set up to have pluggable indexes on top of collections - we haven't yet exposed this to end users. But will fairly soon. We also plan to have a "smart index" that does KNN brute force and then a cutover to ANN.
> 
> Indexes over multiple collections - while I do understand the use case - we've chosen to not prioritize this as it adds a lot of DX complexity. We instead encourage users to eat the "read amplification" and query multiple collections/indexes and then cull/rerank themselves client side.
> 
> You may also enjoy reading this chroma proposal where we have put a lot of thought into the pipelines to support index/collection creation and access - [chroma-core/chroma#1110](https://github.com/chroma-core/chroma/issues/1110)
> 
> @dave1010 mentioned this issue 
> Add option for RAG-style augmentation [dave1010/clipea#1](https://github.com/dave1010/clipea/issues/1)
> Open
> 
> @IvanVas commented 
> If someone ever need to move data from llm to Chroma, below is a simple script to do so. Needs a little more work to productise it though.
> 
> @simonw, hope it would help if you ever need to create smth like llm embed-multi migrate --chroma
> 
> ```python
> import sqlite3
> import struct
> import chromadb
> 
> def decode(binary):
>     if not isinstance(binary, bytes):
>         raise ValueError("Binary data must be of bytes type")
>     return struct.unpack("<" + "f" * (len(binary) // 4), binary)
> 
> client = chromadb.PersistentClient(path="chroma.db") # FIXME
> 
> collectionName = "collection" # FIXME
> collection = client.get_or_create_collection(collectionName)
> 
> # Path to your SQLite database
> db_path = "/Users/username/Library/Application Support/io.datasette.llm/embeddings.db" # FIXME
> 
> # Query to retrieve embeddings
> llm_collection = "fixme" # FIXME
> query = f"""
> SELECT id, embedding, content FROM embeddings WHERE collection_id = (
>     SELECT id FROM collections WHERE name = "{llm_collection}" 
> )
> """
> 
> def parse_id(id_str):
>     # FIXME parse metadata
>     return {
>         "meta1": "meta1",
>     }
> 
> def main(db_path, batch_size=1000):
>     # Connect to the SQLite database
>     conn = sqlite3.connect(db_path)
>     cursor = conn.cursor()
> 
>     # Query the embeddings table
>     cursor.execute(query)
>     rows = cursor.fetchall() # FIXME assumes there is not MUCH data, works fine for x100k records
> 
>     # Initialize batch variables
>     batch_embeddings = []
>     batch_documents = []  # You'll need to adjust how you handle documents
>     batch_metadatas = []  # You'll need to adjust how you handle metadatas
>     batch_ids = []
> 
>     for i, (id, embedding, content) in enumerate(rows):
>         idParsed = parse_id(id)
> 
>         # Decode the binary data
>         decoded_embedding = decode(embedding)
> 
>         # Append to the batch
>         batch_embeddings.append(list(decoded_embedding))
>         batch_documents.append(content)
>         batch_metadatas.append({"meta1": idParsed['meta1']}) # FIXME
>         batch_ids.append(id)
> 
>         # When batch size is reached or end of rows
>         if len(batch_embeddings) == batch_size or i == len(rows) - 1:
>             collection.add(
>                 embeddings=batch_embeddings,
>                 documents=batch_documents,
>                 metadatas=batch_metadatas,
>                 ids=batch_ids
>             )
> 
>             print(f"Added {len(batch_embeddings)} rows to chromaDb (Total: {i + 1})")
> 
>             # Reset batch variables
>             batch_embeddings = []
>             batch_documents = []
>             batch_metadatas = []
>             batch_ids = []
> 
>     # Close the database connection
>     conn.close()
> 
> if __name__ == "__main__":
>     main(db_path)
> ```
> 
> #### Suggested labels
> 
> - { "key": "llm-experiments", "value": "Experiment results and tools related to Large Language Models" }
> - { "key": "llm-inference-engines", "value": "Software for running inference on Large Language Models" }

<details><summary>Metadata</summary>

- Duration: 18920 ms
- Datetime: 2024-01-10T19:44:23.081178
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

