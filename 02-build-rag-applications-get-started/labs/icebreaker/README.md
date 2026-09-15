# LinkedIn Icebreaker Bot (IBM Skills Network Lab)

Final project of [Course 2 — Build RAG Applications: Get Started](../../README.md).
A small end-to-end RAG application: it pulls a LinkedIn profile, indexes it, and lets you
chat with an LLM that only answers from that profile's data — a "conversation icebreaker"
generator plus a Q&A bot over one person's career/education history.

## What it does

1. **Extract** — `modules/data_extraction.py` fetches a LinkedIn profile either via the
   [ProxyCurl](https://nubela.co/proxycurl/) API (real profile, needs an API key) or by
   downloading a pre-made mock JSON profile (`--mock`, no key needed).
2. **Process** — `modules/data_processing.py` turns the raw JSON into a single
   `Document`, splits it into chunks with LlamaIndex's `SentenceSplitter`
   (`config.CHUNK_SIZE`), and embeds the chunks into a `VectorStoreIndex` using
   `WatsonxEmbeddings` (`ibm/granite-embedding-278m-multilingual`).
3. **Query** — `modules/query_engine.py` wraps a `WatsonxLLM`
   (`ibm/granite-4-h-small` by default) in a LlamaIndex query engine with a custom
   `PromptTemplate`, so answers are grounded only in the retrieved profile chunks
   (`config.SIMILARITY_TOP_K` chunks per query) — one template to generate three
   opening "interesting facts" about the person, another to answer free-form questions.
4. **Interact** — two front ends over the same pipeline:
   - `main.py`: a CLI that prints the three facts, then opens a simple chat loop.
   - `app.py`: a [Gradio](https://www.gradio.app/) web UI (`localhost:5000`) with a
     "Process Profile" tab and a "Chat" tab, session-scoped by a UUID so several
     profiles can be processed without mixing their indexes.

## ⚠️ Note on `config.py`

This lab's starter code is normally provided as a `icebreaker.tar` you extract in the
Skills Network Cloud IDE — the lab instructions describe `config.py`'s contents
conceptually rather than printing the file verbatim. The version here was reconstructed
from every `config.XYZ` reference used across the other modules (model IDs, chunk size,
prompt templates, etc.) and is a best effort, not a verbatim copy. If you re-run this
lab from a fresh Cloud IDE extraction, diff your real `config.py` against this one —
`MOCK_DATA_URL` in particular should be double-checked.

## Setup

```bash
cd 02-build-rag-applications-get-started/labs/icebreaker
python3.11 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running

CLI, with mock data (no API key required):

```bash
python main.py --mock
```

CLI against a real profile (needs a ProxyCurl API key):

```bash
python main.py --url "https://www.linkedin.com/in/<someone>/" --api-key "<your-proxycurl-key>"
```

Web UI:

```bash
python app.py
```

Opens a Gradio app on port 5000 (with `share=True`, also prints a temporary public link).

## Sanity check

```bash
python test_config.py
```

Prints whether the prompt templates are defined and the configured chunk size /
`similarity_top_k`, without calling any model.
