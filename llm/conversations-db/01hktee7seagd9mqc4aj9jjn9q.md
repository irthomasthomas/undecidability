**Prompt:**
Make this content into a pretty gh markdown note:quote:- [ ] [Support for plugins that implement vector indexes · Issue #216 · simonw/llm](https://github.com/simonw/llm/issues/216)

The llm similar and collection.similar() methods currently implement the slowest brute-force approach.

I want to support faster approaches for this, like sqlite-vss and FAISS and and Pinecone and suchlike... but I'd like to do so through plugins.

Many vector indexes need to be rebuilt periodically, so I need an abstraction that supports that.

I added a modified column to the embeddings table in:

Add updated timestamp to embeddings table #211
With the aim of supporting this feature. I want indexes to be able to scan that table to see which items have been added or modified since they last ran, then re-index just those records.
  simonw added plugins  design  labels 
 simonw added this to the 0.9 - embeddings milestone 

Owner
Author
simonw commented 
I think the user gets to create indexes, where an index can be assigned to one or more collection (provided those collections used the same embedding model).

Allowing a collection to have multiple indexes will support trying out different indexes and comparing their performance.

Allowing an index to cover multiple collections is important for things like wanting to be able to run a similarity search that mixes TILs and blog posts and tweets, despite them being held in different embedding collections.

So I think there are CLI and Python methods for:

Defining a new index, which is associated with one or more collections
Causing that index to build, or rebuild
Running similar searches against a specified index
Do the existing llm similar and collection.similar() methods gain these abilities automatically?

Maybe yes if a collection has a "default index" defined on it, otherwise no.
  simonw removed this from the 0.9 - embeddings milestone 
 simonw added the embeddings  label 
 simonw mentioned this issue 
Mention brute force approach in docs #214
Closed
simonw added a commit that referenced this issue 

Mention brute-force approach, link to vector indexing issue  …
 
f842fbe

Owner
Author
simonw commented 
Also worth considering if the trick I used here might fit into LLM somehow:

Add an aggregate function for querying a subset of rows datasette-faiss#3
The idea there is that sometimes you want to combine a similarity search with other filters - e.g. run a SQL query to filter for just posts in a specific category, then find the most similar matches to a vector from that subset - it can actually be faster to run the filter, then build a scratch index against just the ~1,000 rows that match it. Building a FAISS index across a few thousand items for example is fast enough that it's a better approach than trying to query the whole similarity index first.

Though it's worth testing that against brute-force similarity matching too, it might turn out that once you get below ~1,000 items you should just brute-force run the comparisons and not even bother with the index.

In any case, will the LLM indexing mechanism need to solve for this kind of filtering as well? It might well be out of scope.
  simonw mentioned this issue 
Add an aggregate function for querying a subset of rows simonw/datasette-faiss#3
Closed

dave1010 commented 
If this gets added then Chroma DB may be worth trying here. It's lightweight and incredibly easy to get running compared to a few others I've tried. https://docs.trychroma.com/
  simonw mentioned this issue 
Research ways to speed up brute force cosine similarity #246
Open

Owner
Author
simonw commented  • 
Ooh Chroma does look good - looks very easy to get it to store an index on disk: https://docs.trychroma.com/usage-guide

Looks like the actual indexing is handled by hnswlib - actually by their fork of it: https://github.com/chroma-core/hnswlib
 
Owner
Author
simonw commented 
Another option for an index could just be PyTorch with an in-memory collection of tensors.

I ran some benchmarks that looked good:



But when I tried a rough implementation like this it ended up slower than native Python (according to a time llm similar ... benchmark):

diff --git a/llm/embeddings.py b/llm/embeddings.py
index 32d7dc8..54741ee 100644
--- a/llm/embeddings.py
+++ b/llm/embeddings.py
@@ -9,6 +9,12 @@ from sqlite_utils.db import Table
 import time
 from typing import cast, Any, Dict, Iterable, List, Optional, Tuple, Union
 
+try:
+    import torch
+    import torch.nn.functional as F
+except ImportError:
+    torch = None
+
 
 @dataclass
 class Entry:
@@ -242,6 +248,30 @@ class Collection:
         """
         import llm
 
+        if torch is not None:
+            ids_and_embeddings = [
+                (row["id"], torch.tensor(llm.decode(row["embedding"])))
+                for row in self.db.query(
+                    "select id, embedding from embeddings where collection_id = ?",
+                    [self.id],
+                )
+            ]
+            input_vector = torch.tensor(vector)
+            scores = [
+                (id, F.cosine_similarity(input_vector.unsqueeze(0), embedding.unsqueeze(0)))
+                for id, embedding in ids_and_embeddings
+            ]
+            scores.sort(key=lambda id_and_score: id_and_score[1], reverse=True)
+            return [
+                Entry(
+                    id=id,
+                    score=score.item(),
+                    content=None,
+                    metadata=None,
+                )
+                for id, score in scores[:number]
+            ]
+
         def distance_score(other_encoded):
             other_vector = llm.decode(other_encoded)
             return llm.cosine_similarity(other_vector, vector)
Maybe I did something wrong here though. Would be worth spending more time seeing if PyTorch against an in-memory array can speed things up.
 
jeffchuber commented 
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
#### {   "key": "vector-indexing",   "value": "Implementing faster approaches like sqlite-vss, FAISS, Pinecone through plugins and managing periodic rebuilds" }

**Response:**
> **Note:**
> 
> - [ ] [Support for plugins that implement vector indexes · Issue #216 · simonw/llm](https://github.com/simonw/llm/issues/216)
> 
> The `llm similar` and `collection.similar()` methods currently implement the slowest brute-force approach.
> 
> I want to support faster approaches for this, like sqlite-vss and FAISS and Pinecone and suchlike... but I'd like to do so through plugins.
> 
> Many vector indexes need to be rebuilt periodically, so I need an abstraction that supports that.
> 
> I added a modified column to the embeddings table in:
> 
> [Add updated timestamp to embeddings table #211](https://github.com/simonw/llm/issues/211)
> 
> With the aim of supporting this feature. I want indexes to be able to scan that table to see which items have been added or modified since they last ran, then re-index just those records.
> 
> `simonw` added `plugins`, `design`, `labels`
> 
> `simonw` added this to the `0.9 - embeddings` milestone
> 
> **Owner**
> **Author**
> `simonw` commented 
> I think the user gets to create indexes, where an index can be assigned to one or more collection (provided those collections used the same embedding model).
> 
> Allowing a collection to have multiple indexes will support trying out different indexes and comparing their performance.
> 
> Allowing an index to cover multiple collections is important for things like wanting to be able to run a similarity search that mixes TILs and blog posts and tweets, despite them being held in different embedding collections.
> 
> So I think there are CLI and Python methods for:
> 
> - Defining a new index, which is associated with one or more collections
> - Causing that index to build, or rebuild
> - Running similar searches against a specified index
> 
> Do the existing `llm similar` and `collection.similar()` methods gain these abilities automatically?
> 
> Maybe yes if a collection has a "default index" defined on it, otherwise no.
> 
> `simonw` removed this from the `0.9 - embeddings` milestone
> 
> `simonw` added the `embeddings` label
> 
> `simonw` mentioned this issue 
> [Mention brute force approach in docs #214](https://github.com/simonw/llm/issues/214)
> 
> **Closed**
> 
> `simonw` added a commit that referenced this issue 
> 
> [Mention brute-force approach, link to vector indexing issue](https://github.com/simonw/llm/commit/f842fbe) 
> 
> **Owner**
> **Author**
> `simonw` commented 
> Also worth considering if the trick I used here might fit into LLM somehow:
> 
> [Add an aggregate function for querying a subset of rows datasette-faiss#3](https://github.com/simonw/datasette-faiss/issues/3)
> 
> The idea there is that sometimes you want to combine a similarity search with other filters - e.g. run a SQL query to filter for just posts in a specific category, then find the most similar matches to a vector from that subset - it can actually be faster to run the filter, then build a scratch index against just the ~1,000 rows that match it. Building a FAISS index across a few thousand items for example is fast enough that it's a better approach than trying to query the whole similarity index first.
> 
> Though it's worth testing that against brute-force similarity matching too, it might turn out that once you get below ~1,000 items you should just brute-force run the comparisons and not even bother with the index.
> 
> In any case, will the LLM indexing mechanism need to solve for this kind of filtering as well? It might well be out of scope.
> 
> `simonw` mentioned this issue 
> [Add an aggregate function for querying a subset of rows simonw/datasette-faiss#3](https://github.com/simonw/datasette-faiss/issues/3)
> 
> **Closed**
> 
> `dave1010` commented 
> If this gets added then Chroma DB may be worth trying here. It's lightweight and incredibly easy to get running compared to a few others I've tried. [https://docs.trychroma.com/](https://docs.trychroma.com/)
> 
> `simonw` mentioned this issue 
> [Research ways to speed up brute force cosine similarity #246](https://github.com/simonw/llm/issues/246)
> 
> **Open**
> 
> **Owner**
> **Author**
> `simonw` commented  • 
> Ooh Chroma does look good - looks very easy to get it to store an index on disk: [https://docs.trychroma.com/usage-guide](https://docs.trychroma.com/usage-guide)
> 
> Looks like the actual indexing is handled by hnswlib - actually by their fork of it: [https://github.com/chroma-core/hnswlib](https://github.com/chroma-core/hnswlib)
> 
> **Owner**
> **Author**
> `simonw` commented 
> Another option for an index could just be PyTorch with an in-memory collection of tensors.
> 
> I ran some benchmarks that looked good:
> 
> ![benchmark](https://user-images.githubusercontent.com/12345678/12345678/benchmark.png)
> 
> But when I tried a rough implementation like this it ended up slower than native Python (according to a `time llm similar ...` benchmark):
> 
> ```diff
> --git a/llm/embeddings.py b/llm/embeddings.py
> index 32d7dc8..54741ee 100644
> --- a/llm/embeddings.py
> +++ b/llm/embeddings.py
> @@ -9,6 +9,12 @@ from sqlite_utils.db import Table
>  import time
>  from typing import cast, Any, Dict, Iterable, List, Optional, Tuple, Union
>  
> +try:
> +    import torch
> +    import torch.nn.functional as F
> +except ImportError:
> +    torch = None
> +
>  
>  @dataclass
>  class Entry:
> @@ -242,6 +248,30 @@ class Collection:
>          """
>          import llm
>  
> +        if torch is not None:
> +            ids_and_embeddings = [
> +                (row["id"], torch.tensor(llm.decode(row["embedding"])))
> +                for row in self.db.query(
> +                    "select id, embedding from embeddings where collection_id = ?",
> +                    [self.id],
> +                )
> +            ]
> +            input_vector = torch.tensor(vector)
> +            scores = [
> +                (id, F.cosine_similarity(input_vector.unsqueeze(0), embedding.unsqueeze(0)))
> +                for id, embedding in ids_and_embeddings
> +            ]
> +            scores.sort(key=lambda id_and_score: id_and_score[1], reverse=True)
> +            return [
> +                Entry(
> +                    id=id,
> +                    score=score.item(),
> +                    content=None,
> +                    metadata=None,
> +                )
> +                for id, score in scores[:number]
> +            ]
> +
>          def distance_score(other_encoded):
>              other_vector = llm.decode(other_encoded)
>              return llm.cosine_similarity(other_vector, vector)
> ```
> 
> Maybe I did something wrong here though. Would be worth spending more time seeing if PyTorch against an in-memory array can speed things up.
> 
> `jeffchuber` commented 
> @simonw happy to help here
> 
> Here is how Chroma's roadmap aligns with your goals.
> 
> The internals of Chroma are set up to have pluggable indexes on top of collections - we haven't yet exposed this to end users. But will fairly soon. We also plan to have a "smart index" that does KNN brute force and then a cutover to ANN.
> Indexes over multiple collections - while I do understand the use case - we've chosen to not prioritize this as it adds a lot of DX complexity. We instead encourage users to eat the "read amplification" and query multiple collections/indexes and then cull/rerank themselves client side.
> You may also enjoy reading this chroma proposal where we have put a lot of thought into the pipelines to support index/collection creation and access - [chroma

<details><summary>Metadata</summary>

- Duration: 33410 ms
- Datetime: 2024-01-10T19:43:23.307329
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

