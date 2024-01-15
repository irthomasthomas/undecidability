**Prompt:**
diff --git a/agents/vision/GPT4-vision-toolkit.py b/agents/vision/GPT4-vision-toolkit.py
new file mode 100644
index 0000000..04be120
--- /dev/null
+++ b/agents/vision/GPT4-vision-toolkit.py
@@ -0,0 +1,90 @@
+import click
+import logging
+import os
+import sys
+import io
+import base64
+from PIL import Image
+from openai import OpenAI
+
+devtty = "/dev/tty"
+if os.path.exists(devtty):
+    logging.basicConfig(filename=devtty, level=logging.DEBUG)
+
+# Client instantiation, moved from individual functions to reduce duplication
+client = OpenAI()
+
+def openai_completion(prompt, system_prompt, max_tokens=2000, model='gpt-4-vision-preview', base64_image=None):
+    response = client.chat.completions.create(
+        model=model,
+        messages=[
+            {
+                "role": "user",
+                "content": [
+                    {
+                        "type": "text",
+                        "text": prompt,
+                    },
+                    {
+                        "type": "image_url",
+                        "image_url": {
+                            "url": f"data:image/png;base64,{base64_image}"
+                        },
+                    },
+                ],
+            },
+        ],
+        max_tokens=max_tokens,
+    )
+    result = response.choices[0].message.content
+    return result
+
+def convert_image_to_base64(image):
+    buffered = io.BytesIO()
+    image.save(buffered, format="PNG")
+    return base64.b64encode(buffered.getvalue()).decode('utf-8')
+
+def generate_output(image, prompt, output_type):
+    base64_image = convert_image_to_base64(image)
+    system_prompts = {
+        'describe': "You are GPT-4-Vision. Describe the image.",
+        'json': "**IMPORTANT**: Only write output in valid JSON format. Say nothing else. Notes and comments are not allowed, except in the form of valid JSON.",
+        'md': "Write a Markdown representation of the data in the image below. Say nothing else. Only reply in the form of valid Markdown."
+    }
+    system_prompt = system_prompts[output_type]
+    try:
+        result = openai_completion(prompt, system_prompt, base64_image=base64_image, model="gpt-4-vision-preview")
+        return result
+    except Exception as e:
+        logging.error(e)
+        return "Error: " + str(e)
+
+@click.group()
+def cli():
+    pass
+
+@cli.command()
+@click.argument('image_path', type=click.Path(exists=True), required=False)
+@click.argument('prompt', required=False)
+@click.option('--output', type=click.Choice(['text', 'json', 'md'], case_sensitive=False), default='describe')
+def describe(image_path, prompt, output):
+    if not image_path:
+        if sys.stdin.isatty():
+            raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
+        try:
+            image = Image.open(sys.stdin.buffer)
+        except Exception as e:
+            logging.error(f"Error reading image from stdin: {e}")
+            sys.exit(1)
+    else:
+        try:
+            image = Image.open(image_path)
+        except Exception as e:
+            logging.error(f"Error opening image '{image_path}': {e}")
+            sys.exit(1)
+    
+    result = generate_output(image, prompt, output)
+    click.echo(result)
+
+if __name__ == '__main__':
+    cli()
\ No newline at end of file
diff --git a/agents/vision/gpt4-vision-describe-image.py b/agents/vision/gpt4-vision-describe-image.py
deleted file mode 100644
index 631a933..0000000
--- a/agents/vision/gpt4-vision-describe-image.py
+++ /dev/null
@@ -1,77 +0,0 @@
-import click
-import logging
-import os
-import sys
-from PIL import Image
-from openai import OpenAI
-
-# Assuming that OpenAI's GPT has a function named 'create_completion'
-# and API instantiation requires an API key.
-# Replace it with the correct function calls based on the actual library you're using.
-
-@click.group()
-def cli():
-    pass
-
-# Todo: Add a way for the user to include prompt text with the image.
-@cli.command()
-@click.argument('image_path', type=click.Path(exists=True), required=False)
-@click.argument('prompt', required=False)
-
-def describe(image_path, prompt=None):
-    '''Describes the content of an image.'''
-
-    # If no image path is provided, try to read the image from stdin
-    if not image_path:
-        if sys.stdin.isatty():
-            raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
-        image = Image.open(sys.stdin.buffer)
-    else:
-        # Open the image from the provided path
-        image = Image.open(image_path)
-    
-    description = get_image_description(image, prompt)
-    click.echo(description)
-
-def get_image_description(image, prompt=None):
-    # Replace 'OpenAI' instantiation and 'create_completion' as appropriate for your SDK
-    client = OpenAI()
-
-    # Convert image to base64 for sending to the API
-    import io
-    import base64
-    buffered = io.BytesIO()
-    image.save(buffered, format="PNG")
-    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
-    
-    try:
-        # Requesting description from OpenAI (Replace with the proper API call)
-        response = client.chat.completions.create(
-            model="gpt-4-vision-preview",
-            messages=[
-                {
-                    "role": "user",
-                    "content": [
-                        {
-                            "type": "image_url",
-                            "image_url": {
-                                "url": f"data:image/png;base64,{base64_image}"
-                            },
-                        },
-                        {
-                            "type": "text",
-                            "text": prompt or "Describe this image in fine detail. Pay special attention to new or unfamilliar terms and nomenclature. They may be extremely important in delineating what is interesting about the content.",
-                        }
-                    ],
-                },
-            ],
-            max_tokens=2000,
-        )
-        result = response.choices[0].message.content
-        print(f"{result}")
-    except Exception as e:
-        logging.error(e)
-        return "Error: " + str(e)
-
-if __name__ == '__main__':
-    cli()
\ No newline at end of file
diff --git a/agents/vision/tests/Screenshot_20240109_183314-hf-benchmarks-ai-explanation.png b/agents/vision/tests/Screenshot_20240109_183314-hf-benchmarks-ai-explanation.png
new file mode 100644
index 0000000..d99da9e
Binary files /dev/null and b/agents/vision/tests/Screenshot_20240109_183314-hf-benchmarks-ai-explanation.png differ
diff --git a/agents/vision/tests/gh_homepage.png b/agents/vision/tests/gh_homepage.png
new file mode 100644
index 0000000..d4190d8
Binary files /dev/null and b/agents/vision/tests/gh_homepage.png differ
diff --git a/agents/vision/tests/krita-stable-diffusion-woman-smoking.png b/agents/vision/tests/krita-stable-diffusion-woman-smoking.png
new file mode 100644
index 0000000..eb656b6
Binary files /dev/null and b/agents/vision/tests/krita-stable-diffusion-woman-smoking.png differ
diff --git a/agents/vision/tests/terminator_keyboard_shortcuts.png b/agents/vision/tests/terminator_keyboard_shortcuts.png
new file mode 100644
index 0000000..e29dd57
Binary files /dev/null and b/agents/vision/tests/terminator_keyboard_shortcuts.png differ
diff --git a/agents/vision/tests/terminator_keyboard_shortcuts_2.png b/agents/vision/tests/terminator_keyboard_shortcuts_2.png
new file mode 100644
index 0000000..bfe27c6
Binary files /dev/null and b/agents/vision/tests/terminator_keyboard_shortcuts_2.png differ


**Response:**
Add GPT4-vision-toolkit.py and remove gpt4-vision-describe-image.py

<details><summary>Metadata</summary>

- Duration: 639 ms
- Datetime: 2024-01-12T21:06:52.604268
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

