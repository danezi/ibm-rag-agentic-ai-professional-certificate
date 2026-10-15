# Course 6 — Fundamentals of Building AI Agents

**Coursera course:** [fundamentals-of-building-ai-agents](https://www.coursera.org/learn/fundamentals-of-building-ai-agents)
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟡 In progress (~15%)

## Learning goals

- Build AI agents that reason and complete tasks on their own
- Set up tool calling and chaining to form structured AI workflows
- Use LangChain's built-in agents to analyze data, create charts and run database queries
- Apply prompt engineering and tool-calling practices to improve agent performance

## Course structure

1. Foundations of Tool Calling and Chaining — Lab 1
2. LCEL and Manual Tool Calling in LangChain
3. Using Built-in Agents in LangChain

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

## Key takeaways

- An agent = LLM + tools + a loop: the model decides which tool to call, reads the result and answers.
- The `@tool` decorator builds the tool schema from type hints and the docstring; clear names and descriptions help the model pick the right tool.
- Always test tools on their own before giving them to an agent, and inspect the tool calls in the message history.

## Tools & libraries

- Python, Jupyter Notebook
- LangChain (`langchain`, `create_agent`, `@tool`), LangGraph
- IBM watsonx.ai (`langchain-ibm`, `ChatWatsonx`) — Granite 4
- OpenAI (`langchain-openai`) — GPT-5.4 nano
- Wikipedia API (`langchain-community`, `wikipedia`)
