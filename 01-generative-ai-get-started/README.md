# Course 1 — Develop Generative AI Applications: Get Started

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Specialization](../README.md)
**Status:** 🟡 In progress (~68%)

## Learning goals

- Understand what generative AI is and where LLMs fit into an application stack
- Work with foundation models through APIs and SDKs (prompts, parameters, responses)
- Apply prompt engineering patterns — zero-/one-/few-shot, chain-of-thought, self-consistency — for reliable output
- Structure prompts with LangChain `PromptTemplate` and reuse them across use cases
- Compose LangChain components — output parsers, chains (LCEL), memory, retrievers, tools, agents — into multi-step apps
- Build a retrieval-augmented generation (RAG) pipeline: load → split → embed → store → retrieve → answer
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

### Lab 2 — Build Smarter AI Apps: Empower LLMs with LangChain

- **Task:** Work through the core LangChain building blocks against watsonx.ai models, then combine them into higher-level apps: structured output, retrieval-augmented generation, conversational memory, multi-step chains, and a tool-using agent. Includes 7 exercises.
- **Approach:**
  - **Models & messages:** wrapped `ibm/granite-4-h-small` and `meta-llama/llama-4-maverick-17b-128e-instruct-fp8` (via `ibm-watson-machine-learning`'s `WatsonxLLM`) as LangChain chat models and drove them with `SystemMessage` / `HumanMessage` / `AIMessage` sequences. Exercise 1 compared models and temperatures on identical prompts.
  - **Prompt templates & output parsers:** string `PromptTemplate`, `ChatPromptTemplate`, and `MessagesPlaceholder`; `JsonOutputParser` (with a Pydantic model), `CommaSeparatedListOutputParser`, and `StrOutputParser` to turn completions into structured Python objects.
  - **RAG:** `PyPDFLoader` / `WebBaseLoader` → `CharacterTextSplitter` / `RecursiveCharacterTextSplitter` → `WatsonxEmbeddings` (`ibm/granite-embedding-278m-multilingual`) → `Chroma` vector store → vector-store-backed and `ParentDocumentRetriever` retrievers → `RetrievalQA`.
  - **Memory:** `ChatMessageHistory`, `ConversationBufferMemory` / `ConversationSummaryMemory` inside a `ConversationChain` so the model keeps context across turns.
  - **Chains:** built the same workflows two ways — legacy `LLMChain` / `SequentialChain` vs LCEL (`prompt | llm | parser` with `RunnablePassthrough.assign`).
  - **Tools & agents:** wrapped `PythonREPL` and custom `@tool` functions, then ran a ReAct agent with `create_react_agent` + `AgentExecutor` over the toolkit.
- **Code:** [`labs/Build Smarter AI Apps Empower LLMs with LangChain.ipynb`](./labs/Build%20Smarter%20AI%20Apps%20Empower%20LLMs%20with%20LangChain.ipynb)
- **Key learning:** LangChain's payoff is composition — the same few primitives (prompt, LLM, parser, retriever, memory, tool) snap together into RAG pipelines, chatbots, and agents, and models or prompts can be swapped without touching the wiring. LCEL (`|`) is now the default way to build chains; `SequentialChain` still works but is more rigid. RAG is a fixed pipeline (load → split → embed → store → retrieve → stuff into prompt); agents add a reason–act–observe (ReAct) loop on top so the LLM decides which tool to call.

## Key takeaways

- Decoding parameters: lower `temperature` / `top_p` / `top_k` for deterministic, factual tasks; raise them for variety (e.g. self-consistency, brainstorming).
- In-context learning progression: zero-shot → one-shot → few-shot trades prompt length for reliability; add examples only until the format stabilizes.
- Chain-of-thought makes the model show intermediate steps; self-consistency aggregates multiple CoT samples to reduce single-path errors.
- LangChain `PromptTemplate` separates prompt wording from the data filled into it — the basis for chains and, later, RAG and agents.
- The same small set of prompting patterns covers summarization, QA, classification, code generation and role play.
- LangChain's value is composition: swap models or prompts without rewriting app logic; LCEL (`|`) is the current standard for chains, with `LLMChain` / `SequentialChain` kept for backward compatibility.
- RAG pipeline = document loader → text splitter → embedding model → vector store → retriever → prompt; `RetrievalQA` wires retrieval into a QA chain.
- Output parsers (JSON/Pydantic, CSV, `StrOutputParser`) turn free-text completions into structured Python objects.
- Conversational memory (`ChatMessageHistory`, `ConversationBufferMemory`, `ConversationSummaryMemory`) re-injects prior turns so a chat model keeps context.
- Agents use an LLM as a reasoning engine over tools: `create_react_agent` + `AgentExecutor` run a thought → action → observation (ReAct) loop.

## Tools & libraries

- Python, Jupyter Notebook
- IBM watsonx.ai — `ibm-watsonx-ai`, `ibm-watson-machine-learning`; models `ibm/granite-4-h-small`, `meta-llama/llama-4-maverick-17b-128e-instruct-fp8`; embeddings `ibm/granite-embedding-278m-multilingual`
- LangChain — `langchain`, `langchain-core`, `langchain-community` (document loaders, `Chroma`), `langchain-experimental` (`PythonREPL`), `langchainhub`
- `langchain-ibm` — `WatsonxLLM` / `WatsonxEmbeddings` integrations (Lab 2 also uses `ibm-watson-machine-learning`'s older `WatsonxLLM` wrapper)
- Chroma vector database (`chromadb`), `pypdf` for PDF loading
