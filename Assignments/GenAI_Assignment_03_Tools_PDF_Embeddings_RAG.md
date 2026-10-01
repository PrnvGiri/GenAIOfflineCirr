# Assignment 3: HR Policy Q&A with Tools, PDF & Embeddings (RAG)

**Module:** GenAI with Gemini SDK — Session 3  
**Estimated Time:** 2 – 2.5 Hours  
**Difficulty:** Intermediate  

---

## 🎯 Objective
Build a comprehensive Human Resources (HR) Assistant that combines:
1. Python Function Calling (Leave balance & salary calculation tools).
2. Gemini File API (Direct PDF document Q&A).
3. Text Embeddings & Cosine Semantic Vector Retrieval (RAG).
4. Google Search Grounding (Live external salary benchmark checks).

---

## 📌 Problem Scenario
"NexTech Solutions" has a 15-page employee benefits handbook. Employees constantly flood HR with repetitive questions about maternity/paternity leave, work-from-home allowances, and paid time off (PTO). Furthermore, employees want to calculate remaining leave pay or check market benchmarks for their job title.

---

## 📋 Tasks & Requirements

### Task 1: Function Calling (Tool Use)
- Write two standard Python functions:
  ```python
  def get_employee_leave_balance(emp_id: str) -> str:
      """Returns remaining paid time off (PTO) days for an employee ID."""
      # Example database: {"EMP-101": 14, "EMP-202": 5}
      ...

  def calculate_encashment(daily_pay_rate: float, unused_days: int) -> str:
      """Calculates gross salary encashment for unused leaves."""
      ...
  ```
- Ask Gemini: *"Employee EMP-101 has a daily rate of $250. How many leaves do they have remaining, and what is their total encashment amount?"*
- Provide the functions in `tools=[...]` and verify Gemini calls both functions autonomously.

### Task 2: PDF Document Understanding (Gemini File API)
- Upload an employee policy PDF (you can use [`GenAI/samples/sample_policy.pdf`](../GenAI/samples/sample_policy.pdf) or any sample corporate policy PDF).
- Use `client.files.upload(file="...")` to upload the document.
- Ask Gemini a specific question that can only be answered from the PDF text:
  - *"What are the strict rules or deadlines stated in this policy document?"*

### Task 3: Text Embeddings & Semantic Search (RAG)
- Create a list of 4-5 company HR benefit rules:
  1. *"Employees get 20 days paid vacation annually after completing probation."*
  2. *"Health insurance covers dental and vision checkups up to $1,500 per year."*
  3. *"Work from home equipment stipend is $500 one-time for home office setup."*
  4. *"Parental leave is 16 weeks paid for primary caregivers."*
- Convert all rules into vector embeddings using `gemini-embedding-001`.
- Convert an employee query (e.g. *"Can I expense a new monitor and ergonomic desk chair?"*) into a vector embedding.
- Compute cosine similarity with NumPy to retrieve the best matching rule.
- Prompt Gemini using the retrieved context to formulate the final grounded answer.

### Task 4: Live Google Search Grounding
- Ask Gemini to check current market compensation data:
  - *"What is the typical average salary range for an AI Prompt Engineer in the US in 2026?"*
- Enable Google Search tool using `types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())])`.
- Print the live search-grounded response.

---

## 💡 Key SDK Methods to Use
```python
from google.genai import types

# 1. Tools
config = types.GenerateContentConfig(tools=[get_employee_leave_balance, calculate_encashment])

# 2. File Upload
uploaded_pdf = client.files.upload(file="policy.pdf")

# 3. Embeddings
res = client.models.embed_content(model="gemini-embedding-001", contents="text")
vector = res.embeddings[0].values

# 4. Search Grounding
config = types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())])
```

---

## 🏆 Submission Deliverables
1. Python script: `assignment_03.py`
2. Terminal execution output showing:
   - Tool calling math result
   - PDF Q&A answer
   - RAG embedding similarity match & grounded answer
   - Live Google search results
