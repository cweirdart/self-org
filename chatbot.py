import os
import openai

PROMPT_FILE = 'system_prompt.txt'
CONTRACT_FILE = 'behavior_contract.txt'


def load_prompt(path: str) -> str:
    """Load text from a file, returning an empty string if not found."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def main() -> None:
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print('Error: OPENAI_API_KEY environment variable not set.')
        return

    openai.api_key = api_key
    prompt = load_prompt(PROMPT_FILE)
    contract = load_prompt(CONTRACT_FILE)
    system_message = f"{contract}\n\n{prompt}" if contract or prompt else "You are a helpful assistant."

    print("Type 'quit' or 'exit' to stop.")
    while True:
        try:
            user_input = input('You: ')
        except EOFError:
            break
        if user_input.strip().lower() in {'quit', 'exit'}:
            break
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_input},
                ],
            )
            message = response.choices[0].message["content"].strip()
            print(f'Bot: {message}')
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()
