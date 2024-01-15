**Prompt:**
Is there a way to do this without the torch dependency while keeping cuda support?

import llm
from transformers import AutoModel

MAX_LENGTH = 8192


@llm.hookimpl
def register_embedding_models(register):
    for model_id in (
        "jina-embeddings-v2-small-en",
        "jina-embeddings-v2-base-en",
        "jina-embeddings-v2-large-en",
    ):
        register(JinaEmbeddingModel(model_id))


class JinaEmbeddingModel(llm.EmbeddingModel):
    def __init__(self, model_id):
        self.model_id = model_id
        self._model = None

    def embed_batch_torch(self, texts): # Needs refactoring without torch
        import torch
        torch.cuda.empty_cache()
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        if self._model is None:
            self._model = AutoModel.from_pretrained(
                "jinaai/{}".format(self.model_id), trust_remote_code=True
            )
            self._model.to(device)
        results = self._model.encode([text[:MAX_LENGTH] for text in texts], device=device)
        return (list(map(float, result)) for result in results)

**Response:**
1. Import the required libraries and functions.
2. Define the model_id list of pretrained model specifications.
3. Use the `register_embedding_models` function to register the models with the tokenizer.
4. Prepare the input texts.
5. Initialize the tokenizer.
6. Apply the tokenizer to the input texts and obtain the features.
7. The features can be used for further analysis or storage.

NOTE: This code assumes that the required dependencies are already installed and that the pretrained JINA models are available in the given directories.



<details><summary>Metadata</summary>

- Duration: 6094 ms
- Datetime: 2024-01-10T20:14:26.777604
- Model: gorilla-7b-hf-v1

</details>

**Options:**
```json
{"temperature": 0.8}
```

