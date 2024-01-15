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



<details><summary>Metadata</summary>

- Duration: 903 ms
- Datetime: 2024-01-10T20:14:07.185064
- Model: gorilla-7b-hf-v1

</details>

**Options:**
```json
{"temperature": 0.8}
```

