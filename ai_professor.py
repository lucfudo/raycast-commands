#!./.venv-raycast/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ai English Teacher
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🏴󠁧󠁢󠁥󠁮󠁧󠁿

# Documentation:
# @raycast.description English teacher
# @raycast.author Fudo

import sys
import pyperclip

try:
    from langchain_community.llms import Ollama
except ImportError as e:
    print("Failed to import the necessary module. Make sure 'langchain-community' is installed.")
    print(f"Error: {e}")
    sys.exit(1)

user_input = pyperclip.paste()
print(user_input)

ollama = Ollama(
    base_url='http://localhost:11434',
    model="llama3"
)

response = ollama.invoke([
  {
    'role': 'system',
    'content': 'Your role is to check that there are no spelling mistakes and that the sentence is written in good English. If there are no spelling mistakes, you simply say "Right!", otherwise you write the correct form of the sentence.',
  },
  {
    'role': 'user',
    'content': user_input,
  },
])

print(response)
