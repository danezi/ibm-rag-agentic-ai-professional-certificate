# Course 2 — Build RAG Applications: Get Started

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Specialization](../README.md)
**Status:** 🟢 Done

## Learning goals

- Explain the RAG pattern and why it beats fine-tuning for knowledge-grounded apps
- Load, split, and embed documents into a retrievable index
- Wire retrieval into a prompt so the LLM answers from provided context
- Build and run a minimal RAG pipeline end to end

## Labs

### Final Project — LinkedIn Icebreaker Bot

- **Task:** Build an end-to-end RAG application — not a notebook exercise, a small real
  program with two front ends (CLI + Gradio web UI) — that pulls one person's LinkedIn
  profile, indexes it, and answers questions grounded only in that profile's data,
  including an opening "here are 3 interesting facts about this person" icebreaker.
- **Approach:**
  - **Extraction:** [ProxyCurl](https://nubela.co/proxycurl/) API for a real profile, or
    a pre-made mock JSON profile (`--mock`) so the app runs without an API key.
  - **Indexing (LlamaIndex, not LangChain):** raw profile JSON → single `Document` →
    `SentenceSplitter` chunks → `VectorStoreIndex` embedded with `WatsonxEmbeddings`
    (`ibm/granite-embedding-278m-multilingual`).
  - **Querying:** `WatsonxLLM` (`ibm/granite-4-h-small`) wrapped in a LlamaIndex query
    engine with two custom `PromptTemplate`s — one for the initial "3 facts", one for
    free-form Q&A — both instructed to answer only from the retrieved context
    (`similarity_top_k` chunks) and say "I don't know" otherwise.
  - **Front ends:** a CLI (`main.py`, prints facts then opens a chat loop) and a Gradio
    web app (`app.py`, session-scoped by UUID so multiple profiles don't mix indexes).
- **Code:** [`labs/icebreaker/`](./labs/icebreaker/) — [screenshots](./labs/icebreaker/screenshot-1.png)
- **Key learning:** LlamaIndex is a second, RAG-focused alternative to LangChain's
  document/retriever stack — same underlying idea (load → split → embed → index →
  retrieve → prompt), but `VectorStoreIndex` + `as_query_engine()` collapse most of that
  pipeline into two calls. Constraining both prompt templates to answer only from
  retrieved context (and admit "I don't know") is what keeps a RAG bot from quietly
  hallucinating facts about a real person.

## Key takeaways

- RAG's value proposition over fine-tuning: ground answers in retrieved, current,
  person-/document-specific data instead of baking facts into model weights.
- LlamaIndex's high-level API (`VectorStoreIndex`, `as_query_engine()`,
  `as_retriever()`) trades some of LangChain's explicit wiring for fewer moving parts —
  useful to know both, since real projects use whichever fits the task.
- A RAG prompt template should explicitly instruct the model to answer only from the
  provided context and say so when it can't — otherwise retrieval augmentation doesn't
  actually stop the model from guessing.
- Mock-data fallbacks (a fixed sample JSON instead of a live API call) make a RAG app
  runnable and testable without paid API keys or live network dependencies.

## Tools & libraries

- Python, Gradio (web UI)
- IBM watsonx.ai — `ibm-watsonx-ai`; models `ibm/granite-4-h-small` (LLM),
  `ibm/granite-embedding-278m-multilingual` (embeddings)
- LlamaIndex — `llama-index-core`, `llama-index-llms-ibm`, `llama-index-embeddings-ibm`,
  `llama-index-readers-web`, `llama-hub`
- [ProxyCurl](https://nubela.co/proxycurl/) API for LinkedIn profile extraction (with a
  mock-data fallback)
