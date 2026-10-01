# Agentic AI — 3-Hour Hands-On Session

This module covers the complete 3-hour Agentic AI journey as specified in [`agenticCirr.txt`](agenticCirr.txt):

1. **Fundamentals (0:00–0:30):** What makes an application agentic, model vs tool vs memory vs decision loop, and single tool-using agents.
2. **From Single to Multi-Agent (0:30–1:00):** Agent specialization, communication, and supervisor routing.
3. **Multi-Agent Architecture (1:00–1:30):** System design with Supervisor $\to$ [Researcher, Analyst, Critic] $\to$ Writer.
4. **Complete Multi-Agent System (1:30–3:00):** Hands-on implementation from scratch producing an executive research briefing.

---

## 🏗️ Architecture

```text
                    USER QUERY
                        │
               ┌─────────────────┐
               │ Supervisor Agent│ (Plans & coordinates)
               └────────┬────────┘
                        │
            ┌───────────┼───────────┐
            ↓           ↓           ↓
       Researcher  Data Analyst   Critic
         Agent        Agent       Agent
       (Gathers)   (Computes)   (Reviews)
            │           │           │
            └───────────┼───────────┘
                        ↓
                  Writer Agent  (Compiles Final Report)
                        ↓
                  FINAL DELIVERABLE
```

---

## 📂 Files in this Module

* [`agenticCirr.txt`](agenticCirr.txt) — 3-hour Agentic AI Curriculum syllabus
* [`multi_agent_system.py`](multi_agent_system.py) — Complete, linear, beginner-friendly hands-on implementation from scratch
* [`output.md`](output.md) — Verified execution outputs including the generated Multi-Agent Executive Briefing

---

## 🚀 How to Run

From the project root:
```bash
python3 AgenticAI/multi_agent_system.py
```
