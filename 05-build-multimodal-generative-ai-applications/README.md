# Course 5 — Build Multimodal Generative AI Applications

**Coursera course:** [https://www.coursera.org/learn/[course-slug]](https://www.coursera.org/learn/[course-slug])
**Part of:** [IBM RAG and Agentic AI Professional Certificate](../README.md)
**Status:** 🟡 In progress (~50%)

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
- **Result:** [`meeting_minutes_and_tasks.txt`](./labs/lab1/final_project_Modul_1/meeting_minutes_and_tasks.txt)
- **Screenshots:**

  ![Meeting minutes — part 1](<./labs/lab1/final_project_Modul_1/meeting_summary_AUDIO1.png>)

  ![Meeting minutes — part 2 (decisions & tasks)](<./labs/lab1/final_project_Modul_1/meeting_summary_AUDIO1_2.png>)
- **Key learning:** Cleaning up the transcript before summarizing improves the result. With random sampling, the model sometimes invents details (e.g. an assignee nobody named).

### Lab 2 — Image Generation Guide for Beginners

- **Task:** Generate images from text prompts with the OpenAI Images API and compare two models. Includes 2 exercises.
- **Approach:**
  - Generated "a white siamese cat" with a smaller and a larger image model and compared the results.
  - The lab is written for DALL-E 2 and DALL-E 3; I used the current replacements `gpt-image-1-mini` and `gpt-image-1.5`.
  - Exercises: the same comparison for "a beautiful lake with a sunset".
- **Code:** [`labs/lab_2_GPT Image generation Guide for Beginners.ipynb`](<./labs/lab_2_GPT%20Image%20generation%20Guide%20for%20Beginners.ipynb>) (generated images are visible in the notebook)
- **Key learning:** Image generation is a single API call; the prompt and the model choice decide the quality and level of detail.

### Lab 3 — Build an Image Captioning System with IBM watsonx and Llama

- **Task:** Use a vision-language model to describe images and answer questions about them.
- **Approach:**
  - Llama 4 Maverick (`meta-llama/llama-4-maverick-17b-128e-instruct-fp8`) on watsonx.ai via `ModelInference.chat()`.
  - Images are downloaded, base64-encoded and sent together with the text prompt in one chat message.
  - Tested captioning on 4 images plus visual questions: counting cars, rating flood damage, reading sodium from a nutrition label.
  - Exercises: cholesterol from the nutrition label (20 mg) and the color of a jacket (yellow), both answered correctly.
- **Code:** [`labs/lab_3_Build an Image Captioning System with IBM watsonx and Llama.ipynb`](<./labs/lab_3_Build%20an%20Image%20Captioning%20System%20with%20IBM%20watsonx%20and%20Llama.ipynb>)
- **Key learning:** A vision-language model handles captioning, object questions and reading text in images with the same function. Only the question changes.

### Lab 4 — AI Nutrition Coach (Image-Based Web App)

- **Task:** A Flask web app that estimates calories and nutrients from a photo of food.
- **Approach:**
  - The user uploads an image and asks a question; the image is base64-encoded and sent to Llama 4 Maverick on watsonx.ai.
  - A structured prompt asks for food identification, portion size and calories, nutrients, a health evaluation and a disclaimer.
  - The model's Markdown answer is converted to HTML and shown on the page.
  - Tested with a sushi platter (sushi rolls, gyoza, mochi).
- **Code:** [lab instructions incl. solution code](./labs/lab_4_AI_Nutrition_Coach/lab-instructions_AI_Nutrition_Coach.md) · [test image](./labs/lab_4_AI_Nutrition_Coach/image_test-calorie.png)
- **Screenshots:**

  ![AI Nutrition Coach — input](<./labs/lab_4_AI_Nutrition_Coach/image_test_lab_build_GenAI_powered_Image-Based_web_application_AI_Nutrition_Coach.png>)

  ![Result 1 — identification and calories](<./labs/lab_4_AI_Nutrition_Coach/result_1_lab_build_GenAI_powered_Image-Based_web_application_AI_Nutrition_Coach.png>)

  ![Result 2](<./labs/lab_4_AI_Nutrition_Coach/result_2_lab_build_GenAI_powered_Image-Based_web_application_AI_Nutrition_Coach.png>)

  ![Result 3](<./labs/lab_4_AI_Nutrition_Coach/result_3_lab_build_GenAI_powered_Image-Based_web_application_AI_Nutrition_Coach.png>)

  ![Result 4 — health evaluation and disclaimer](<./labs/lab_4_AI_Nutrition_Coach/result_4_lab_build_GenAI_powered_Image-Based_web_application_AI_Nutrition_Coach.png>)
- **Key learning:** The model recognizes the foods reliably, but its counts are rough: it estimated 40 sushi pieces, while the platter clearly holds more. Calorie values from images are estimates, which is why the disclaimer matters.

### Lab 5 — Style Finder: Fashion Analysis with Multimodal RAG

- **Task:** A Gradio app that analyzes an outfit photo and finds matching items with brand, price and shop link.
- **Approach:**
  - **Retrieval:** ResNet50 turns the uploaded image into a vector; cosine similarity finds the closest outfit in a prepared fashion dataset.
  - **Generation:** Llama 4 Maverick describes the clothing items and the style, using the image and the retrieved item data.
  - **Interface:** Gradio app with three example images and an upload field.
- **Code:** [lab instructions incl. solution code](<./labs/lab_5_Fashion_Style_Finder/lab-instructions_Style%20Finder_Computer%20Vision-Based%20Fashion%20Analysis.md>)
- **Screenshots:**

  ![Style Finder — start page](<./labs/lab_5_Fashion_Style_Finder/bild_1_lab_buildaStyleFinderUsing_MM-RAG.png>)

  ![Example 1 — houndstooth outfit](<./labs/lab_5_Fashion_Style_Finder/bild_2_lab_buildaStyleFinderUsing_MM-RAG.png>)

  ![Example 2 — cardigan and shorts](<./labs/lab_5_Fashion_Style_Finder/bild_3_lab_buildaStyleFinderUsing_MM-RAG.png>)

  ![Example 3 — teal top and suede skirt](<./labs/lab_5_Fashion_Style_Finder/bild_4_lab_buildaStyleFinderUsing_MM-RAG.png>)
- **Key learning:** The image description is accurate, but the retrieved items depend entirely on the dataset. Example 3 returned the same items as Example 1 because it matched the same closest outfit. The output also shows small formatting bugs (item list printed twice, `$$` prices).

## Key takeaways

- Chaining single-purpose models (speech-to-text, LLM, text-to-speech) is a simple way to build multimodal apps.
- Speech-to-text output should be cleaned up before an LLM summarizes it.
- For structured outputs like task lists, use low temperature or greedy decoding to avoid invented details.
- Vision-language models take images as base64 inside the chat message; captioning, visual Q&A and reading text all use the same call.
- Estimates from images (counts, calories) are approximate and should be presented as such.
- Multimodal RAG = image embedding + similarity search + LLM generation. Its results can only be as good as the dataset behind it.

## Tools & libraries

- Python, Jupyter Notebook
- IBM watsonx.ai (`ibm-watsonx-ai`) — Mistral Medium, Granite 4, Llama 4 Maverick (vision)
- OpenAI Images API — `gpt-image-1-mini`, `gpt-image-1.5`
- gTTS (Google Text-to-Speech)
- Hugging Face Transformers — OpenAI Whisper (`whisper-tiny.en`, `whisper-medium`)
- LangChain (`langchain-ibm`, LCEL)
- PyTorch / torchvision (ResNet50), scikit-learn (cosine similarity)
- Gradio, Flask
