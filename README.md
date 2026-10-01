# Complete 11-Hour GenAI & Agentic AI Curriculum

This repository contains the complete 11-hour hands-on curriculum:
1. **GenAI with Gemini SDK (8 Hours)** in [`GenAI/`](GenAI/)
2. **Autonomous Multi-Agent AI (3 Hours)** in [`AgenticAI/`](AgenticAI/)

---

## 📂 Repository Structure

```text
├── .env.example                       # API key configuration template
├── README.md                          # Repository overview & quickstart
│
├── GenAI/                             # MODULE 1: 8-Hour Gemini SDK Curriculum
│   ├── curriculum.txt                 # 8-hour syllabus breakdown
│   ├── output.md                      # Verified execution outputs
│   ├── samples/                       # Test assets (receipt image, policy PDF, audio call)
│   │   ├── sample_receipt.png
│   │   ├── sample_policy.pdf
│   │   └── sample_call.wav
│   └── hands_on/
│       ├── check_models.py            # API model audit script
│       ├── 01_chatbot_foundations.py  # Session 1: Text, persona, streaming, chat
│       ├── 02_multimodal_structured.py# Session 2: Image reading + strict Pydantic JSON
│       ├── 03_tools_and_rag.py        # Session 3: Function calling, PDF, RAG, Search
│       └── 04_advanced_caching_audio.py# Session 4: Audio understanding, safety, caching
│
└── AgenticAI/                         # MODULE 2: 3-Hour Agentic AI Curriculum
    ├── agenticCirr.txt                # 3-hour Agentic AI syllabus
    ├── multi_agent_system.py          # Complete multi-agent implementation from scratch
    ├── output.md                      # Verified multi-agent report execution output
    └── README.md                      # Architecture diagram and design notes
```

---

## 🚀 Quickstart

### 1. Install Dependencies
```bash
pip install google-genai python-dotenv pillow pydantic numpy
```

### 2. Configure API Key
Create a `.env` file in the project root:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Run GenAI Labs (Module 1)
```bash
python3 GenAI/hands_on/check_models.py
python3 GenAI/hands_on/01_chatbot_foundations.py
python3 GenAI/hands_on/02_multimodal_structured.py
python3 GenAI/hands_on/03_tools_and_rag.py
python3 GenAI/hands_on/04_advanced_caching_audio.py
```

### 4. Run Agentic AI System (Module 2)
```bash
python3 AgenticAI/multi_agent_system.py
```
