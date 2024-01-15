**Prompt:**
Write this pricing data into a structured file for ingestion by python:

Language models

Multiple models, each with different capabilities and price points. Prices are per 1,000 tokens. You can think of tokens as pieces of words, where 1,000 tokens is about 750 words. This paragraph is 35 tokens.
GPT-4 Turbo

With 128k context, fresher knowledge and the broadest set of capabilities, GPT-4 Turbo is more powerful than GPT-4 and offered at a lower price.
Learn about GPT-4 Turbo
Model	Input	Output
gpt-4-1106-preview	$0.01 / 1K tokens	$0.03 / 1K tokens
gpt-4-1106-vision-preview	$0.01 / 1K tokens	$0.03 / 1K tokens
Vision pricing calculator
px
by
px
=$0.00255
GPT-4
With broad general knowledge and domain expertise, GPT-4 can follow complex instructions in natural language and solve difficult problems with accuracy.
Learn about GPT-4
Model	Input	Output
gpt-4	$0.03 / 1K tokens	$0.06 / 1K tokens
gpt-4-32k	$0.06 / 1K tokens	$0.12 / 1K tokens
GPT-3.5 Turbo

GPT-3.5 Turbo models are capable and cost-effective.

gpt-3.5-turbo is the flagship model of this family, supports a 16K context window and is optimized for dialog.

gpt-3.5-turbo-instruct is an Instruct model and only supports a 4K context window.
Learn about GPT-3.5 Turbo
Model	Input	Output
gpt-3.5-turbo-1106	$0.0010 / 1K tokens	$0.0020 / 1K tokens
gpt-3.5-turbo-instruct	$0.0015 / 1K tokens	$0.0020 / 1K tokens
Assistants API

Assistants API and tools (retrieval, code interpreter) make it easy for developers to build AI assistants within their own applications. Each assistant incurs its own retrieval file storage fee based on the files passed to that assistant. The retrieval tool chunks and indexes your files content in our vector database.

Learn more

The tokens used for the Assistant API are billed at the chosen language model's per-token input / output rates and the assistant intelligently chooses which context from the thread to include when calling the model
Learn about Assistants API
Tool	Input
Code interpreter	$0.03 / session (free until 11/17/2023)
Retrieval	$0.20 / GB / assistant / day (free until 11/17/2023)


Fine-tuning models
Create your own custom models by fine-tuning our base models with your training data. Once you fine-tune a model, you’ll be billed only for the tokens you use in requests to that model.
Learn about fine-tuning
Model	Training	Input usage	Output usage
gpt-3.5-turbo	$0.0080 / 1K tokens	$0.0030 / 1K tokens	$0.0060 / 1K tokens
davinci-002	$0.0060 / 1K tokens	$0.0120 / 1K tokens	$0.0120 / 1K tokens
babbage-002	$0.0004 / 1K tokens	$0.0016 / 1K tokens	$0.0016 / 1K tokens
Embedding models
Build advanced search, clustering, topic modeling, and classification functionality with our embeddings offering.
Learn about embeddings
Model	Usage
ada v2	$0.0001 / 1K tokens
Base models
GPT base models are not optimized for instruction-following and are less capable, but they can be effective when fine-tuned for narrow tasks.
Learn about GPT base models
Model	Usage
davinci-002	$0.0020 / 1K tokens
babbage-002	$0.0004 / 1K tokens
Other models
Image models

Build DALL·E directly into your apps to generate and edit novel images and art. DALLE·E 3 is the highest quality model and DALL·E 2 is optimized for lower cost.
Learn about image generation
Model	Quality	Resolution	Price
DALL·E 3	Standard	1024×1024	$0.040 / image
	Standard	1024×1792, 1792×1024	$0.080 / image
DALL·E 3	HD	1024×1024	$0.080 / image
	HD	1024×1792, 1792×1024	$0.120 / image
DALL·E 2		1024×1024	$0.020 / image
		512×512	$0.018 / image
		256×256	$0.016 / image
Audio models

Whisper can transcribe speech into text and translate many languages into English.

Text-to-speech (TTS) can convert text into spoken audio.
Model	Usage
Whisper	$0.006 / minute (rounded to the nearest second)
TTS	$0.015 / 1K characters
TTS HD	$0.030 / 1K characters

Please note that our Usage Policies require you to provide a clear disclosure to end users that the TTS voice they are hearing is AI-generated and not a human voice.

**Response:**
To structure the provided pricing data for ingestion by a Python program, we can create a JSON file. JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.

Here is an example of how the data might be structured in a JSON file:

```json
{
  "language_models": {
    "GPT-4 Turbo": {
      "description": "With 128k context, fresher knowledge and the broadest set of capabilities, GPT-4 Turbo is more powerful than GPT-4 and offered at a lower price.",
      "models": [
        {
          "name": "gpt-4-1106-preview",
          "input_price": 0.01,
          "output_price": 0.03
        },
        {
          "name": "gpt-4-1106-vision-preview",
          "input_price": 0.01,
          "output_price": 0.03
        }
      ],
      "vision_pricing_calculator": {
        "price_per_pixel": 0.00255
      }
    },
    "GPT-4": {
      "description": "With broad general knowledge and domain expertise, GPT-4 can follow complex instructions in natural language and solve difficult problems with accuracy.",
      "models": [
        {
          "name": "gpt-4",
          "input_price": 0.03,
          "output_price": 0.06
        },
        {
          "name": "gpt-4-32k",
          "input_price": 0.06,
          "output_price": 0.12
        }
      ]
    },
    "GPT-3.5 Turbo": {
      "description": "GPT-3.5 Turbo models are capable and cost-effective.",
      "models": [
        {
          "name": "gpt-3.5-turbo-1106",
          "input_price": 0.0010,
          "output_price": 0.0020
        },
        {
          "name": "gpt-3.5-turbo-instruct",
          "input_price": 0.0015,
          "output_price": 0.0020
        }
      ]
    },
    "Assistants API": {
      "description": "Assistants API and tools make it easy for developers to build AI assistants within their own applications.",
      "tools": [
        {
          "name": "Code interpreter",
          "input_price": 0.03,
          "free_until": "2023-11-17"
        },
        {
          "name": "Retrieval",
          "price_per_gb_per_day": 0.20,
          "free_until": "2023-11-17"
        }
      ]
    },
    "Fine-tuning models": {
      "models": [
        {
          "name": "gpt-3.5-turbo",
          "training_price": 0.0080,
          "input_usage_price": 0.0030,
          "output_usage_price": 0.0060
        },
        {
          "name": "davinci-002",
          "training_price": 0.0060,
          "input_usage_price": 0.0120,
          "output_usage_price": 0.0120
        },
        {
          "name": "babbage-002",
          "training_price": 0.0004,
          "input_usage_price": 0.0016,
          "output_usage_price": 0.0016
        }
      ]
    },
    "Embedding models": {
      "models": [
        {
          "name": "ada v2",
          "usage_price": 0.0001
        }
      ]
    },
    "Base models": {
      "models": [
        {
          "name": "davinci-002",
          "usage_price": 0.0020
        },
        {
          "name": "babbage-002",
          "usage_price": 0.0004
        }
      ]
    }
  },
  "other_models": {
    "Image models": {
      "DALL·E 3": {
        "Standard": [
          {
            "resolution": "1024x1024",
            "price_per_image": 0.040
          },
          {
            "resolution": "1024x1792, 1792x1024",
            "price_per_image": 0.080
          }
        ],
        "HD": [
          {
            "resolution": "1024x1024",
            "price_per_image": 0.080
          },
          {
            "resolution": "1024x1792, 1792x1024",
            "price_per_image": 0.120
          }
        ]
      },
      "DALL·E 2": [
        {
          "resolution": "1024x1024",
          "price_per_image": 0.020
        },
        {
          "resolution": "512x512",
          "price_per_image": 0.018
        },
        {
          "resolution": "256x256",
          "price_per_image": 0.016
        }
      ]
    },
    "Audio models": {
      "Whisper": {
        "usage_price_per_minute": 0.006
      },
      "TTS": {
        "standard": {
          "usage_price_per_1k_characters": 0.015
        },
        "HD": {
          "usage_price_per_1k_characters": 0.030
        }
      }
    }
  }
}
```

This JSON file can then be read by a Python program using the `json` module. Here's an example of how you might load this data in Python:

```python
import json

# Load the JSON data from a file
with open('pricing_data.json', 'r') as file:
    pricing_data = json.load(file)

# Now you can access the pricing data as a Python dictionary
print(pricing_data)
```

Please note that the JSON structure above is just one way to organize the data. Depending on the specific requirements of the Python program that will ingest this data, you might need to adjust the structure accordingly.

<details><summary>Metadata</summary>

- Duration: 33362 ms
- Datetime: 2023-11-15T20:56:58.154622
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

