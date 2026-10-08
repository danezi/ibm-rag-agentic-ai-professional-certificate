# Course 5 — Build Multimodal Generative AI Applications

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟡 In progress (~10%)

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

## Key takeaways

- Chaining single-modality models (LLM → TTS) is the simplest way to build a multimodal experience; the text output of one step is the input of the next.
- LLM output destined for speech should be cleaned of Markdown formatting first — TTS engines read symbols and structure literally.

## Tools & libraries

- Python
- IBM watsonx.ai (`ibm-watsonx-ai`) — Mistral Medium
- gTTS (Google Text-to-Speech)
- Jupyter Notebook
