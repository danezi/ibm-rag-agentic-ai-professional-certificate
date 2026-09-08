# Course 1 — Develop Generative AI Applications: Get Started

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Specialization](../README.md)
**Status:** 🟡 In progress (~43%)

## Learning goals

- Understand what generative AI is and where LLMs fit into an application stack
- Work with foundation models through APIs and SDKs (prompts, parameters, responses)
- Apply prompt engineering patterns — zero-/one-/few-shot, chain-of-thought, self-consistency — for reliable output
- Structure prompts with LangChain `PromptTemplate` and reuse them across use cases
- Build a first end-to-end generative AI application

## Labs

### Lab 1 — Master Prompt Engineering and LangChain PromptTemplates

- **Task:** Explore prompt engineering end to end against an IBM Granite model on watsonx.ai: start from basic prompts, work through advanced in-context learning techniques, then use LangChain prompt templates to apply prompting to real use cases (summarization, QA, classification, code generation, role play). Includes 5 exercises.
- **Approach:**
  - `ibm/granite-4-h-small` via `langchain-ibm`'s `WatsonxLLM`, wrapped in a reusable `llm_model(prompt, params)` helper with `default_params` (`max_new_tokens`, `min_new_tokens`, `temperature`, `top_p`, `top_k`).
  - Compared prompt styles on the same tasks: **zero-shot** vs **one-shot** vs **few-shot**, then **chain-of-thought** for multi-step reasoning and **self-consistency** (sampling several reasoning paths and taking the majority answer).
  - Moved hard-coded prompts into `PromptTemplate` objects with input variables so one template serves many inputs; chained template → LLM.
- **Code:** [`labs/In-Context Learning and Prompt Templates for Advanced AI.ipynb`](./labs/In-Context%20Learning%20and%20Prompt%20Templates%20for%20Advanced%20AI.ipynb)
- **Key learning:** Prompt structure is a bigger lever on output quality than parameter tuning. Few-shot examples fix format and tone; chain-of-thought plus self-consistency noticeably improves reasoning tasks; `PromptTemplate` turns one-off prompts into reusable, testable components.

### Lab 2 — [Lab title]

- **Task:** [...]
- **Approach:** [...]
- **Code:** [`labs/[notebook-or-script-name]`](./labs/[notebook-or-script-name])
- **Key learning:** [...]

## Key takeaways

- Decoding parameters: lower `temperature` / `top_p` / `top_k` for deterministic, factual tasks; raise them for variety (e.g. self-consistency, brainstorming).
- In-context learning progression: zero-shot → one-shot → few-shot trades prompt length for reliability; add examples only until the format stabilizes.
- Chain-of-thought makes the model show intermediate steps; self-consistency aggregates multiple CoT samples to reduce single-path errors.
- LangChain `PromptTemplate` separates prompt wording from the data filled into it — the basis for chains and, later, RAG and agents.
- The same small set of prompting patterns covers summarization, QA, classification, code generation and role play.

## Tools & libraries

- Python, Jupyter Notebook
- IBM watsonx.ai — `ibm-watsonx-ai`, model `ibm/granite-4-h-small`
- LangChain — `langchain`, `langchain-core`
- `langchain-ibm` — `WatsonxLLM` integration
