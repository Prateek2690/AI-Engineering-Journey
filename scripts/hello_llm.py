"""Send one prompt to an LLM and print the reply.

Usage:
  python scripts/hello_llm.py "your prompt"                      # OpenRouter, default model
  python scripts/hello_llm.py --provider together "your prompt"
  python scripts/hello_llm.py --provider anthropic --model claude-opus-5-5 "your prompt"

The key is read from the provider's environment variable if set, otherwise asked
for with hidden input and kept in memory for this run only.
"""
import argparse

from llm_client import PROVIDERS, ask

parser = argparse.ArgumentParser()
parser.add_argument("prompt", nargs="*", default=["In two sentences, what is attention in a transformer?"])
parser.add_argument("--provider", choices=PROVIDERS, default="openrouter")
parser.add_argument("--model", help="model id as the provider lists it; defaults per provider")
args = parser.parse_args()

print(ask(" ".join(args.prompt), provider=args.provider, model=args.model))
