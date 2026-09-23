# Course 3 — Vector Databases for RAG: An Introduction

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Specialization](../README.md)
**Status:** 🟡 In progress (Modules 1–2 done: Introduction to Vector Databases and Similarity Search)

## Learning goals

- Understand embeddings, vector similarity, and distance metrics
- Compare vector database options and their indexing strategies (e.g. HNSW, IVF)
- Store, query, and filter vectors with metadata
- Integrate a vector database into a RAG retrieval step

## Labs

### Lab 1 — Similarity Search by Hand

- **Task:** Manually compute the distance/similarity metrics behind vector similarity search — L2 (Euclidean) distance, dot product, and cosine similarity — first with hand-written functions, then with library equivalents, and finish by using cosine similarity to answer a query against a small document set. Includes 3 exercises.
- **Approach:**
  - Embedded 4 single-sentence documents (deliberately ambiguous — all start with "Bugs", but split between software-bug and insect meanings) with `sentence-transformers`' `paraphrase-MiniLM-L6-v2` → `(4, 384)` embedding matrix.
  - **L2 distance:** hand-rolled `euclidean_distance_fn` in a nested loop, cross-checked against `scipy.spatial.distance.cdist` with `np.allclose`. Exercise 1 optimized the manual loop to only fill the upper triangle and mirror it, instead of recomputing the symmetric lower half and the zero diagonal.
  - **Dot product:** hand-rolled `dot_product_fn`, then the same result via matrix multiplication (`embeddings @ embeddings.T`, equivalently `np.matmul`/`np.dot`) — similarity, not distance, so negating it turns it into a distance.
  - **Cosine similarity:** normalized every embedding by its L2 norm (manually, and cross-checked against `torch.nn.functional.normalize`), then took the dot product of normalized vectors. Exercise 2 verified normalization by confirming each normalized vector's L2 norm ≈ 1. Exercise 3 embedded a new query ("Who is responsible for a coding project and fixing others' mistakes?"), normalized it, computed cosine similarity against all 4 documents via `normalized_embeddings_manual @ normalized_query_embedding.T`, and used `argmax` to retrieve the correct (software-bug) document.
- **Code:** [`labs/Similarity Search by Hand.ipynb`](<./labs/Similarity%20Search%20by%20Hand.ipynb>)
- **Key learning:** The three metrics answer different questions and aren't interchangeable: L2 distance is sensitive to vector magnitude, the raw dot product conflates magnitude with direction, while cosine similarity isolates direction (semantic content) by normalizing magnitude away — which is why it's the standard choice for embedding-based semantic search. Also, a full similarity search is just this pairwise-metric computation applied to a query vector against a document matrix and taking the `argmax`/top-k — the same operation a vector database's index (HNSW, IVF, etc.) is built to approximate at scale instead of computing exhaustively.

### Lab 2 — Similarity Search on Text Using ChromaDB and Python

- **Task:** Move from computing similarity by hand to using an actual vector database. Set up a ChromaDB collection with an automatic embedding function, insert a small grocery-item text corpus with metadata, retrieve everything back, then run a semantic similarity search for the query "apple" and inspect the top-3 matches with their distance scores.
- **Approach:**
  - Defined a `SentenceTransformerEmbeddingFunction` (`all-MiniLM-L6-v2`) so ChromaDB auto-embeds any text passed to it — no manual `model.encode()` step like in Lab 1.
  - Created an in-memory `chromadb.Client()` collection configured with `hnsw.space: "cosine"` (cosine distance as the index's similarity metric) and the embedding function above.
  - Inserted 14 grocery-item documents (`collection.add`) with per-document metadata (`source`, `category`) and generated IDs (`food_1`, `food_2`, …).
  - Retrieved all stored documents with `collection.get()` (a "SELECT *", no similarity involved) to confirm the insert.
  - Ran `collection.query(query_texts=["apple"], n_results=3)` — ChromaDB embeds the query text itself, compares it against every stored vector via the configured cosine index, and returns the 3 closest matches with IDs, texts, and distance scores.
  - Result: `golden apple` (0.3825), `fresh red apples` (0.4809), `red fruit` (0.5965) — semantically closest items ranked by distance, run and verified in the Coursera cloud IDE (Theia).
- **Code:** [`labs/chroma-similarity-search/similarity_search.py`](./labs/chroma-similarity-search/similarity_search.py) — [terminal run](./labs/chroma-similarity-search/screenshot-run.png)
- **Key learning:** A vector database collapses the manual Lab 1 pipeline (embed → normalize → compute pairwise distance → argmax) into three calls (`create_collection`, `add`, `query`) by baking the embedding function and distance metric into the collection's configuration up front. `hnsw.space` is where the distance metric decision from Lab 1 (cosine vs. L2 vs. dot product) actually gets made in a real system — HNSW is the approximate-nearest-neighbor index that makes `query()` fast at scale instead of the exhaustive pairwise computation done by hand earlier.

## Key takeaways

- Cosine similarity = dot product of L2-normalized vectors; it's preferred for semantic search because it ignores vector magnitude and compares direction only.
- L2 distance, dot product, and cosine similarity are related but distinct: pick the metric based on whether magnitude should matter (L2, dot product) or be ignored (cosine).
- All three metrics vectorize cleanly into matrix operations (`cdist`, `@`/`matmul`) instead of nested Python loops — this is the computational pattern a vector database's index has to approximate efficiently at scale.
- A vector database (e.g. ChromaDB) bundles what Lab 1 did by hand into collection config: an embedding function (text → vector, automatic on insert and query) and a distance metric/index (`hnsw.space`) — `add()` and `query()` replace manual embedding, normalization, and pairwise distance computation.
- [More to come as the course progresses]

## Tools & libraries

- Python, NumPy, SciPy, PyTorch
- `sentence-transformers` (`paraphrase-MiniLM-L6-v2`, `all-MiniLM-L6-v2`) for text embeddings
- ChromaDB (`chromadb`) — in-memory vector database with HNSW indexing
- Jupyter Notebook
