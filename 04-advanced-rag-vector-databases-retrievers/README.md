# Course 4 — Advanced RAG with Vector Databases and Retrievers

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟢 Done

## Learning goals

- Improve retrieval quality with re-ranking, hybrid search, and query transformation
- Use advanced retriever types (multi-query, parent-document, self-query, MMR)
- Evaluate a RAG system (relevance, groundedness, answer quality)
- Tune chunking and retrieval parameters against measured results

## Labs

### Lab 1 — Build a Smarter Search with LangChain Context Retrieval

- **Task:** Go beyond basic similarity search with four LangChain retriever types. Includes 2 exercises.
- **Approach:**
  - **Setup:** Mistral Small via `WatsonxLLM`, Granite embeddings via `WatsonxEmbeddings`, Chroma as vector store.
  - **Vector Store-Backed Retriever:** compared default top-k, MMR (more diverse results) and a similarity threshold (only relevant matches).
  - **Multi-Query Retriever:** the LLM rewrites one question into several variants and merges the results.
  - **Self-Querying Retriever:** the LLM turns a natural-language request into a metadata filter (e.g. "rated higher than 8.5").
  - **Parent Document Retriever:** searches small chunks but returns the larger parent chunk for more context.
  - **Exercises:** reran two retrievers on new queries. This required clearing the Chroma collection first, which the lab code does not do.
- **Code:** [`labs/Build a Smarter Search with LangChain Context Retrieval.ipynb`](<./labs/Build%20a%20Smarter%20Search%20with%20LangChain%20Context%20Retrieval.ipynb>)
- **Key learning:** Each retriever fixes a specific weakness of plain similarity search. A reused vector store keeps old data, so it must be cleared before loading a new dataset.

### Lab 2 — Explore Advanced Retrievers in LlamaIndex

- **Task:** Explore the same retrieval ideas in LlamaIndex with six retriever types, then build a custom hybrid retriever. Includes 2 exercises.
- **Approach:**
  - **Setup:** Granite (`ibm/granite-4-h-small`) as LLM and `BAAI/bge-small-en-v1.5` as embedding model, set globally via `Settings`.
  - **Retrievers:** Vector Index, BM25 (keyword search), Document Summary Index, Auto Merging, Recursive, and Query Fusion with three merge strategies (RRF, relative score, distribution-based).
  - **Exercise 1:** a hybrid retriever combining vector and BM25 scores. Results are matched by text, since node IDs differ between retrievers.
  - **Exercise 2:** a small RAG pipeline with simple query routing and evaluation.
- **Code:** [`labs/Explore Advanced Retrievers in LlamaIndex.ipynb`](<./labs/Explore%20Advanced%20Retrievers%20in%20LlamaIndex.ipynb>)
- **Key learning:** LangChain and LlamaIndex solve the same problems with different tools: Auto Merging corresponds to Parent Document, Query Fusion to Multi-Query. Semantic and keyword search complement each other.

### Lab 3 — Semantic Similarity with FAISS

- **Task:** Build a semantic search engine on the 20 Newsgroups dataset (~20,000 posts) without a framework.
- **Approach:**
  - Cleaned every post (headers, email addresses, punctuation) before embedding.
  - Embedded all posts with the Universal Sentence Encoder (TensorFlow Hub).
  - Indexed the vectors in FAISS (`IndexFlatL2`, exact search) and queried them. For example, "motorcycle" finds relevant posts without exact keyword matches.
- **Code:** [`labs/Semantic Similarity with FAISS.ipynb`](<./labs/Semantic%20Similarity%20with%20FAISS.ipynb>)
- **Key learning:** Every retriever comes down to the same steps: clean → embed → index → search. The query must be cleaned exactly like the documents, otherwise retrieval quality drops.

## Final Project — AI-Powered YouTube Summarizer & Q&A Tool (RAG, LangChain, FAISS)

- **Task:** A Gradio app that summarizes any YouTube video and answers questions about its content.
- **Approach:**
  - **Transcript:** extracted the video ID and fetched the transcript (manual preferred over auto-generated).
  - **Summary:** the full transcript goes directly to the LLM (`ibm/granite-8b-code-instruct`), no retrieval needed.
  - **Q&A:** the transcript is chunked, embedded and stored in FAISS; the 7 most relevant chunks serve as context for the answer.
  - **Testing:** beyond the lab's test video, tested on two other videos, including a German question about an English video, answered correctly.
- **Code:** [`labs/final-project-youtube-rag-qa/ytbot.py`](./labs/final-project-youtube-rag-qa/ytbot.py)
- **Screenshots:**

  ![Lab example 1 — hallucinations Q&A](<./labs/final-project-youtube-rag-qa/screenshot-1-hallucinations-qa.png>)

  ![Lab example 2 — RAG problems Q&A](<./labs/final-project-youtube-rag-qa/screenshot-2-rag-problems-qa.png>)

  ![Custom video — AI chips](<./labs/final-project-youtube-rag-qa/screenshot-3-custom-video-aws-chips.png>)

  ![Custom video — German question](<./labs/final-project-youtube-rag-qa/screenshot-4-custom-video-german-question.png>)
- **Key learning:** Not every task needs retrieval: a summary can use the full transcript, while Q&A needs only the relevant chunks.

## Key takeaways

- MMR returns more diverse results; a similarity threshold returns only relevant ones instead of a fixed number.
- Multi-Query, Self-Query and Parent Document retrievers each fix a specific weakness of plain similarity search.
- LangChain and LlamaIndex implement the same retrieval ideas under different names.
- Keyword search (BM25) and semantic search complement each other.
- A reused vector store must be cleared before loading new data.
- Every retriever follows the same core steps (clean → embed → index → search), and queries must be cleaned the same way as documents.
- Use retrieval when an answer needs specific context; skip it when the full content fits into the prompt.

## Tools & libraries

- Python, Jupyter Notebook
- LangChain — retrievers: `MultiQueryRetriever`, `SelfQueryRetriever`, `ParentDocumentRetriever`
- LlamaIndex — retrievers: Vector Index, BM25, Document Summary, Auto Merging, Recursive, Query Fusion
- IBM watsonx.ai — `WatsonxLLM` (Mistral Small, Granite), `WatsonxEmbeddings` (Granite, Slate)
- ChromaDB, FAISS (`faiss-cpu`)
- Hugging Face embeddings (`BAAI/bge-small-en-v1.5`), TensorFlow Hub (Universal Sentence Encoder)
- `youtube-transcript-api`, Gradio
