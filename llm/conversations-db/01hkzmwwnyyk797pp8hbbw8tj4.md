**Prompt:**
Can you create a synthesis of these two scripts to create a complete finished cli tool with a sensible click ui design. It should be sensibly compartmentalised. Pay attention to unfamiliar terms and do not rewrite any of the api details like model name. IMPORTANT: I am without arms, so you will have to type the complete solution for me. Do not leave anything incomplete. Do a greate job and I will tip you 20 dollars, do you understand?
Also include a simple test to run each of the examples.

# SCRIPT_ONE
import logging
import os
import sys
import io
import base64
from PIL import Image
from openai import OpenAI

devtty = "/dev/tty"
if os.path.exists(devtty):
    logging.basicConfig(filename=devtty, level=logging.DEBUG)


def openai_completion(prompt, system_prompt, oai_client, max_tokens=2000, model='gpt-4-vision-preview', base64_image=None):
    # Requesting description from OpenAI
    client = oai_client
    print(f"Prompt: {prompt}")
    print(f"System prompt: {system_prompt}")   
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            },
        ],
        max_tokens=max_tokens,
    )
    result = response.choices[0].message.content
    return result


def read_image(image_path):
    """Reads an image from a file path or stdin if path is None."""
    if not image_path:
        if sys.stdin.isatty():
            error_message = "No image provided. You must provide an image path or pipe in an image."
            logging.error(error_message)
        try:
            image = Image.open(sys.stdin.buffer)
            return image
        except Exception as e:
            logging.error(f"Error reading image from stdin: {e}")
            sys.exit(1)
    else:
        try:
            image = Image.open(image_path)
            return image
        except Exception as e:
            logging.error(f"Error opening image '{image_path}': {e}")
            sys.exit(1)


def generate_description(image, prompt):
    """Uses an AI model to generate a description of the image and returns it."""
    client = OpenAI()  # This should be configured with proper authentication for OpenAI's services    
    # Convert image to base64 format
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    system_prompt = "You are GPT-4-Vision. Describe the image."
    try:
        result = openai_completion(prompt, system_prompt, client, base64_image=base64_image, model="gpt-4-vision-preview")
        return result
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)


def generate_json(image, prompt):
    """Generates a JSON representation of the image."""
    system_prompt = "**IMPORTANT**: Only write output in valid JSON format. Say nothing else. Notes and comments are not allowed, except in the form of valid JSON."
    print(f"Prompt: {prompt}")
    client = OpenAI()
    base64_image = convert_image_to_base64(image)
    try:
        result = openai_completion(prompt, system_prompt, client, base64_image=base64_image, model="gpt-4-vision-preview")
        return result
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)


def generate_md(image, prompt):
    """Generates a Markdown representation of the image."""
    system_prompt = "Write a Markdown representation of the data in the image below. Say nothing else. Only reply in the form of valid Markdown."
    client = OpenAI()
    base64_image = convert_image_to_base64(image)
    try:
        result = openai_completion(prompt, client, base64_image=base64_image, model="gpt-4-vision-preview")
        return result
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)


def convert_image_to_base64(image):
    """Converts a PIL image into a base64-encoded string."""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def main(image_path=None, prompt=None, output='describe'):
    image = read_image(image_path)
    
    if output == 'describe':
        description = generate_description(image, prompt)
        print(description)
    elif output == 'json':
        json_output = generate_json(image, prompt)
        print(json_output)
    elif output == 'md':
        md_output = generate_md(image, prompt)
        print(md_output)
    else:
        print(f"Unsupported output type: {output}")


# Sample usage
if __name__ == '__main__':
    # You would dynamically determine these paths depending on your use case
    code_image = "/home/thomas/Pictures/Screenshot_20240112_155417-copilot-helping-me-namestorm.png"
    key_data = "/home/thomas/Pictures/Screenshot_20240111_121310.png"
    photo = "/run/media/thomas/828ca7e5-381d-4149-8fc5-6d6aa26b90f2/101MEDIA/2023_09_25__12_22_54.png"
    # example_prompt = "Return the JSON representation of the keyboard shortcuts for the image below."
    example_prompt = "Rewrite a sample of this into a markdown document."
    # You can change the output to 'json' or 'md' to get different representations
    main(image_path=key_data, prompt=example_prompt, output='json')

# END_SCRIPT_ONE

# SCRIPT_TWO
import click
import logging
import os
import sys
from PIL import Image
from openai import OpenAI


@click.group()
def cli():
    pass

# Todo: Add a way for the user to include prompt text with the image.
@cli.command()
@click.argument('image_path', type=click.Path(exists=True), required=False)
@click.argument('prompt', required=False)

def describe(image_path, prompt=None):
    '''Describes the content of an image.'''

    # If no image path is provided, try to read the image from stdin
    if not image_path:
        if sys.stdin.isatty():
            raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
        image = Image.open(sys.stdin.buffer)
    else:
        # Open the image from the provided path
        image = Image.open(image_path)
    
    description = get_image_description(image, prompt)
    click.echo(description)

def get_image_description(image, prompt=None):
    # Replace 'OpenAI' instantiation and 'create_completion' as appropriate for your SDK
    client = OpenAI()

    # Convert image to base64 for sending to the API
    import io
    import base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    try:
        # Requesting description from OpenAI (Replace with the proper API call)
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt or "Describe this image in fine detail. Pay special attention to new or unfamilliar terms and nomenclature. They may be extremely important in delineating what is interesting about the content.",
                        }
                    ],
                },
            ],
            max_tokens=2000,
        )
        result = response.choices[0].message.content
        print(f"{result}")
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)

if __name__ == '__main__':
    cli()
# END_SCRIPT_TWO

**Response:**
Below is the combined script of SCRIPT_ONE and SCRIPT_TWO, incorporating a click UI design.

```python
import click
import logging
import os
import sys
import io
import base64
from PIL import Image
from openai import OpenAI

devtty = "/dev/tty"
if os.path.exists(devtty):
    logging.basicConfig(filename=devtty, level=logging.DEBUG)

# Client instantiation, moved from individual functions to reduce duplication
client = OpenAI()

def openai_completion(prompt, system_prompt, max_tokens=2000, model='gpt-4-vision-preview', base64_image=None):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            },
        ],
        max_tokens=max_tokens,
    )
    result = response.choices[0].message.content
    return result

def convert_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def generate_output(image, prompt, output_type):
    base64_image = convert_image_to_base64(image)
    system_prompts = {
        'describe': "You are GPT-4-Vision. Describe the image.",
        'json': "**IMPORTANT**: Only write output in valid JSON format. Say nothing else. Notes and comments are not allowed, except in the form of valid JSON.",
        'md': "Write a Markdown representation of the data in the image below. Say nothing else. Only reply in the form of valid Markdown."
    }
    system_prompt = system_prompts[output_type]
    try:
        result = openai_completion(prompt, system_prompt, base64_image=base64_image, model="gpt-4-vision-preview")
        return result
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('image_path', type=click.Path(exists=True), required=False)
@click.argument('prompt', required=False)
@click.option('--output', type=click.Choice(['describe', 'json', 'md'], case_sensitive=False), default='describe')
def process(image_path, prompt, output):
    if not image_path:
        if sys.stdin.isatty():
            raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
        try:
            image = Image.open(sys.stdin.buffer)
        except Exception as e:
            logging.error(f"Error reading image from stdin: {e}")
            sys.exit(1)
    else:
        try:
            image = Image.open(image_path)
        except Exception as e:
            logging.error(f"Error opening image '{image_path}': {e}")
            sys.exit(1)
    
    result = generate_output(image, prompt, output)
    click.echo(result)

if __name__ == '__main__':
    cli()
```

To test each of the outputs, you can run the following commands where `sample.png` is a placeholder for an image and `sample_prompt` is a placeholder prompt text:

```shell
# Test describe
python script.py process sample.png 'sample_prompt' --output describe
# Test json
python script.py process sample.png 'sample_prompt' --output json
# Test markdown
python script.py process sample.png 'sample_prompt' --output md
```

Note: Replace `script.py` with the actual name you give to the combined script.

<details><summary>Metadata</summary>

- Duration: 42626 ms
- Datetime: 2024-01-12T20:12:17.850786
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

