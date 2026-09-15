# IBM RAG and Agentic AI — Specialization Portfolio

This repository documents my hands-on work through the **[IBM "RAG and Agentic AI" Specialization](https://www.coursera.org/)** on Coursera — a 10-course program covering Retrieval-Augmented Generation, vector databases, and agent frameworks. Retrieval pipelines and agentic systems built with LangChain, LangGraph, CrewAI, AutoGen, and MCP are among the most requested skills in applied GenAI engineering right now, and this repo is where I keep the labs, design decisions, and takeaways from each course in one auditable place.

Every course has its own folder with a dedicated README (learning goals, implemented labs, key learnings) and a `labs/` directory holding the actual notebooks and code.

## Skills covered

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C)
![CrewAI](https://img.shields.io/badge/CrewAI-FF5A50)
![AutoGen](https://img.shields.io/badge/AutoGen-0078D4)
![MCP](https://img.shields.io/badge/Model_Context_Protocol-000000)

**Competency areas**

- RAG architecture — chunking, embeddings, retrieval, generation, evaluation
- Vector databases — indexing, similarity search, metadata filtering
- Advanced retrieval — re-ranking, hybrid search, query transformation, multi-query
- Prompt engineering for grounded, citation-backed responses
- Multimodal GenAI — text, image, and audio inputs
- AI agents — tool use, planning, memory, multi-agent orchestration
- Agent frameworks — LangChain, LangGraph, CrewAI, AutoGen, BeeAI
- Model Context Protocol (MCP) — building and connecting tool servers

## Course progress

Legend: 🟢 Done · 🟡 In progress · ⚪ Not started

| #  | Course | Status | Folder |
|----|--------|--------|--------|
| 1  | Develop Generative AI Applications: Get Started | 🟢 Done | [`01-generative-ai-get-started/`](./01-generative-ai-get-started/) |
| 2  | Build RAG Applications: Get Started | 🟢 Done | [`02-build-rag-applications-get-started/`](./02-build-rag-applications-get-started/) |
| 3  | Vector Databases for RAG: An Introduction | ⚪ Not started | [`03-vector-databases-for-rag/`](./03-vector-databases-for-rag/) |
| 4  | Advanced RAG with Vector Databases and Retrievers | ⚪ Not started | [`04-advanced-rag-vector-databases-retrievers/`](./04-advanced-rag-vector-databases-retrievers/) |
| 5  | Build Multimodal Generative AI Applications | 🟡 In progress (~3%) | [`05-build-multimodal-generative-ai-applications/`](./05-build-multimodal-generative-ai-applications/) |
| 6  | Fundamentals of Building AI Agents | ⚪ Not started | [`06-fundamentals-of-building-ai-agents/`](./06-fundamentals-of-building-ai-agents/) |
| 7  | Agentic AI with LangChain and LangGraph | ⚪ Not started | [`07-agentic-ai-langchain-langgraph/`](./07-agentic-ai-langchain-langgraph/) |
| 8  | Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI | ⚪ Not started | [`08-agentic-ai-langgraph-crewai-autogen-beeai/`](./08-agentic-ai-langgraph-crewai-autogen-beeai/) |
| 9  | Build AI Agents using MCP | ⚪ Not started | [`09-build-ai-agents-using-mcp/`](./09-build-ai-agents-using-mcp/) |
| 10 | RAG and Agentic AI Capstone Project | ⚪ Not started | [`10-rag-agentic-ai-capstone-project/`](./10-rag-agentic-ai-capstone-project/) |

_Current status: 1 of 10 courses in progress, 2 completed. Updated 2026-09-15._

## 🏆 Capstone Project Highlight

_Placeholder — to be filled in after course 10._

This section will summarize the capstone project: the problem, the RAG + agentic architecture, the tech stack, key results, and a link to the full write-up and code in [`10-rag-agentic-ai-capstone-project/`](./10-rag-agentic-ai-capstone-project/).

## Running the labs

Most labs call foundation models through **IBM watsonx.ai**. Inside the Coursera/Skills Network lab environment, `credentials` and `project_id` are pre-filled, so the notebooks run without any keys of your own. To run the same code **locally**, create your own watsonx.ai API key and project ID and set them via `.env` (see [`.env.example`](./.env.example)) — the walkthrough for generating those keys is here:
[IBM watsonx.ai: The Interface and API — Sina Nazeri (Medium)](https://medium.com/the-power-of-ai/ibm-watsonx-ai-the-interface-and-api-e8e1c7227358).

Key parameters used when instantiating a model:

- **`model_id`** — which foundation model to use. Options are listed in the [watsonx.ai Foundation Models docs](https://ibm.github.io/watsonx-ai-python-sdk/foundation_models.html); the labs default to `ibm/granite-4-h-small`.
- **`parameters`** — the model's generation config (e.g. decoding method, max/min new tokens, temperature). Run `GenParams().get_example_values()` to see common options; if none are passed, `default_params` are used.
- **`credentials`** and **`project_id`** — required to run any watsonx.ai model. Pre-set in the lab environment; supply your own for local runs.
- **`WatsonxLLM()`** — LangChain wrapper that creates the usable LLM instance.

## How this repository is used

- Each `NN-course-name/` folder has its own `README.md` following a shared template ([`docs/course-readme-template.md`](./docs/course-readme-template.md)): course link, learning goals, a per-lab breakdown (task, approach, code link, key learning), key takeaways, and the tools used.
- Course code and notebooks live in that course's `labs/` folder.
- The progress table above is updated as courses move from ⚪ to 🟡 to 🟢.
- Commits are scoped to one lab or one course update at a time, so the history reads as a learning log.

## About me

- **Study:** M.Sc. Trustworthy Systems (*Vertrauenswürdige Systeme*), Hochschule Bremerhaven
- **Currently:** Working student at Beezubi Lernwelt GmbH — AI data pipelines and a learning app
- **GitHub:** [@danezi](https://github.com/danezi)

## License

Released under the MIT License — see [`LICENSE`](./LICENSE) — for my own code, notebooks, and documentation. Some course/project instruction PDFs from IBM Skills Network are included alongside the relevant lab for reference and remain the property of IBM and Coursera; the MIT License does not extend to that content.
