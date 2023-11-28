import os
from pathlib import Path
import openai

client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get('OPENAI_API_KEY'),
)

assistant = client.beta.assistants.create(
    name = "Test",
    model="gpt-3.5-turbo-1106",
)

print(assistant.id)