# Course 6 — Fundamentals of Building AI Agents

**Coursera course:** [fundamentals-of-building-ai-agents](https://www.coursera.org/learn/fundamentals-of-building-ai-agents)
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟢 Done

## Learning goals

- Build AI agents that reason and complete tasks on their own
- Set up tool calling and chaining to form structured AI workflows
- Use LangChain's built-in agents to analyze data, create charts and run database queries
- Apply prompt engineering and tool-calling practices to improve agent performance

## Course structure

1. Foundations of Tool Calling and Chaining — Lab 1
2. LCEL and Manual Tool Calling in LangChain — Labs 2–4
3. Using Built-in Agents in LangChain — Labs 5–6

## Labs

### Lab 1 — Build an AI Math Assistant with LangChain Tool Calling

- **Task:** Build a math agent that decides on its own which tool to call, then extend it with a Wikipedia search tool. Includes 1 exercise.
- **Approach:**
  - **Tools:** created tools two ways, with the `Tool` class and with the `@tool` decorator (which generates an argument schema automatically), including a tool with several typed inputs.
  - **Agents:** built agents with LangChain's `create_agent`, using Granite (`ibm/granite-4-h-small`) and OpenAI (`gpt-5.4-nano`) as the LLM.
  - **Math toolkit:** one agent with add, subtract, multiply and divide tools, verified with automated test cases (4/4 passed after fixing the subtraction tool).
  - **Built-in tools:** added a Wikipedia search tool, so the agent can answer multi-step questions like "What is the population of Canada? Multiply it by 0.75".
  - **Exercise:** a power tool (x^y), tested with "5 to the power of 2" → 25.
- **Code:** [`labs/lab_1_AI-Math-Assistant Tool Calling.ipynb`](<./labs/lab_1_AI-Math-Assistant%20Tool%20Calling.ipynb>)
- **Key learning:** The agent is only as reliable as its tools. The first add tool ignored decimals and returned 0 for "27.72 + 2.14 + 1.79", but the LLM still answered 31.65 on its own, so the wrong tool result stayed hidden. Testing tools directly and checking the tool messages, not just the final answer, catches this.

### Lab 2 — DataWizard: AI-Powered Data Analysis with LCEL

- **Task:** Give an LLM agent tools to explore CSV datasets and train quick baseline models.
- **Approach:**
  - Tools to list CSV files, cache them in memory, summarize them, run DataFrame methods (`head`, `describe`, …) and evaluate a classification or regression dataset with scikit-learn.
  - A tool-calling agent (`create_openai_tools_agent`, `gpt-4o-mini`) wrapped in an `AgentExecutor` for the ReAct loop, plus a small chat loop ("DataWizard").
- **Code:** [`LLM-Powered Data Science LCEL.ipynb`](<./labs/fundamentals%20of%20Building%20AI%20Agents/LLM-Powered%20Data%20Science%20LCEL.ipynb>)
- **Note:** the agent call failed with an OpenAI `401`, because the "only run locally" cell replaced the lab's API key with the placeholder text. The tools are built, but there is no saved agent output.
- **Key learning:** Each tool should do one small, well-described job; the agent combines them. A shared in-memory cache avoids reloading the same CSV for every tool call.

### Lab 3 — Build Interactive LLM Agents with Tools

- **Task:** Run the tool-calling loop by hand to see what an agent does internally. Includes 3 exercises.
- **Approach:**
  - Arithmetic tools bound to `gpt-4o-mini` with `bind_tools`.
  - Manual loop: the model returns a tool call → the tool runs → a `ToolMessage` goes back into the chat history → the model writes the final answer.
  - Wrapped the loop in a small `ToolCallingAgent` class ("one plus 2", "three times two").
  - Exercises: a `calculate_tip` tool and a `TipAgent` ("How much should I tip on $60 at 20%?" → $12).
- **Code:** [`Build Interactive LLM Agents with Tools.ipynb`](<./labs/fundamentals%20of%20Building%20AI%20Agents/Build%20Interactive%20LLM%20Agents%20with%20Tools.ipynb>)
- **Key learning:** The model never runs a tool itself. It only returns the tool name and arguments; the application executes the tool and sends the result back, matched by the tool call ID.

### Lab 4 — Build a Tool-Calling Agent (YouTube)

- **Task:** An agent that summarizes YouTube videos and collects video data using several tools. Includes 7 exercises.
- **Approach:**
  - Five tools: extract the video ID, fetch the transcript, search YouTube, get full metadata (views, duration, likes, chapters) and get thumbnails.
  - Two-step LCEL chain (`RunnablePassthrough`, `RunnableLambda`): first tool call → second tool call → summary.
  - Recursive "universal" chain that keeps executing tool calls until the model stops asking for them, e.g. "Show top 3 US trending videos with metadata and thumbnails".
  - Exercises: collected ID, metadata, transcript and 42 thumbnails for one video, then produced an analysis with a single LLM call.
- **Code:** [`Manual Tool-Calling Agent.ipynb`](<./labs/fundamentals%20of%20Building%20AI%20Agents/Manual%20Tool-Calling%20Agent.ipynb>)
- **Key learning:** A fixed two-step chain only works when the number of tool calls is known in advance. A recursive loop that stops when no tool calls remain handles open-ended questions.

### Lab 5 — Build Your Own Data Visualization Agent

- **Task:** Ask questions and request charts about a dataset in plain English. Includes 3 exercises.
- **Approach:**
  - A pandas DataFrame agent on Llama 4 Maverick (watsonx.ai) over a student performance dataset (395 students, 33 columns).
  - Questions ("how many rows?", "students over 18") and charts: gender count, alcohol consumption vs. final grade, free time vs. grade, internet access vs. grade.
  - Checked the Python code the agent generated through its intermediate steps.
- **Code:** [`Text-to-chart in Jupyter notebook Visualization Agent.ipynb`](<./labs/fundamentals%20of%20Building%20AI%20Agents/Text-to-chart%20in%20Jupyter%20notebook%20Visualization%20Agent.ipynb>)
- **Key learning:** The agent writes and runs pandas/matplotlib code. Reading its intermediate steps shows exactly how an answer was computed, which is how you verify it.

### Lab 6 — Build a Natural Language SQL Agent

- **Task:** Answer questions about a MySQL database in plain English.
- **Approach:**
  - MySQL server with the Chinook sample database (music store).
  - Granite (`ibm/granite-4-h-small`) via `WatsonxLLM`, connected with LangChain's `SQLDatabase` and `create_sql_agent` (ReAct agent).
  - Low temperature (0.2) for stable SQL generation; test question: "How many albums are there in the database?"
- **Code:** [`llm_agent.py`](<./labs/fundamentals%20of%20Building%20AI%20Agents/project%20%281%29/llm_agent.py>), [`sql_agent.py`](<./labs/fundamentals%20of%20Building%20AI%20Agents/project%20%281%29/sql_agent.py>) · [lab instructions](<./labs/fundamentals%20of%20Building%20AI%20Agents/lab-instructions%20%284%29.md>)
- **Note:** database password and host are read from the `MYSQL_PASSWORD` and `MYSQL_HOST` environment variables instead of being written in the code.
- **Key learning:** The SQL agent reads the database schema itself and writes the query, so the user does not need to know table names. Credentials belong in environment variables, never in code.

## Key takeaways

- An agent = LLM + tools + a loop: the model decides which tool to call, reads the result and answers.
- The model only proposes tool calls; the application executes them and returns the results as tool messages.
- The `@tool` decorator builds the tool schema from type hints and the docstring; clear names and descriptions help the model pick the right tool.
- Fixed chains suit known workflows; recursive tool loops handle open-ended questions.
- Built-in agents (pandas, SQL) turn plain-English questions into code or SQL; inspecting the intermediate steps is how you check their answers.
- Always test tools on their own, and keep credentials out of code.

## Tools & libraries

- Python, Jupyter Notebook
- LangChain (`langchain`, `create_agent`, `@tool`, `bind_tools`, LCEL, `AgentExecutor`), LangGraph
- LangChain built-in agents: pandas DataFrame agent, SQL agent (`create_sql_agent`)
- IBM watsonx.ai — Granite 4, Llama 4 Maverick
- OpenAI — GPT-4o mini, GPT-5.4 nano
- pandas, matplotlib, scikit-learn, MySQL (Chinook database)
- YouTube tools: `youtube-transcript-api`, `pytube`, `yt-dlp`; Wikipedia API
