# Course 5 — Build Multimodal Generative AI Applications

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟡 In progress (~20%)

## Learning goals

- Work with models that accept and produce multiple modalities (text, image, audio)
- Build prompts and pipelines that combine image understanding with text generation
- Apply multimodal RAG (retrieving over images / mixed content)
- Ship a multimodal application feature end to end

## Labs

### Lab 1 — Use Mistral and gTTS to Create Your Personal Storyteller

- **Task:** Generate a short educational story with an LLM and turn it into speech.
- **Approach:**
  - Mistral Medium (`mistralai/mistral-medium-2505`) on watsonx.ai writes a 200–300-word story for a given topic.
  - gTTS converts the story to an MP3, which plays directly in the notebook.
  - Exercise: a second story on "introduction to cloud".
- **Code:** [`labs/lab1/Use Mixtral and gTTS to create your personal storyteller.ipynb`](<./labs/lab1/Use%20Mixtral%20and%20gTTS%20to%20create%20your%20personal%20storyteller.ipynb>)
- **Key learning:** Two single-purpose models (text LLM → text-to-speech) chained together already make a multimodal app.

### Module 1 Final Project — AI Meeting Assistant

- **Task:** A Gradio app that turns a meeting recording into meeting minutes and a task list.
- **Approach:**
  1. **Speech-to-text:** Whisper (`openai/whisper-medium`) transcribes the audio.
  2. **Fix terminology:** Granite (`ibm/granite-4-h-small`) spells out financial terms, e.g. "VaR" → "Value at Risk (VaR)".
  3. **Write minutes:** a LangChain chain produces summary, key points, decisions and tasks.
  4. **Output:** shown in the app and downloadable as `.txt`.
- **Code:** [`speech_analyzer.py`](./labs/lab1/final_project_Modul_1/speech_analyzer.py) (final app) · practice scripts: [`hello.py`](./labs/lab1/final_project_Modul_1/hello.py), [`simple_speech2text.py`](./labs/lab1/final_project_Modul_1/simple_speech2text.py), [`speech2text_app.py`](./labs/lab1/final_project_Modul_1/speech2text_app.py), [`simple_llm.py`](./labs/lab1/final_project_Modul_1/simple_llm.py)
- **Result:** [`meeting_minutes_and_tasks.txt`](./labs/lab1/final_project_Modul_1/meeting_minutes_and_tasks.txt) · screenshots: [part 1](./labs/lab1/final_project_Modul_1/meeting_summary_AUDIO1.png), [part 2](./labs/lab1/final_project_Modul_1/meeting_summary_AUDIO1_2.png)
- **Key learning:** Cleaning up the transcript before summarizing improves the result. With random sampling, the model sometimes invents details (e.g. an assignee nobody named).

## Key takeaways

- Chaining single-purpose models (speech-to-text, LLM, text-to-speech) is a simple way to build multimodal apps.
- Speech-to-text output should be cleaned up before an LLM summarizes it.
- For structured outputs like task lists, use low temperature or greedy decoding to avoid invented details.

## Tools & libraries

- Python
- IBM watsonx.ai (`ibm-watsonx-ai`) — Mistral Medium
- gTTS (Google Text-to-Speech)
- Hugging Face Transformers — OpenAI Whisper (`whisper-tiny.en`, `whisper-medium`)
- LangChain (`langchain-ibm`, LCEL) — IBM Granite 4 (`granite-4-h-small`)
- Gradio
- Jupyter Notebook
