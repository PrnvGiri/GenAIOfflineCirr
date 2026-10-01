# Agentic AI — Smart Travel & Budget Planner

A beginner-friendly, practical multi-agent AI system built using the **Google GenAI SDK (`google-genai`)** and **Gemini 2.5 Flash**.

---

## 💡 What This System Does

Users give a plain English goal:
> *"Plan a 2-day weekend trip to Goa for 2 friends with a total budget of Rs 20,000."*

A specialized team of AI agents collaborates autonomously:
1. **Single Agent with Tools:** Shows how 1 agent calls a Python calculator tool (`split_budget`) to compute per-person shares.
2. **Researcher Agent:** Identifies top must-visit places and clean budget accommodations.
3. **Budget Agent:** Quantifies realistic costs in Indian Rupees (Stay, Food, Scooty rental, Petrol, Activities) and validates against the budget limit.
4. **Writer Agent:** Assembles a ready-to-use 2-day schedule (Day 1 & Day 2) with budget breakdown and money-saving pro-tips.

---

## 🏗️ Architecture

```text
               USER REQUEST ("Goa trip for 2, budget Rs 20,000")
                                 │
                                 ▼
                     [ Researcher Agent ]
             (Finds top places & verified budget stay)
                                 │
                                 ▼
                      [ Budget Agent ]
          (Calculates stay + food + scooty + activities)
                                 │
                                 ▼
                      [ Writer Agent ]
               (Builds crisp 2-day itinerary)
                                 │
                                 ▼
                  READY-TO-USE TRAVEL ITINERARY
```

---

## 🚀 Running the Script

```bash
python3 AgenticAI/multi_agent_system.py
```

All verified execution outputs are recorded in [`AgenticAI/output.md`](output.md).
