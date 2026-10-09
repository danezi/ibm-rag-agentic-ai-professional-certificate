# Course 1 — Develop Generative AI Applications: Get Started

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟢 Done

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

- **Task:** Learn prompt engineering with an IBM Granite model, from basic prompts to advanced techniques and reusable LangChain templates. Includes 5 exercises.
- **Approach:**
  - **Setup:** `ibm/granite-4-h-small` via `WatsonxLLM`, wrapped in a reusable helper with default generation parameters.
  - **Prompting techniques:** compared zero-, one- and few-shot prompts, then chain-of-thought and self-consistency for reasoning tasks.
  - **Templates:** moved prompts into `PromptTemplate` objects and applied them to summarization, QA, classification, code generation and role play.
- **Code:** [`labs/In-Context Learning and Prompt Templates for Advanced AI.ipynb`](./labs/In-Context%20Learning%20and%20Prompt%20Templates%20for%20Advanced%20AI.ipynb)
- **Key learning:** Prompt structure affects output quality more than parameter tuning. Few-shot examples fix format and tone; chain-of-thought improves reasoning; templates make prompts reusable.

### Lab 2 — Build Smarter AI Apps: Empower LLMs with LangChain

- **Task:** Work through LangChain's core building blocks and combine them into RAG, chatbots and an agent. Includes 7 exercises.
- **Approach:**
  - **Models & messages:** Granite and Llama 4 as chat models with system, human and AI messages; compared models and temperatures.
  - **Templates & output parsers:** `ChatPromptTemplate`, plus JSON (Pydantic), list and string parsers for structured output.
  - **RAG:** load → split → embed (Granite embeddings) → store in Chroma → retrieve → answer with `RetrievalQA`.
  - **Memory:** conversation buffer and summary memory so the chatbot keeps context.
  - **Chains:** the same workflow built with legacy `SequentialChain` and with LCEL (`prompt | llm | parser`).
  - **Agents:** a ReAct agent using a Python REPL and custom `@tool` functions.
- **Code:** [`labs/Build Smarter AI Apps Empower LLMs with LangChain.ipynb`](./labs/Build%20Smarter%20AI%20Apps%20Empower%20LLMs%20with%20LangChain.ipynb)
- **Key learning:** LangChain's strength is composition: a few building blocks (prompt, LLM, parser, retriever, memory, tool) combine into RAG pipelines, chatbots and agents. LCEL is the current standard for building chains.

### Final Project — Build Your First GenAI Application the Right Way

- **Task:** A Flask "AI Assistant" for customer support that returns structured JSON instead of free text. Includes an exercise adding `category` and `action` fields.
- **Approach:**
  - **Backend:** a Flask `/generate` endpoint that routes each message to the selected model and measures response time.
  - **Three models:** Granite, Llama 4 and Mistral Small via `ChatWatsonx`, selectable in the UI for side-by-side comparison.
  - **Structured output:** a Pydantic schema (`summary`, `sentiment`, `response`, `category`, `action`) enforced with `JsonOutputParser`.
  - **Model-specific prompts:** each model family gets its own template with its native special tokens.
  - **Frontend:** a minimal chat page with a model selector.
- **Code:** [`labs/genai_flask_app/`](./labs/genai_flask_app/)
- **Screenshots:**

  ![AI Assistant Flask app](<./labs/genai_flask_app/screenshot.png>)
- **Key learning:** The real work is not the chat interface but reliable output: a validated JSON schema and prompts adapted to each model family.

## Key takeaways

- Lower `temperature` / `top_p` / `top_k` for factual tasks; raise them for variety.
- Zero- → one- → few-shot trades prompt length for reliability.
- Chain-of-thought shows the reasoning steps; self-consistency combines several runs to reduce errors.
- `PromptTemplate` separates the prompt wording from the input data, which is the basis for chains, RAG and agents.
- RAG pipeline: load → split → embed → store → retrieve → answer.
- Output parsers turn free text into structured Python objects.
- Memory passes earlier messages back to the model so a chatbot keeps context.
- Agents use the LLM to decide which tool to call (ReAct: thought → action → observation).
- A production-ready GenAI app needs a validated output schema and model-specific prompt templates.

## Tools & libraries

- Python, Jupyter Notebook, Flask
- IBM watsonx.ai — Granite, Llama 4, Mistral Small; Granite embeddings
- LangChain (`langchain`, `langchain-core`, `langchain-community`, `langchain-experimental`, `langchain-ibm`)
- ChromaDB, `pypdf`
- Pydantic
