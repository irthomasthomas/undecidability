**Prompt:**
load a peft 

**Response:**

import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


def load_model():
    model_name = "kochetkov-doc2vec-SST-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model
    

def process_data(tokenizer, model, text):
    doc_vectors = model.encode(text)
    # Get the similarity between the query and the docs in the training set
    doc_queries = pd.DataFrame(np.random.randn(len(doc_vectors), 1), columns=['query_' + str(col) for col in range(len(doc_vectors))])
    doc_queries['query_0'] = doc_queries['query_1'] = doc_queries['query_2'] = ... = doc_queries['query_{}'.format(len(doc_queries)/2)] = np.zeros(doc_vectors.shape[1])
    doc_queries['query_{}'.format(i)] = doc_vectors[:, i].T for i in range(1, len(doc_queries)/1)
    doc_queries = doc_queries.applymap(str)
    # Calculate the similarity scores between the query and the docs
    similarities = np.inner(doc_queries.values, doc_vectors.T)
    # Get the top 5 docuements with highest similarity scores
    indices = np.argsort(similarities)[::-1][5]
    doc_vectors = doc_vectors[indices, :]
    doc_queries = doc_queries[indices]
    # Return the docuements and their respective scores
    response = [tokenizer.encode(query) for query, score in zip(doc_queries, indices)]
    return response


# Load the model and tokenizer
tokenizer, model = load_model()
# Process the data
response = process_data(tokenizer, model, "What are

<details><summary>Metadata</summary>

- Duration: 22474 ms
- Datetime: 2024-01-10T19:31:00.901265
- Model: gorilla-7b-hf-v1

</details>

**Options:**
```json
{"temperature": 1.0}
```

