import openai
import os
from pathlib import Path
import time
import utils

client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get('OPENAI_API_KEY'),
)

assistant_id = os.environ.get("ASSISTANT_ID")
thread_id = os.environ.get("THREAD_ID")

msg = ""

while msg != "exit":
  msg = input("Enter your prompt: ")
  instruction = input("Any specific instruction ?: ")
  run = utils.new_prompt(assistant_id, thread_id, msg, instruction)
  while run.status != "completed":
    run = client.beta.threads.runs.retrieve(
      thread_id=thread_id,
      run_id=run.id
    )
    time.sleep(1) 
  thread_messages = client.beta.threads.messages.list(thread_id, order="desc", limit=2)
  for i in thread_messages.data:
    if i.role == 'assistant':
      print(i.content[0].text, "\n")
