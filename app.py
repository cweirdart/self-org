import gradio as gr
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load system prompt
with open("system_prompt.txt") as f:
    system_prompt = f.read()

# Load behavior contract
with open("behavior_contract.txt") as f:
    behavior_contract = f.read()

# Load governance design layer explicitly
with open("governance_design.txt") as f:
    governance_design = f.read()

# Explicitly combine all prompts
combined_prompt = f"{system_prompt}\n\n{behavior_contract}\n\n{governance_design}"

def chatbot_response(message, history):
    messages = [{"role": "system", "content": combined_prompt}]
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response.choices[0].message.content.strip()

iface = gr.ChatInterface(
    fn=chatbot_response,
    title="Systems Guide",
    retry_btn=None,
    undo_btn=None,
    clear_btn="Clear",
)

iface.launch(server_name="0.0.0.0", server_port=7860)
