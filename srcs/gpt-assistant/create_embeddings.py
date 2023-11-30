from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

response = client.embeddings.create(
    input="""Example""",
    model="text-embedding-ada-002"
)

print(response.data[0].embedding)