# self-org

This repository contains a simple command-line chatbot interface.

## Requirements

- Python 3.8+
- An API key for OpenAI's chat completion API (or another compatible service).

## Setup

1. Install the `openai` package if it's not already installed:
   ```bash
   pip install openai
   ```
2. Export your API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```
3. (Optional) Edit `system_prompt.txt` to customize the system prompt sent to the model. A default prompt aligned with the philosophy at [self-org.org](https://self-org.org) is provided.
4. (Optional) Edit `behavior_contract.txt` to adjust the behavioral contract that will be prepended to the system prompt. Both files are loaded at runtime. If both files are missing, the script falls back to a helper prompt.

## Running the chatbot

Execute the script with Python:

```bash
python3 chatbot.py
```

Type your messages at the prompt. Enter `quit` or `exit` to stop the program.
