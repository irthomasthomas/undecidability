import os
import sys

from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)

# accept user_input passed to the script as a command line argument.
# user_input = sys.argv[1]
user_input = sys.argv[1]

stream = client.chat.completions.create(
  messages=[
    {
      "role": "user",
      "content": f"{user_input}"
    }
  ],
  model="mixtral-8x7b-32768",
  stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
