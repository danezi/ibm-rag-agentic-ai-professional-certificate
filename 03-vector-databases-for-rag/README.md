# Course 3 — Vector Databases for RAG: An Introduction

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Specialization](../README.md)
**Status:** 🟡 In progress (Labs 1–3 + final project done)

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

### Lab 3 — Similarity Search on Employee Records Using Python and ChromaDB

- **Task:** Apply the ChromaDB pattern from Lab 2 to a richer, structured dataset (15 employees with role/department/skills/experience/location) and go beyond plain similarity search into metadata filtering and combined (similarity + filter) queries. Includes a practice exercise that repeats the whole pattern independently on a books dataset.
- **Approach:**
  - Built one text document per employee by concatenating role, experience, department, skills, and location into a single descriptive string, embedded via the same `all-MiniLM-L6-v2` cosine-HNSW collection pattern as Lab 2 — this is the standard "flatten structured fields into a searchable text blob" move for putting relational-shaped data into a vector index.
  - Kept the original structured fields as ChromaDB **metadata** (`department`, `role`, `experience`, `location`, `employment_type`) alongside the embedded text, so results can be filtered on exact/range values that embeddings can't reliably capture (e.g. "10+ years experience").
  - Ran plain similarity queries ("Python developer with web development experience", "team leader manager with experience"), pure metadata filters via `collection.get(where=...)` (department equality, `$gte` on experience, `$in` on location), and a **combined** query mixing `query_texts` similarity with an `$and`/`$gte`/`$in` `where` clause — e.g. "senior Python developer full-stack" restricted to 8+ years and three named tech-hub cities.
  - **Practice exercise (`books_advanced_search.py`):** rebuilt the identical collection → similarity search → metadata filter → combined search pattern from scratch on an 8-book dataset (genre/year/rating/pages), confirming the pattern generalizes to a different domain.
- **Code:** [`labs/lab3-employee-similarity-search/similarity_employeedata.py`](./labs/lab3-employee-similarity-search/similarity_employeedata.py), practice exercise: [`books_advanced_search.py`](./labs/lab3-employee-similarity-search/books_advanced_search.py) — [terminal run](./labs/lab3-employee-similarity-search/screenshot-run.png)
- **Key learning:** Semantic similarity and metadata filtering solve different problems and are meant to be combined, not chosen between — embeddings answer "what's conceptually similar" while `where` filters answer "what satisfies this exact constraint" (a range, an enum, a set membership) that a vector alone can't express reliably. ChromaDB's `where` clause (`$and`, `$gte`, `$in`, …) applies **before or alongside** the vector search rather than as a manual post-filter, which is what makes queries like "similar to X, but only 8+ years experience in these three cities" a single call instead of fetch-then-filter application logic.

## Final Project — Interactive Food Search and RAG Chatbot System

- **Task:** Build three progressively more capable food-recommendation systems on the same ~185-item food dataset (name, description, ingredients, calories, cuisine, cooking method, taste/health features) sharing one ChromaDB-backed core: (1) an interactive CLI similarity search, (2) an advanced search system with metadata filtering, and (3) a full RAG chatbot that grounds an LLM's natural-language answers in retrieved food data — then compare all three head-to-head.
- **Approach:**
  - **Shared core (`shared_functions.py`):** dataset loading/normalization, `create_similarity_search_collection` (ChromaDB, `all-MiniLM-L6-v2`, cosine HNSW), `populate_similarity_collection` (flattens each food item's name/description/ingredients/cuisine/cooking method/taste/health-benefit fields into one embeddable text blob, keeps the structured fields as metadata), and `perform_similarity_search` / `perform_filtered_similarity_search` — reused by every system below instead of duplicating the ChromaDB wiring per script.
  - **System 1 — `interactive_search.py`:** a CLI chat loop (`help`/`history`/`quit`) that runs plain similarity search per query and derives lightweight follow-up suggestions from the result set (e.g. suggests other cuisines seen in the top matches, or a "low calorie" query if the average result is calorie-heavy).
  - **System 2 — `advanced_search.py`:** a menu-driven CLI exposing basic search, cuisine-filtered search, calorie-filtered search (`where={"calories": {"$lte": N}}`), and combined filters, plus a scripted demonstration mode that runs three preset filtered queries back-to-back.
  - **System 3 — `rag_chatbot.py`:** retrieves the top-3 similarity matches for a user's natural-language query, formats them into a structured context block, and passes that context plus the query into an IBM watsonx.ai `ModelInference` (`ibm/granite-4-h-small`) prompt instructed to recommend 2–3 items and explain why — the RAG pattern (retrieve → stuff context into prompt → generate) applied to conversational food recommendations, with a rule-based `generate_fallback_response` if the LLM call fails or returns too little text. Also implements a `compare` mode that runs two queries through the same retrieve-then-generate pipeline and asks the LLM to contrast them.
  - **Extra practice scripts:** `calorie_checker.py` (interactive calorie-budget search, splits results into "fits budget" vs. "over budget" using the same filtered-search helper) and `result_limiter.py` (runs one query at `n_results` = 1/3/5/10 and reports how average/best/worst similarity score shifts with `k`, i.e. a hands-on precision/recall-at-k intuition check).
  - **`system_comparison.py`:** runs the identical query ("chocolate dessert") through all three systems' retrieval path back-to-back with timing, then prints a side-by-side capability summary (interactive: fast but limited context; advanced: precise but filter-syntax-aware; RAG: conversational but the most complex to build).
- **Code:** [`labs/practice-food-recommendation-rag/`](./labs/practice-food-recommendation-rag/) — [terminal run (system comparison)](./labs/practice-food-recommendation-rag/screenshot-system-comparison.png)
- **Key learning:** The same `shared_functions.py` retrieval core powers three completely different user experiences (raw search, filtered search, conversational RAG) — the LLM in the RAG chatbot doesn't replace the vector search, it sits *after* it and only ever sees the top-k retrieved items as context, which is what keeps its food recommendations grounded in the actual dataset instead of invented dishes. `result_limiter.py` also makes concrete why `n_results` (top-k) is a real tuning knob: similarity score quality degrades predictably as k grows, since low-ranked results are, by construction, less similar to the query.

## Key takeaways

- Cosine similarity = dot product of L2-normalized vectors; it's preferred for semantic search because it ignores vector magnitude and compares direction only.
- L2 distance, dot product, and cosine similarity are related but distinct: pick the metric based on whether magnitude should matter (L2, dot product) or be ignored (cosine).
- All three metrics vectorize cleanly into matrix operations (`cdist`, `@`/`matmul`) instead of nested Python loops — this is the computational pattern a vector database's index has to approximate efficiently at scale.
- A vector database (e.g. ChromaDB) bundles what Lab 1 did by hand into collection config: an embedding function (text → vector, automatic on insert and query) and a distance metric/index (`hnsw.space`) — `add()` and `query()` replace manual embedding, normalization, and pairwise distance computation.
- Similarity search and metadata filtering are complementary, not competing: embed unstructured meaning into the vector, keep structured fields (numbers, enums, dates) as metadata, and combine both in one `query(where=...)` call.
- RAG = retrieve top-k from a vector store, format it as context, hand it to an LLM with an instruction to answer only from that context — the LLM never sees the whole dataset, only what similarity search already judged relevant.
- `n_results`/top-k is a tunable trade-off: more results mean more (and lower-quality) context, so the right k depends on how much the generation step can usefully digest.

## Tools & libraries

- Python, NumPy, SciPy, PyTorch
- `sentence-transformers` (`paraphrase-MiniLM-L6-v2`, `all-MiniLM-L6-v2`) for text embeddings
- ChromaDB (`chromadb`) — in-memory vector database with HNSW indexing, metadata filtering (`where`)
- IBM watsonx.ai (`ibm-watsonx-ai`) — `ModelInference` with `ibm/granite-4-h-small` for the RAG chatbot's generation step
- Jupyter Notebook
