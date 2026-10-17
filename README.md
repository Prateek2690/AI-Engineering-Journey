# AI Engineering Journey

Building LLM, agent and RL skills from first principles, applied to quantitative finance. This repo holds the notebooks, exercises and notes from an 8-month plan (November 2026 to June 2027, about 15 hours a week). Each phase ends with a shipped project in its own repository.

## The plan

| Phase | Dates | Learn | Ships |
| --- | --- | --- | --- |
| 1. Foundations | Nov 2026 | Backprop, transformers from scratch, tokenization, LLM APIs, tool calling | A small GPT trained from scratch |
| 2. Agents and RAG | Dec 2026 – Jan 2027 | LangGraph, MCP, A2A, hybrid retrieval, vector databases | [finagent-research](#projects): multi-agent equity research analyst |
| 3. Evals and governance | Feb – Mar 2027 | Golden datasets, LLM-as-judge, red-teaming, observability, AI model risk | [llm-model-risk-kit](#projects): eval and model-risk toolkit |
| 4. Post-training and inference | Apr – May 2027 | SFT, LoRA, DPO, GRPO with verifiable rewards, vLLM, quantization | [finreason-rl](#projects): RL fine-tuning for financial reasoning |
| 5. Capstone | Jun 2027 | ML system design, cost and latency trade-offs | Production rebuild of Project 1 and a paper |

## Repository layout

```
phase-1-foundations/     micrograd, makemore, GPT from scratch, LLM API exercises
phase-2-agents-rag/      LangGraph and MCP exercises, retrieval experiments
phase-3-evals-governance/ eval methods, red-teaming, model-risk notes
phase-4-post-training/   fine-tuning, DPO and GRPO experiments
phase-5-capstone/        system design write-ups
notebooks/               setup checks and scratch notebooks
scripts/                 small runnable scripts
notes/                   learning log entries
```

## How to run it

Nothing needs to be installed locally.

- **GPU notebooks (Google Colab or Kaggle):** in Colab choose File › Open notebook › GitHub, paste this repo's URL, then Runtime › Change runtime type › GPU. Start with `notebooks/00_environment_check.ipynb`.
- **App code and scripts (GitHub Codespaces):** Code › Codespaces › Create codespace on main. The dev container installs everything in `requirements.txt` (CPU PyTorch included). Stop the codespace when you finish to save free hours.
- **API keys:** add `ANTHROPIC_API_KEY` (and `OPENAI_API_KEY` if you use it) as Codespaces secrets (Settings › Codespaces › Secrets) and as Colab secrets (the key icon in the left bar). Never commit keys; `.env` is git-ignored.

Quick check in a codespace:

```bash
python scripts/hello_llm.py "Explain the KV cache in two sentences."
```

## Projects

Each project lives in its own repository once it starts:

- **finagent-research**: planner, retriever, quant and critic agents read SEC filings through MCP servers and write cited research notes.
- **llm-model-risk-kit**: golden datasets, LLM-as-judge, red-teaming, drift monitoring and SR 11-7 style validation reports.
- **finreason-rl**: teaching small open LLMs financial reasoning with SFT, DPO and GRPO on code-verifiable rewards.

## Learning log

Short entries on what I built and what broke go in [`notes/`](notes/).
