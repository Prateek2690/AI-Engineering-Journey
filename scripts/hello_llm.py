"""Send one prompt to an LLM through OpenRouter and print the reply.

Usage:
  python scripts/hello_llm.py "your prompt"
  python scripts/hello_llm.py --model <openrouter-model-id> "your prompt"

Model ids are listed at https://openrouter.ai/models (for example an "anthropic/..."
id for Claude or a "meta-llama/..." id for Llama). The key is read from
OPENROUTER_API_KEY if set, otherwise asked for with hidden input and kept in
memory for this run only.
"""
import argparse

from llm_client import DEFAULT_MODEL, ask

parser = argparse.ArgumentParser()
parser.add_argument("prompt", nargs="*", default=["In two sentences, what is attention in a transformer?"])
parser.add_argument("--model", default=DEFAULT_MODEL, help="OpenRouter model id")
args = parser.parse_args()

print(ask(" ".join(args.prompt), model=args.model))
