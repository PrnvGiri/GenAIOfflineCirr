# agentic ai: smart travel & budget planner
# simple multi-agent system from scratch using gemini
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# load api key from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
api_key = os.getenv("GEMINI_API_KEY", "").strip()

# connect to gemini client
client = genai.Client(api_key=api_key)
MODEL = "gemini-2.5-flash"


# =============================================================
# PART 1: SINGLE AGENT WITH A PYTHON TOOL
# =============================================================
print("\n--- Part 1: Single Agent with a Tool ---")

# tool to calculate per-person cost
def split_budget(total_amount: float, people: int) -> str:
    """Calculates per person cost for a trip budget."""
    if people <= 0:
        return "Number of people must be at least 1."
    cost_per_head = total_amount / people
    return f"Budget per person is Rs {cost_per_head:.2f}"

query = "We have a total budget of Rs 30,000 for 3 friends traveling to Goa. Calculate per person share."
print("User asked:", query)

# give the tool to gemini so it calls it automatically
response = client.models.generate_content(
    model=MODEL,
    contents=query,
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful travel planner assistant. Use provided tools when needed.",
        tools=[split_budget]
    )
)
print("Agent reply:", response.text.strip())


# pause to keep free tier safe
time.sleep(3)


# =============================================================
# PART 2: MULTI-AGENT TEAM (SUPERVISOR -> RESEARCHER -> BUDGET -> WRITER)
# =============================================================
print("\n--- Part 2: Multi-Agent Travel Planner ---")

user_request = "Plan a 2-day weekend trip to Goa for 2 friends with a total budget of Rs 20,000."
print(f"Goal: {user_request}\n")

# shared notebook memory between all agents
trip_data = {
    "places": "",
    "expenses": "",
    "itinerary": ""
}


# 1. RESEARCHER AGENT: finds best places and hotels
print("-> [Researcher Agent] Finding top places and budget stay...")
researcher_prompt = (
    f"User wants: '{user_request}'. "
    f"Recommend 3 must-visit places in North Goa and 1 clean budget hotel with estimated room rate per night."
)
res = client.models.generate_content(model=MODEL, contents=researcher_prompt)
trip_data["places"] = res.text.strip()
print("Places & Stay Found:\n", trip_data["places"])

time.sleep(3)


# 2. BUDGET AGENT: breaks down costs for 2 people
print("\n-> [Budget Agent] Calculating estimated expenses...")
budget_prompt = (
    f"Budget limit: Rs 20,000 for 2 people.\n"
    f"Review these places and stay:\n{trip_data['places']}\n\n"
    f"Provide a realistic rough cost breakdown in Indian Rupees for: "
    f"1. Stay (1 night), 2. Food (2 days), 3. Local Scooty rental + petrol, 4. Entry/Activities. "
    f"Confirm if total stays under Rs 20,000."
)
res = client.models.generate_content(model=MODEL, contents=budget_prompt)
trip_data["expenses"] = res.text.strip()
print("Cost Breakdown:\n", trip_data["expenses"])

time.sleep(3)


# 3. WRITER AGENT: creates the final clean 2-day plan
print("\n-> [Writer Agent] Making final easy 2-day itinerary...")
writer_prompt = (
    f"Goal: {user_request}\n\n"
    f"Places: {trip_data['places']}\n\n"
    f"Cost: {trip_data['expenses']}\n\n"
    f"Write a crisp, practical travel plan with:\n"
    f"- Day 1 Schedule (Morning, Afternoon, Evening)\n"
    f"- Day 2 Schedule (Morning, Afternoon, Evening)\n"
    f"- Total Cost Summary & 1 Pro-tip for saving money."
)
res = client.models.generate_content(model=MODEL, contents=writer_prompt)
trip_data["itinerary"] = res.text.strip()

print("\n" + "=" * 60)
print("FINAL RESULT: YOUR 2-DAY GOA TRIP PLAN")
print("=" * 60)
print(trip_data["itinerary"])
