import gradio as gr
import openai
import os

# Load the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the system prompt from file
with open("system_prompt.txt") as f:
    system_prompt = f.read()

# Load behavior contract (optional, if you want to include it)
with open("behavior_contract.txt") as f:
    behavior_contract = f.read()

# Combine prompts if desired (customizable)
combined_prompt = f"{system_prompt}\n\n{behavior_contract}"

# Chatbot response logic
def chatbot_response(message, history):
    messages = [{"role": "system", "content": combined_prompt}]
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
    )

    return response.choices[0].message.content.strip()

# Create Gradio interface clearly
iface = gr.ChatInterface(
    fn=chatbot_response,
    title="Systems Guide",
    retry_btn=None,
    undo_btn=None,
    clear_btn="Clear",
)

# Launch Gradio clearly
iface.launch(server_name="0.0.0.0", server_port=7860)
