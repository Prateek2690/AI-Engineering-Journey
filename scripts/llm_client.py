"""One small helper to call an LLM through Anthropic, OpenRouter or Together.

OpenRouter and Together speak the OpenAI-style API, so they share one code path
(the `openai` package pointed at a different base URL). Anthropic uses its own SDK.
API keys are read from the environment if set, otherwise asked for with hidden
input and kept in memory only.
"""
import getpass
import os

PROVIDERS = {
    # name: (env var for the key, base URL for OpenAI-style APIs, default model)
    "anthropic": ("ANTHROPIC_API_KEY", None, "claude-opus-5-5"),
    "openrouter": ("OPENROUTER_API_KEY", "https://openrouter.ai/api/v1", "meta-llama/llama-3.3-70b-instruct"),
    "together": ("TOGETHER_API_KEY", "https://api.together.xyz/v1", "meta-llama/Llama-3.3-70B-Instruct-Turbo"),
}


def _key(env_var: str) -> str:
    if not os.environ.get(env_var):
        os.environ[env_var] = getpass.getpass(f"{env_var} (hidden): ")
    return os.environ[env_var]


def ask(prompt: str, provider: str = "openrouter", model: str | None = None, max_tokens: int = 1024) -> str:
    """Send one user prompt and return the reply text."""
    env_var, base_url, default_model = PROVIDERS[provider]
    model = model or default_model

    if provider == "anthropic":
        import anthropic

        client = anthropic.Anthropic(api_key=_key(env_var))
        response = client.messages.create(
            model=model, max_tokens=max_tokens, messages=[{"role": "user", "content": prompt}]
        )
        if response.stop_reason == "refusal":
            return "[The model declined this request.]"
        return "".join(block.text for block in response.content if block.type == "text")

    from openai import OpenAI

    client = OpenAI(api_key=_key(env_var), base_url=base_url)
    response = client.chat.completions.create(
        model=model, max_tokens=max_tokens, messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content or ""
