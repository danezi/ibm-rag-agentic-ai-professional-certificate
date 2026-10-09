# Course 3 — Vector Databases for RAG: An Introduction

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟢 Done

## Learning goals

- Understand embeddings, vector similarity, and distance metrics
- Compare vector database options and their indexing strategies (e.g. HNSW, IVF)
- Store, query, and filter vectors with metadata
- Integrate a vector database into a RAG retrieval step

## Labs

### Lab 1 — Similarity Search by Hand

- **Task:** Compute the core similarity metrics by hand, then use them to answer a query against a small document set. Includes 3 exercises.
- **Approach:**
  - Embedded 4 short, deliberately ambiguous documents ("Bugs" as software vs. insects) with `paraphrase-MiniLM-L6-v2`.
  - Implemented L2 distance, dot product and cosine similarity manually and checked them against SciPy/NumPy/PyTorch.
  - Exercises: optimized the distance loop, verified vector normalization, and retrieved the best document for a query via cosine similarity + `argmax`.
- **Code:** [`labs/Similarity Search by Hand.ipynb`](<./labs/Similarity%20Search%20by%20Hand.ipynb>)
- **Key learning:** Cosine similarity ignores vector length and compares only direction, which is why it is the standard metric for semantic search. A vector database does the same computation, just efficiently at scale.

### Lab 2 — Similarity Search on Text Using ChromaDB and Python

- **Task:** Replace the manual pipeline from Lab 1 with a real vector database.
- **Approach:**
  - Created a ChromaDB collection with automatic embeddings (`all-MiniLM-L6-v2`) and cosine distance (`hnsw.space: "cosine"`).
  - Inserted 14 grocery items with metadata and ran a similarity query for "apple".
  - Result: `golden apple`, `fresh red apples`, `red fruit`, ranked by distance.
- **Code:** [`labs/chroma-similarity-search/similarity_search.py`](./labs/chroma-similarity-search/similarity_search.py) — [terminal run](./labs/chroma-similarity-search/screenshot-run.png)
- **Key learning:** A vector database reduces embedding, distance computation and ranking to three calls: `create_collection`, `add`, `query`.

### Lab 3 — Similarity Search on Employee Records Using Python and ChromaDB

- **Task:** Combine semantic search with metadata filtering on a structured employee dataset. Includes a practice exercise on a books dataset.
- **Approach:**
  - Turned each employee record (role, skills, experience, location) into one searchable text, keeping the original fields as metadata.
  - Ran similarity queries, pure metadata filters (`$gte`, `$in`) and combined queries, e.g. "senior Python developer" with 8+ years in specific cities.
  - Repeated the same pattern independently on a books dataset.
- **Code:** [`labs/lab3-employee-similarity-search/similarity_employeedata.py`](./labs/lab3-employee-similarity-search/similarity_employeedata.py), practice exercise: [`books_advanced_search.py`](./labs/lab3-employee-similarity-search/books_advanced_search.py) — [terminal run](./labs/lab3-employee-similarity-search/screenshot-run.png)
- **Key learning:** Embeddings answer "what is similar", metadata filters answer "what meets an exact condition". Combined in one query, they cover both.

## Final Project — Interactive Food Search and RAG Chatbot System

- **Task:** Build three food-recommendation systems on a shared ChromaDB core (~185 dishes) and compare them.
- **Approach:**
  - **Shared core:** `shared_functions.py` handles data loading, the ChromaDB collection and (filtered) similarity search for all systems.
  - **System 1 — Interactive search:** CLI chat with plain similarity search and follow-up suggestions.
  - **System 2 — Advanced search:** filters by cuisine and calories, alone or combined.
  - **System 3 — RAG chatbot:** retrieves the top 3 dishes and lets Granite (`ibm/granite-4-h-small`) recommend and explain them, with a rule-based fallback.
  - **Extras:** a calorie-budget checker, a top-k comparison (`result_limiter.py`) and a side-by-side comparison of all three systems.
- **Code:** [`labs/practice-food-recommendation-rag/`](./labs/practice-food-recommendation-rag/) — [terminal run (system comparison)](./labs/practice-food-recommendation-rag/screenshot-system-comparison.png)
- **Key learning:** In RAG, the LLM does not replace the search. It only sees the retrieved results, which keeps its answers grounded in real data. The number of results (top-k) is a real tuning parameter: more results also means less relevant ones.

## Key takeaways

- Cosine similarity compares direction only and is the default metric for semantic search; L2 and dot product also take vector length into account.
- A vector database bundles embedding, distance metric and indexing (HNSW) into the collection configuration.
- Store meaning in the vector and structured fields as metadata, then combine similarity search and filters in one query.
- RAG = retrieve the top-k results, pass them as context to the LLM, generate an answer from that context only.
- Top-k is a trade-off between more context and lower relevance.

## Tools & libraries

- Python, NumPy, SciPy, PyTorch
- `sentence-transformers` (`paraphrase-MiniLM-L6-v2`, `all-MiniLM-L6-v2`) for text embeddings
- ChromaDB (`chromadb`) — in-memory vector database with HNSW indexing, metadata filtering (`where`)
- IBM watsonx.ai (`ibm-watsonx-ai`) — `ModelInference` with `ibm/granite-4-h-small` for the RAG chatbot's generation step
- Jupyter Notebook
