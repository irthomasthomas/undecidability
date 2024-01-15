**Prompt:**
from openai import OpenAI

# gets OPENAI_API_KEY from your environment variables
openai = OpenAI()

prompt = "An astronaut lounging in a tropical resort in space, pixel art"
model = "dall-e-3"

def main() -> None:
    # Generate an image based on the prompt
    response = openai.images.generate(prompt=prompt, model=model)
    
    # Prints response containing a URL link to image
    print(response)
    
if __name__ == "__main__":
    main(){
    "language_models": {
        "GPT-4 Turbo": {
            "description": "With 128k context, fresher knowledge and the broadest set of capabilities, GPT-4 Turbo is more powerful than GPT-4 and offered at a lower price.",
            "models": [
                {
                    "name": "gpt-4-1106-preview",
                    "input_price": 0.01,
                    "output_price": 0.03,
                    "context_window": 128000,
                    "max_output_tokens": 4096,
                    "training_data_cutoff_isodate": "2023-04-01"
                },
                {
                    "name": "gpt-4-1106-vision-preview",
                    "input_price": 0.01,
                    "output_price": 0.03,
                    "context_window": 128000,
                    "max_output_tokens": 4096,
                    "training_data_cutoff_isodate": "2023-04-01"
                }
            ]
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
import click
import tiktoken
import json

# Load an encoding for tokenization
# Replace 'gpt-3.5-turbo' with the model you are using
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Function to load pricing data from a JSON file
def load_pricing_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        pricing = {}
        for category in data['language_models'].values():
            for model in category.get('models', []):
                pricing[model['name']] = {
                    'input': model.get('input_price', 0),
                    'output': model.get('output_price', 0)
                }
        for category, details in data['other_models'].items():
            for model_name, model_data in details.items():
                if isinstance(model_data, list):
                    for spec in model_data:
                        pricing[spec['resolution']] = {'image': spec['price_per_image']}
                elif isinstance(model_data, dict):
                    for sub_category, sub_specs in model_data.items():
                        if isinstance(sub_specs, list):
                            for spec in sub_specs:
                                pricing[spec['resolution']] = {'image': spec['price_per_image']}
                        else:
                            pricing[sub_category] = sub_specs
        return pricing

# Load pricing data from the JSON file
PRICING = load_pricing_data('/home/thomas/Development/Projects/llm/openai_cost_estimator/openai-api-prices.json')

def calculate_cost(model, content_length, operation='input'):
    """Calculate the cost based on model, content length, and operation type."""
    rate = PRICING.get(model, {}).get(operation)
    if rate is None:
        raise ValueError('Model or operation type not found in pricing data.')
    return rate * content_length / 1000  # Assuming rate is per 1K tokens

def calculate_token_count(content):
    """Calculate the number of tokens in the content using tiktoken."""
    token_count = len(encoding.encode(content))
    return token_count

@click.command()
@click.argument('content', default='', required=False)
@click.option('--model', prompt='Model name', help='The model/service endpoint.')
@click.option('--operation', default='input', help='Operation type (input/output).')
@click.option('--token-count', default=None, help='Token count (overrides content).', type=int)


def main(model, content, operation, token_count):
    """CLI tool to calculate the cost of using OpenAI API."""
    if token_count is None:
        token_count = calculate_token_count(content)
    cost = calculate_cost(model, token_count, operation)
    click.echo(f"Cost: ${cost:.6f} (USD) for {token_count} tokens.")


if __name__ == '__main__':
    main()import argparse
from PIL import Image


def calculate_cost_from_dimensions(width, height, detail_level):
    """
    Calculate the token cost based on the given dimensions and detail level.

    :param width: Width of the image
    :param height: Height of the image
    :param detail_level: 'high' or 'low'
    :return: Token cost
    """
    if detail_level == 'low':
        return 85  # Fixed cost for low detail images

    # For high detail images
    # Step 1: Scale to fit within a 2048 x 2048 square
    if width > 2048 or height > 2048:
        aspect_ratio = width / height
        if width > height:
            width = 2048
            height = int(width / aspect_ratio)
        else:
            height = 2048
            width = int(height * aspect_ratio)

    # Step 2: Scale such that the shortest side is 768px
    if width < height:
        scale_factor = 768 / width
    else:
        scale_factor = 768 / height
    width = int(width * scale_factor)
    height = int(height * scale_factor)

    # Step 3: Count 512px squares
    # squares_count = (width // 512) * (height // 512)
    squares_count = ((width + 511) // 512) * ((height + 511) // 512)

    # Step 4: Calculate cost
    return 170 * squares_count + 85


def calculate_token_cost(image_file=None, width=None, height=None, detail_level='low'):
    """
    Calculate the token cost based on an image file or given dimensions.

    :param image_file: Path to the image file (optional)
    :param width: Width of the image (optional)
    :param height: Height of the image (optional)
    :param detail_level: 'high' or 'low'
    :return: Token cost
    """
    if image_file:
        with Image.open(image_file) as img:
            width, height = img.size

    if width is not None and height is not None:
        return calculate_cost_from_dimensions(width, height, detail_level)

    raise ValueError("Either image_file or both width and height must be provided")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate token cost based on image dimensions.')
    parser.add_argument('--image', help='Path to the image file')
    parser.add_argument('--width', type=int, help='Width of the image')
    parser.add_argument('--height', type=int, help='Height of the image')
    parser.add_argument('--detail-level', choices=['low', 'high'], default='high', help='Detail level (low or high)')

    args = parser.parse_args()

    try:
        token_cost = calculate_token_cost(image_file=args.image, width=args.width, height=args.height, detail_level=args.detail_level)
        print(token_cost)
    except ValueError as e:
        print(f'Error: {str(e)}')

**Response:**
# OpenAI API Cost Estimator

This project contains Python scripts to estimate the cost of using the OpenAI API based on various models and operations.

## Usage

### Calculate Cost Based on Text Input

```
python calculate_cost.py --model <model_name> --content <text_input> --operation <input/output>
```

- `model`: The name of the model or service endpoint.
- `content`: The input text.
- `operation`: The type of operation (input or output).

This script uses the OpenAI pricing information to calculate the approximate cost of using the OpenAI API based on the number of tokens in the input text.

### Calculate Cost Based on Image Dimensions

```
python calculate_cost.py --image <image_file> --detail-level <low/high>
```

- `image`: The path to the image file.
- `detail-level`: The level of detail of the image (low or high).

This script calculates the token cost based on the dimensions of the image.

## Pricing Data

The script uses pricing data loaded from a JSON file (`openai-api-prices.json`) to estimate the cost. The pricing data includes the prices per token for different models and operations, as well as the prices per image for different resolutions and detail levels.

## TODO

- [ ] Implement support for more models and services offered by the OpenAI API.
- [ ] Add command-line options to specify the path to the pricing data JSON file.
- [ ] Enhance the error handling and user input validation.
- [ ] Improve the formatting and output of the cost estimation results.
- [ ] Add example usages and instructions in the readme file.

<details><summary>Metadata</summary>

- Duration: 6897 ms
- Datetime: 2024-01-10T17:19:42.024062
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

