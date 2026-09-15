"""Configuration file for the Icebreaker Bot.

NOTE: This file is normally provided as starter/boilerplate code when you
extract icebreaker.tar in the Cloud IDE. The lab instructions describe its
contents conceptually but do not print the full file verbatim, so the
values below (especially MOCK_DATA_URL and the exact prompt wording) are a
best-effort reconstruction based on every config.XYZ reference used across
the other modules. Please compare this against your actual config.py in
the Cloud IDE (from the tar extraction) before replacing it - keep your
real MOCK_DATA_URL if it differs from the placeholder below.
"""

# --- watsonx.ai connection settings ---
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
WATSONX_PROJECT_ID = "skills-network"

# --- Model IDs ---
LLM_MODEL_ID = "ibm/granite-4-h-small"
EMBEDDING_MODEL_ID = "ibm/granite-embedding-278m-multilingual"

# --- LLM generation parameters ---
TEMPERATURE = 0.7
MAX_NEW_TOKENS = 500
MIN_NEW_TOKENS = 1
TOP_K = 50
TOP_P = 1.0

# --- RAG / retrieval settings ---
CHUNK_SIZE = 400  # Smaller chunks for more granular retrieval
SIMILARITY_TOP_K = 7  # Retrieve more chunks for more comprehensive answers

# --- Data source settings ---
# NOTE: verify this against your actual starter config.py - this URL must
# point to a real, reachable mock LinkedIn-profile JSON file.
MOCK_DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/bZyisII_msBvxphC3H0MlQ/mock-profile.json"
PROXYCURL_API_KEY = ""  # Leave empty to use mock data

# --- Prompt templates ---
INITIAL_FACTS_TEMPLATE = """Context information about a person is below.
---------------------
{context_str}
---------------------
Given only the context information above and no prior knowledge, provide
three interesting facts about this person's career or education. Answer
in detail, using only information found in the context.
Answer:
"""

USER_QUESTION_TEMPLATE = """Context information about a person is below.
---------------------
{context_str}
---------------------
Given only the context information above and no prior knowledge, answer
the following question. If the information is not available in the
context, respond with "I don't know."
Question: {query_str}
Answer:
"""
