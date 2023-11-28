import os
from pathlib import Path
import openai

client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get('OPENAI_API_KEY'),
)

thread = client.beta.threads.create()

print(thread.id)