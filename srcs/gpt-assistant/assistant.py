import openai
import os
from pathlib import Path

client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get('OPENAI_API_KEY'),
)

# upload = client.files.create(
#     file=Path("Normas_debate.pdf"),
#     purpose="assistants",
# )

# file_id = list(upload.id)

assistant = client.beta.assistants.create(
    # file_ids=file_id,
    # question="Que hay en el texto qu te he enviado ?",
    model="gpt-3.5-turbo-1106",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is the capital of Morocco ?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Answer as a local guide"
)

# thread_messages = client.beta.threads.messages.list(thread.id)
# print(thread_messages.data)
runs = client.beta.threads.runs.list(
  thread.id
)

# for run in runs:
#     while run.completed_at is None:
#         # Process the run object or break the loop
#         continue

print(runs)

# files = client.beta.assistants.files.create(
#     assistant.id, upload.id
# )


# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Who is Mehdi Bennis ?",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )

# print(chat_completion.choices[0].message.content)


