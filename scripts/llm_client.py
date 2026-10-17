"""One small helper to call any LLM through OpenRouter.

OpenRouter speaks the OpenAI-style API, so this uses the `openai` package pointed
at OpenRouter's base URL. One OpenRouter key reaches Claude, GPT, Gemini, Llama,
Qwen, DeepSeek and more; pick a model by its OpenRouter id (https://openrouter.ai/models).
The key is read from OPENROUTER_API_KEY if set, otherwise asked for with hidden
input and kept in memory only.
"""
import getpass
import os

from openai import OpenAI

BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "meta-llama/llama-3.3-70b-instruct"

_client = None


def client() -> OpenAI:
    global _client
    if _client is None:
        if not os.environ.get("OPENROUTER_API_KEY"):
            os.environ["OPENROUTER_API_KEY"] = getpass.getpass("OPENROUTER_API_KEY (hidden): ")
        _client = OpenAI(api_key=os.environ["OPENROUTER_API_KEY"], base_url=BASE_URL)
    return _client


def ask(prompt: str, model: str = DEFAULT_MODEL, max_tokens: int = 1024) -> str:
    """Send one user prompt and return the reply text."""
    response = client().chat.completions.create(
        model=model, max_tokens=max_tokens, messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content or ""
