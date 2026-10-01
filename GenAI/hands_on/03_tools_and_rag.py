# session 3: function calling tools, pdf upload, embeddings and rag
import os
import time
import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types

# load api key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "").strip()

# connect to gemini client
client = genai.Client(api_key=api_key)

# using 2.5 flash
MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "gemini-embedding-001"


# -------------------------------------------------------------
# 1. FUNCTION CALLING (functions are required here so gemini can call them)
# -------------------------------------------------------------
print("\n1. Function calling with Python tools:")

# tool 1: get deductible from policy
def get_deductible(policy_number: str) -> str:
    """Returns deductible amount for a given policy number."""
    if "99214" in policy_number:
        return "Deductible for POL-99214 is $500."
    return "Policy not found."

# tool 2: calculate payout
def calculate_payout(bill_amount: float, deductible: float) -> str:
    """Calculates final payout after subtracting deductible from bill."""
    payout = max(0.0, bill_amount - deductible)
    return f"Calculated net payout to customer is ${payout:.2f}"

question = (
    "Sarah has policy POL-99214 and the repair bill is $1537.15. "
    "Find her deductible and calculate her net payout."
)
print("User query:", question)

# pass functions directly into tools parameter
config = types.GenerateContentConfig(
    tools=[get_deductible, calculate_payout]
)
response = client.models.generate_content(
    model=MODEL,
    contents=question,
    config=config
)
print("\nGemini final response:\n", response.text.strip())


# pause to avoid free tier rate limit
time.sleep(10)


# -------------------------------------------------------------
# 2. PDF READING (GEMINI FILE API)
# -------------------------------------------------------------
print("\n2. Reading PDF document using Gemini File API:")
pdf_path = "samples/sample_policy.pdf"

# upload pdf to gemini temporary storage
print(f"Uploading {pdf_path} to Gemini...")
pdf_file = client.files.upload(file=pdf_path)

# ask question directly on uploaded pdf
prompt = "According to this policy document, within how many hours must an accident be reported?"
response = client.models.generate_content(
    model=MODEL,
    contents=[pdf_file, prompt]
)
print("Answer from PDF:\n", response.text.strip())


# pause to avoid free tier rate limit
time.sleep(10)


# -------------------------------------------------------------
# 3. TEXT EMBEDDINGS & RAG
# -------------------------------------------------------------
print("\n3. Embeddings and basic RAG:")

# sample policy rules stored locally
rules = [
    "Standard collision deductible is $500 per incident.",
    "Incidents must be reported within 72 hours.",
    "OEM parts are covered for vehicles under 4 years old.",
    "Commercial delivery and rideshare use are not covered."
]

# convert all rules into vector numbers
rule_vectors = []
for r in rules:
    res = client.models.embed_content(model=EMBEDDING_MODEL, contents=r)
    rule_vectors.append(res.embeddings[0].values)

# convert user question into a vector number
question = "Will insurance pay for original OEM parts for a 2024 model car?"
q_res = client.models.embed_content(model=EMBEDDING_MODEL, contents=question)
q_vector = q_res.embeddings[0].values

# helper function to calculate similarity between two vectors
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# compare question vector with each rule vector to find closest match
similarity_scores = [cosine_similarity(q_vector, vec) for vec in rule_vectors]
best_match_idx = int(np.argmax(similarity_scores))
selected_rule = rules[best_match_idx]

print(f"User asked: '{question}'")
print(f"Best matched rule: '{selected_rule}'")

# feed selected rule as context to gemini to answer
rag_prompt = f"Using this rule: '{selected_rule}', answer the question: {question}"
ans = client.models.generate_content(model=MODEL, contents=rag_prompt)
print("RAG answer:\n", ans.text.strip())


# pause to avoid free tier rate limit
time.sleep(10)


# -------------------------------------------------------------
# 4. LIVE GOOGLE SEARCH GROUNDING
# -------------------------------------------------------------
print("\n4. Live Google Search Grounding:")
query = "What is the price range of Honda Civic LED headlight replacement in the US?"

# enable google search tool so model gives current web data
config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)
response = client.models.generate_content(
    model=MODEL,
    contents=query,
    config=config
)
print("Google grounded answer:\n", response.text.strip())
