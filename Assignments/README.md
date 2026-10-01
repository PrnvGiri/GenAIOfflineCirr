# Course Assignments Directory

Welcome to the hands-on assignment portal for the **11-Hour GenAI & Agentic AI Curriculum**. These assignments challenge learners to build practical, production-grade applications using the **Google GenAI SDK (`google-genai`)** with Gemini models (`gemini-2.5-flash`).

---

## 📋 Assignment Index

| # | Assignment Document | Module | Key Skills Tested |
| :--- | :--- | :--- | :--- |
| **01** | [`GenAI_Assignment_01_Chatbot_Foundations.md`](GenAI_Assignment_01_Chatbot_Foundations.md) | **GenAI — Session 1** | System Instructions, Temperature control, Streaming responses, Multi-turn Chat memory. |
| **02** | [`GenAI_Assignment_02_Multimodal_Structured_Output.md`](GenAI_Assignment_02_Multimodal_Structured_Output.md) | **GenAI — Session 2** | Image understanding with Gemini Vision, strict Pydantic schemas, `application/json` enforcement. |
| **03** | [`GenAI_Assignment_03_Tools_PDF_Embeddings_RAG.md`](GenAI_Assignment_03_Tools_PDF_Embeddings_RAG.md) | **GenAI — Session 3** | Python Tool Calling, PDF document understanding (File API), text embeddings vector RAG, Google Search grounding. |
| **04** | [`GenAI_Assignment_04_Audio_Safety_Caching.md`](GenAI_Assignment_04_Audio_Safety_Caching.md) | **GenAI — Session 4** | Voice call audio understanding, enterprise safety filters, Context Caching architecture, End-to-End claims pipeline. |
| **05** | [`AgenticAI_Assignment_Multi_Agent_System.md`](AgenticAI_Assignment_Multi_Agent_System.md) | **Agentic AI — 3 Hours** | Single Agent with tools, Supervisor Agent, Specialized workers (Researcher, Analyst, Critic), Shared state, Multi-Agent Dossier synthesis. |

---

## 🛠️ General Submission Guidelines

1. **Environment:**
   * Ensure your `.env` file contains a valid `GEMINI_API_KEY`.
   * Recommended model: `gemini-2.5-flash` for all tasks (and `gemini-embedding-001` for vector embeddings).

2. **Code Philosophy:**
   * Write clean, linear code from top to bottom.
   * Only write functions when necessary (e.g. for tools or mathematical formulas).
   * Include natural one-line pointer comments explaining what each step does.

3. **Deliverables:**
   * Submit the standalone Python script (`.py`) for each assignment.
   * Provide a markdown file (`.md`) or terminal log showing the verified execution output.
