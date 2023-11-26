import openai
import os

print("OpenAI library version:", openai.__version__)

client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get('OPENAI_API_KEY'),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who is Mehdi Bennis ?",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)

