# GenAI Offline Curriculum & Hands-On Labs

This repository provides an 8-hour hands-on curriculum for mastering the **Google GenAI SDK (`google-genai`)** with Gemini models (`gemini-2.5-flash`), organized around an end-to-end incident and insurance claims automation hub.

---

## 📚 Curriculum Breakdown

Refer to [`curriculum.txt`](curriculum.txt) for the full 8-hour syllabus:
* **Session 1: Gemini SDK & GenAI Foundations (2.5h)** — Basic text generation, system instructions, generation config (temperature), streaming responses, and multi-turn chat memory.
* **Session 2: Multimodal AI & Structured Generation (2.5h)** — Image understanding with Gemini Vision and Pydantic schema-driven JSON extraction.
* **Session 3: Function Calling, Documents, Embeddings & RAG (2.5h)** — Python tool calling, PDF understanding via Gemini File API, vector embeddings with `gemini-embedding-001`, semantic search RAG, and live Google Search grounding.
* **Session 4: Advanced Gemini & Mini Project (30m)** — Voice call audio understanding, safety filter configuration, Context Caching architecture, and end-to-end automated claims pipeline.

---

## 📂 Repository Structure

```text
├── curriculum.txt                 # The 8-hour syllabus
├── output.md                      # Verified execution outputs from all hands-on scripts
├── .env.example                   # Environment variable template
├── hands_on/
│   ├── check_models.py            # Verify API connection and inspect available models
│   ├── 01_chatbot_foundations.py  # Session 1: Text, persona, streaming, chat
│   ├── 02_multimodal_structured.py# Session 2: Image reading + strict Pydantic JSON
│   ├── 03_tools_and_rag.py        # Session 3: Function calling, PDF API, RAG, Search
│   └── 04_advanced_caching_audio.py# Session 4: Audio understanding, safety, caching
└── samples/
    ├── sample_receipt.png         # Mechanic repair estimate ($1,537.15)
    ├── sample_policy.pdf          # Auto policy terms & conditions document
    └── sample_call.wav            # Spoken customer phone call recording
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+
* A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### 2. Install Dependencies
```bash
pip install google-genai python-dotenv pillow pydantic numpy
```

### 3. Setup Environment
Copy the `.env.example` file to `.env` and add your API key:
```bash
cp .env.example .env
```
Edit `.env`:
```ini
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### 4. Run the Labs
Run any session script directly:
```bash
# Verify models
python3 hands_on/check_models.py

# Session 1: Chatbot Foundations
python3 hands_on/01_chatbot_foundations.py

# Session 2: Multimodal & Structured Output
python3 hands_on/02_multimodal_structured.py

# Session 3: Tools, PDF, Embeddings & RAG
python3 hands_on/03_tools_and_rag.py

# Session 4: Audio & Advanced Features
python3 hands_on/04_advanced_caching_audio.py
```

All verified execution outputs are documented in [`output.md`](output.md).
