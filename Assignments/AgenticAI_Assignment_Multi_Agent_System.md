# Assignment 5: Autonomous Multi-Agent Tech Buying Assistant

**Module:** Agentic AI — 3-Hour Session  
**Estimated Time:** 2.5 – 3 Hours  
**Difficulty:** Intermediate to Advanced  

---

## 🎯 Objective
Build a specialized **Autonomous Multi-Agent AI System** from scratch using the Google GenAI SDK (`google-genai`) and Gemini models. You will implement a team of AI agents that collaborate through shared memory to recommend the best laptop or gadget for a user's specific budget and workload.

---

## 📌 Problem Scenario
A college engineering student needs to buy a laptop with a strict budget of **₹70,000 (or $900)**. They need it for coding, running local AI models, and casual gaming.
- When asking a regular LLM with one prompt, it gives generic suggestions, hallucinates prices, or recommends laptops well above the budget.
- We need a **Multi-Agent Team** where:
  1. A **Supervisor Agent** breaks the goal into structured sub-tasks.
  2. A **Researcher Agent** searches for laptop models with realistic specs.
  3. A **Budget Analyst Agent** computes exact prices, checks discounts/taxes, and confirms it is within budget.
  4. A **Critic Agent** audits the options for thermal bottlenecks, battery life flaws, or upgrade limitations.
  5. A **Writer Agent** produces a clean, decisive 1-page Buyer's Recommendation Dossier.

---

## 📋 Tasks & Requirements

### Task 1: Single Agent with a Python Tool (Fundamentals)
- Create a Python tool function:
  ```python
  def calculate_discounted_price(mrp: float, discount_percent: float, student_discount_inr: float = 2000.0) -> str:
      """Calculates final out-of-pocket price after store discount and student coupon."""
      discounted = mrp * (1 - (discount_percent / 100))
      final_price = max(0.0, discounted - student_discount_inr)
      return f"Final price after discount: Rs {final_price:.2f}"
  ```
- Pass this tool to Gemini via `types.GenerateContentConfig(tools=[calculate_discounted_price])`.
- Prompt: *"A laptop has an MRP of Rs 75,000 with a 10% instant bank discount. Apply my student coupon and tell me what I will pay."*
- Verify the single agent calls the tool and outputs the exact calculated number.

### Task 2: Multi-Agent Architecture Design
- Define the shared state dictionary connecting all agents:
  ```python
  buyer_state = {
      "user_request": "Engineering student looking for a coding + gaming laptop under Rs 70,000.",
      "plan": "",
      "candidates": "",
      "budget_analysis": "",
      "critique": "",
      "final_recommendation": ""
  }
  ```

### Task 3: Multi-Agent Team Implementation from Scratch
Implement the 4-agent collaboration pipeline sequentially:

1. **Researcher Agent:**
   - Prompt: Research 2 real laptop models (e.g. Acer Nitro, Lenovo LOQ, HP Victus, or Asus Vivobook) with exact processor, RAM, and GPU within the ₹60,000–₹72,000 range.
   - Save findings to `buyer_state["candidates"]`.

2. **Budget Analyst Agent:**
   - Prompt: Analyze the prices of both candidates, calculate remaining money from the ₹70,000 budget for buying a mouse/bag, and state which machine offers better performance-per-rupee.
   - Save analysis to `buyer_state["budget_analysis"]`.

3. **Critic Agent:**
   - Prompt: Review the 2 laptop choices strictly. Highlight potential downsides (e.g., poor battery life, 8GB RAM limitations requiring upgrades, heating issues, or heavy weight).
   - Save critique to `buyer_state["critique"]`.

4. **Writer Agent:**
   - Prompt: Synthesize all agent findings into a crisp, decisive Buyer's Guide:
     - **Top Pick:** Winner model name & why.
     - **Key Specs & Exact Price:** CPU, GPU, RAM, Storage.
     - **Pros & Cons:** Based on Critic's review.
     - **Final Buying Verdict:** Clear step-by-step advice for the student.

---

## 💡 Key Design Rules
- Keep the code linear and clean.
- Do not use bloated third-party frameworks (LangChain, CrewAI, AutoGen) — build the agent orchestration in pure, transparent Python so you understand the raw mechanics.
- Add natural developer comments explaining each agent's role.

---

## 🏆 Submission Deliverables
1. Python script: `assignment_agentic.py`
2. Terminal execution output showing each agent contributing to the shared state and the final generated Buyer's Recommendation Dossier.
