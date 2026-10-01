# Problem Statement: Policy Document Q&A (RAG) & Autonomous Tool Execution

## 1. Business Context
Insurance policies are long, complex legal documents (often 30+ pages). When customers or claims adjusters ask questions (e.g., *"What is my reporting deadline?"* or *"Are OEM parts covered for my car?"*), finding the exact clause takes time. Furthermore, calculating the actual approved reimbursement requires looking up internal deductible databases and doing math, which standard LLMs cannot do reliably on their own.

## 2. Core Problem to Solve
- **Hallucinations & Outdated Knowledge:** An LLM without access to the actual policy document will guess answers.
- **Accurate Math & Database Lookups:** LLMs are language predictors, not calculators or databases. They must be able to call Python tools to fetch real data and calculate numbers accurately.
- **External Real-Time Verification:** When validating repair costs, the system must check current real-world market prices.

## 3. What the Code Implements (`03_tools_and_rag.py`)
1. **Function Calling:** Connects two Python tools (`get_deductible` and `calculate_payout`). Gemini autonomously identifies when to call them and returns the exact net payout: `$1,537.15 - $500 = $1,037.15`.
2. **PDF File API:** Uploads [`samples/sample_policy.pdf`](../samples/sample_policy.pdf) directly to Gemini File API and answers questions directly from the multi-page legal document (e.g. 72-hour filing deadline).
3. **Embeddings & Vector Search (RAG):**
   - Converts policy rules into vector numbers using `gemini-embedding-001`.
   - Converts the user's question into a vector and calculates cosine similarity.
   - Retrieves the most relevant rule (OEM parts coverage for cars under 4 years old) and answers the question grounded in that fact.
4. **Google Search Grounding:** Uses `types.Tool(google_search=...)` to check current real-world replacement costs for Honda Civic LED headlights.

## 4. Expected Output
A grounded claims engine that never guesses: it queries policy PDFs, searches vector databases, executes calculation tools, and cross-checks market prices live on Google.
