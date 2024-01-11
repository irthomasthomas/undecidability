import click
import logging
import os
import sys
from PIL import Image
from openai import OpenAI

# Assuming that OpenAI's GPT has a function named 'create_completion'
# and API instantiation requires an API key.
# Replace it with the correct function calls based on the actual library you're using.

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
        return response.choices[0] if response.choices else "No description found."
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)

if __name__ == '__main__':
    cli()