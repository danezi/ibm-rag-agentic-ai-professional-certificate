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

- **Task:** Build a minimal text → speech pipeline: an LLM writes a short educational story on any topic, and a text-to-speech engine turns it into audio playable directly in the notebook. Includes 1 exercise.
- **Approach:**
  - **LLM setup:** `mistralai/mistral-medium-2505` on watsonx.ai via `ModelInference`, with `GenParams.DECODING_METHOD="greedy"` and `MAX_NEW_TOKENS=1000` (enough headroom for the 200–300-word target). The SDK emitted a `LifecycleWarning` that this model is deprecated from 2026-05-05 until 2027-01-12 — a reminder that hard-coded watsonx model IDs in these labs have a shelf life.
  - **Story generation:** `generate_story(topic)` wraps the topic in a constrained prompt (beginner audience, simple language, interesting facts, ~200–300 words, end with a "what we learned" summary) and calls `model.generate_text()`. Tested on "the life cycle of butterflies".
  - **Text-to-speech:** passed the generated text to `gTTS` (Google Text-to-Speech), saved it as `story.mp3`, then base64-encoded the MP3 and embedded it in an HTML `<audio controls>` element so the notebook plays the story inline.
  - **Exercise:** generated and voiced a second story — on "introduction to cloud" instead of the suggested "the life cycle of a human" — reusing the same function and TTS step. The lab's own solution relies on `io.BytesIO` + `IPython.display.Audio`, neither of which is imported anywhere in the notebook; I kept the working base64/HTML player from the main section instead.
- **Code:** [`labs/lab1/Use Mixtral and gTTS to create your personal storyteller.ipynb`](<./labs/lab1/Use%20Mixtral%20and%20gTTS%20to%20create%20your%20personal%20storyteller.ipynb>)
- **Key learning:** A multimodal app doesn't need a multimodal model — chaining two single-modality components (text LLM → TTS) is often enough, and the integration point is just a string. The prompt carries most of the quality: length, audience, and a closing summary are all specified up front because the TTS step reads everything verbatim, including the Markdown (`**bold**`, list markers) the LLM likes to emit, which a production version would strip before synthesis.

### Module 1 Final Project — AI Meeting Assistant (Whisper, Granite, Gradio)

- **Task:** Build a Gradio app that takes a meeting recording, transcribes it, normalizes domain terminology, and returns meeting minutes plus a task list — both on screen and as a downloadable `.txt` file.
- **Approach:**
  - **Warm-up scripts:** built up the pieces one at a time — a hello-world Gradio interface (`hello.py`), a standalone Whisper transcription of the sample earnings-call clip (`simple_speech2text.py`, `openai/whisper-tiny.en`), a Gradio wrapper around it (`speech2text_app.py`), and a bare watsonx.ai call to `ibm/granite-4-h-small` through LangChain's `WatsonxLLM` (`simple_llm.py`).
  - **Speech-to-text:** in the final app, a Hugging Face `pipeline("automatic-speech-recognition")` with `openai/whisper-medium` (upgraded from `tiny.en`), with 30-second chunking and `batch_size=8`. Non-ASCII characters are stripped from the transcript before it goes to the LLM.
  - **Terminology pass (LLM call 1):** `product_assistant()` sends the raw transcript to Granite through `ModelInference.chat()` (`temperature=0.2`, `top_p=0.6`). A detailed system prompt tells it to expand financial acronyms (e.g. "VaR" → "Value at Risk (VaR)", "401k" → "401(k) retirement savings plan"), convert spoken product numbers to numeric form ("five two nine" → "529 (Education Savings Plan)"), resolve ambiguous acronyms from context, and leave ordinary spelled-out figures alone.
  - **Minutes generation (LLM call 2):** an LCEL chain (`RunnablePassthrough` → `ChatPromptTemplate` → `WatsonxLLM` → `StrOutputParser`) turns the corrected transcript into a summary, key points, decisions, a task list with assignees and deadlines, and notes. The prompt explicitly forbids restating the instructions, returning an empty template, or using information that isn't in the transcript.
  - **Interface:** `gr.Interface` with an audio-upload input and two outputs (a textbox and a `gr.File` download of `meeting_minutes_and_tasks.txt`), served on port 5000.
- **Result:** on the 56-second sample clip, the app correctly extracted the key figures: 99% VaR confidence that losses stay under $5M, a 12.5% tier-one capital ratio, about $135M expected revenue (+8% QoQ), and the planned $200M Pay Plus IPO. The two runs disagreed on the decisions and tasks, though. The run saved in the `.txt` file reports "No specific decisions" and "Assignee/Deadline: Not specified". The run in the screenshots, viewed through the browser's German page translation, lists two decisions and assigns the IPO preparation to the CEO with a 3-month deadline, which I couldn't find in the transcript.
- **Code:** [`speech_analyzer.py`](./labs/lab1/final_project_Modul_1/speech_analyzer.py) (final app), plus [`simple_speech2text.py`](./labs/lab1/final_project_Modul_1/simple_speech2text.py), [`speech2text_app.py`](./labs/lab1/final_project_Modul_1/speech2text_app.py), [`simple_llm.py`](./labs/lab1/final_project_Modul_1/simple_llm.py), [`hello.py`](./labs/lab1/final_project_Modul_1/hello.py). Output: [`meeting_minutes_and_tasks.txt`](./labs/lab1/final_project_Modul_1/meeting_minutes_and_tasks.txt). Screenshots: [minutes, part 1](./labs/lab1/final_project_Modul_1/meeting_summary_AUDIO1.png), [minutes, part 2 — decisions & tasks](./labs/lab1/final_project_Modul_1/meeting_summary_AUDIO1_2.png)
- **Key learning:** The most useful step is the one between the two models. Whisper writes down what it hears, so finance jargon comes out as inconsistent or spelled-out tokens. A dedicated low-temperature LLM pass that only fixes terminology gives the summarization step a cleaner input than one prompt trying to do both jobs. Splitting the pipeline also lets each call use its own settings: low temperature for the faithful rewrite, higher for the free-form minutes. The other lesson is that "use only information from the transcript" doesn't guarantee it. With `decoding_method="sample"` at temperature 0.5, the same audio produced different decisions and an assignee and deadline nobody said. For structured outputs like task lists, greedy decoding or an explicit "write *Not specified* if absent" rule is the safer default.

## Key takeaways

- Chaining single-modality models (LLM → TTS) is the simplest way to build a multimodal experience; the text output of one step is the input of the next.
- LLM output destined for speech should be cleaned of Markdown formatting first — TTS engines read symbols and structure literally.
- Speech → text pipelines benefit from a separate "normalize the transcript" LLM step before any summarization: ASR output is literal, and domain terminology needs fixing before downstream prompts can use it.
- Sampling-based decoding makes structured extraction (decisions, assignees, deadlines) non-deterministic and prone to invented details; grounding instructions in the prompt reduce this but don't eliminate it.

## Tools & libraries

- Python
- IBM watsonx.ai (`ibm-watsonx-ai`) — Mistral Medium
- gTTS (Google Text-to-Speech)
- Hugging Face Transformers — OpenAI Whisper (`whisper-tiny.en`, `whisper-medium`)
- LangChain (`langchain-ibm`, LCEL) — IBM Granite 4 (`granite-4-h-small`)
- Gradio
- Jupyter Notebook
