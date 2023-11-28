import os
import openai

def new_prompt(assistant_id, thread_id, msg, instruction=None):
    client = openai.OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=os.environ.get('OPENAI_API_KEY'),
    )
    message =  client.beta.threads.messages.create(
        thread_id = thread_id,
        role = "user",
        content = msg
    )
    run = client.beta.threads.runs.create(
        thread_id = thread_id,
        assistant_id = assistant_id,
        instructions = instruction
    )
    return run
