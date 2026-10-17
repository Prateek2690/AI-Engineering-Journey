"""Send one prompt to Claude and print the reply.

Usage: python scripts/hello_llm.py "your prompt"
Uses ANTHROPIC_API_KEY if it is set; otherwise asks for the key (hidden input)
and keeps it in memory for this run only, so it is never written to disk.
"""
import getpass
import os
import sys

import anthropic

prompt = " ".join(sys.argv[1:]) or "In two sentences, what is attention in a transformer?"

api_key = os.environ.get("ANTHROPIC_API_KEY") or getpass.getpass("Anthropic API key (hidden): ")
client = anthropic.Anthropic(api_key=api_key)
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
