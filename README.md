# GenAI & Agentic AI — 11-Hour Complete Hands-On Curriculum

A beginner-friendly, production-ready curriculum for mastering the **Google GenAI SDK (`google-genai`)** with Gemini models (`gemini-2.5-flash`), progressing from GenAI foundations to autonomous multi-agent systems.

---

## 📚 Curriculum Overview

This repository is organized into two core modules:

| Module | Duration | Core Focus | Hands-On Project |
| :--- | :--- | :--- | :--- |
| **[`GenAI/`](GenAI/)** | 8 Hours | Gemini SDK, Vision, Structured JSON, Tools, PDF, RAG, Audio | **OmniDesk:** Incident & Claims Processing Hub |
| **[`AgenticAI/`](AgenticAI/)** | 3 Hours | Single Agent, Tool Calling, Multi-Agent Teams, Shared State | **SmartPlanner:** Autonomous Travel & Budget Planner |

---

## 📂 Repository Structure

```text
├── .env.example                       # API key configuration template
├── README.md                          # Master program guide (this file)
│
├── GenAI/                             # MODULE 1: 8-Hour Gemini SDK Curriculum
│   ├── curriculum.txt                 # 8-Hour syllabus breakdown
│   ├── output.md                      # Verified execution outputs for all 4 sessions
│   ├── samples/                       # Test assets
│   │   ├── sample_receipt.png         # Collision repair invoice ($1,537.15)
│   │   ├── sample_policy.pdf          # Auto insurance policy manual
│   │   └── sample_call.wav            # Voice call reporting an incident
│   └── hands_on/
│       ├── check_models.py            # API model audit script
│       ├── 01_chatbot_foundations.py  # Session 1: Text, persona, streaming, chat memory
│       ├── 01_problem_statement.md    # Session 1: Problem statement & architecture
│       ├── 02_multimodal_structured.py# Session 2: Image reading + strict Pydantic JSON
│       ├── 02_problem_statement.md    # Session 2: Problem statement & architecture
│       ├── 03_tools_and_rag.py        # Session 3: Function calling, PDF API, RAG, Search
│       ├── 03_problem_statement.md    # Session 3: Problem statement & architecture
│       ├── 04_advanced_caching_audio.py# Session 4: Audio understanding, safety, caching
│       └── 04_problem_statement.md    # Session 4: Problem statement & architecture
│
└── AgenticAI/                         # MODULE 2: 3-Hour Agentic AI Curriculum
    ├── agenticCirr.txt                # 3-Hour Agentic AI syllabus
    ├── multi_agent_system.py          # Practical multi-agent system from scratch
    ├── problem_statement.md           # Multi-agent problem statement & design
    ├── output.md                      # Verified execution output (Full Travel Plan)
    └── README.md                      # Agentic architecture & design notes
│
└── Assignments/                       # PRACTICE ASSIGNMENTS (GenAI & Agentic AI)
    ├── README.md                      # Assignment index & submission guide
    ├── GenAI_Assignment_01_Chatbot_Foundations.md
    ├── GenAI_Assignment_02_Multimodal_Structured_Output.md
    ├── GenAI_Assignment_03_Tools_PDF_Embeddings_RAG.md
    ├── GenAI_Assignment_04_Audio_Safety_Caching.md
    └── AgenticAI_Assignment_Multi_Agent_System.md
```

---

## 🛠️ Code Style & Design Principles

All code in this repository follows clean, beginner-friendly principles:
* **Linear Execution:** Scripts run from top to bottom without unnecessary function wrappers.
* **Functions Only Where Needed:** Functions are reserved strictly for tool calling or core formulas.
* **Natural Pointer Comments:** Short, direct, one-line comments explaining what each step does.
* **Real-World Use Cases:** Every session solves an immediate, practical problem.

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+
* A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### 2. Install Dependencies
```bash
pip install google-genai python-dotenv pillow pydantic numpy
```

### 3. Setup Your API Key
Copy `.env.example` to `.env` in the project root:
```bash
cp .env.example .env
```
Edit `.env` and add your key:
```ini
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 🧪 Running the Hands-On Labs

### Module 1: GenAI with Gemini SDK (`GenAI/`)
```bash
# Verify API connection & check available models
python3 GenAI/hands_on/check_models.py

# Session 1: Chatbot Foundations (Text, Persona, Streaming, Chat)
python3 GenAI/hands_on/01_chatbot_foundations.py

# Session 2: Multimodal AI & Strict Pydantic JSON Extraction
python3 GenAI/hands_on/02_multimodal_structured.py

# Session 3: Function Calling Tools, PDF File API, Embeddings RAG & Search
python3 GenAI/hands_on/03_tools_and_rag.py

# Session 4: Voice Call Audio Ingestion, Safety Settings & Context Caching
python3 GenAI/hands_on/04_advanced_caching_audio.py
```

### Module 2: Agentic AI (`AgenticAI/`)
```bash
# Run the Autonomous Travel & Budget Planner Agent Team
python3 AgenticAI/multi_agent_system.py
```

---

## 📄 Verified Outputs

All scripts have been executed and their verified outputs are saved in:
* **[`GenAI/output.md`](GenAI/output.md)** — Verified outputs for Sessions 1 through 4.
* **[`AgenticAI/output.md`](AgenticAI/output.md)** — Verified multi-agent output (Trip schedule, expense calculations, and recommendations).
