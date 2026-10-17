"""Send one prompt to Claude and print the reply.

Usage: python scripts/hello_llm.py "your prompt"
Needs ANTHROPIC_API_KEY set as an environment variable or Codespaces/Colab secret.
"""
import sys

import anthropic

prompt = " ".join(sys.argv[1:]) or "In two sentences, what is attention in a transformer?"

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}],
)

if response.stop_reason == "refusal":
    print("The model declined this request.")
else:
    print("".join(block.text for block in response.content if block.type == "text"))
    print(f"\n[{response.usage.input_tokens} input / {response.usage.output_tokens} output tokens]")
