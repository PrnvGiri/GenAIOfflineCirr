# agentic ai: complete 3-hour hands-on session
# covers single agent, tools, supervisor router, and multi-agent system from scratch
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# load api key from .env file in parent or current directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
api_key = os.getenv("GEMINI_API_KEY", "").strip()

# connect to gemini client
client = genai.Client(api_key=api_key)
MODEL = "gemini-2.5-flash"


# ============================================================================
# PART 1: SINGLE AGENT WITH TOOLS (0:00 - 0:30)
# ============================================================================
print("\n" + "=" * 60)
print("PART 1: SINGLE TOOL-USING AGENT")
print("=" * 60)

# tool function for stock and financial data lookup
def get_company_revenue(company: str) -> str:
    """Returns annual revenue for a given tech company."""
    data = {
        "google": "$307 Billion in FY2023",
        "microsoft": "$211 Billion in FY2023",
        "apple": "$383 Billion in FY2023",
        "nvidia": "$60 Billion in FY2023"
    }
    key = company.lower().strip()
    return data.get(key, f"Revenue data for {company} not found.")

# tool function for profit margin calculation
def calculate_margin(revenue_billion: float, net_income_billion: float) -> str:
    """Calculates net profit margin percentage."""
    if revenue_billion <= 0:
        return "Invalid revenue."
    margin = (net_income_billion / revenue_billion) * 100
    return f"Profit margin is {margin:.2f}%"

# user query requiring autonomous tool calling
single_agent_query = (
    "What was Google's revenue, and if their net income was 73 billion, "
    "what is their profit margin?"
)
print("User asked:", single_agent_query)

# pass python tools to model so it decides what to call
single_agent_config = types.GenerateContentConfig(
    system_instruction="You are a financial research agent. Use provided tools to fetch facts and calculate numbers.",
    tools=[get_company_revenue, calculate_margin],
    temperature=0.1
)

single_agent_res = client.models.generate_content(
    model=MODEL,
    contents=single_agent_query,
    config=single_agent_config
)
print("\nSingle Agent Final Reply:\n", single_agent_res.text.strip())


# pause to keep free tier rate limits safe
time.sleep(5)


# ============================================================================
# PART 2 & 3: MULTI-AGENT ARCHITECTURE & WORKFLOW (0:30 - 1:30)
# ============================================================================
print("\n" + "=" * 60)
print("PART 2 & 3: MULTI-AGENT SYSTEM ARCHITECTURE")
print("=" * 60)
print(
    "Architecture:\n"
    "  User Query\n"
    "      |\n"
    "  [Supervisor Agent] -> Plans & assigns tasks\n"
    "      |\n"
    "  +---+--------------------+-------------------+\n"
    "  |                        |                   |\n"
    "  v                        v                   v\n"
    " [Researcher Agent]   [Data Analyst Agent]   [Critic Agent]\n"
    "  (Finds facts)        (Analyzes numbers)     (Reviews quality)\n"
    "  +---+--------------------+-------------------+\n"
    "      |\n"
    "  [Writer Agent] -> Compiles final executive report\n"
)


# ============================================================================
# PART 4: FULL MULTI-AGENT IMPLEMENTATION FROM SCRATCH (1:30 - 3:00)
# ============================================================================
print("=" * 60)
print("PART 4: RUNNING THE MULTI-AGENT RESEARCH & REPORT SYSTEM")
print("=" * 60)

# target problem query for multi-agent system
user_goal = "Analyze the growth of Electric Vehicles (EV) market from 2020 to 2025 and predict 2026 outlook."
print(f"Goal: {user_goal}\n")

# shared state dictionary across all agents
shared_state = {
    "query": user_goal,
    "plan": "",
    "research": "",
    "analysis": "",
    "critique": "",
    "final_report": ""
}


# --- STEP 1: SUPERVISOR AGENT ---
# supervisor breaks user goal into clear tasks
print("-> [Supervisor Agent] Planning the workflow...")
supervisor_prompt = (
    f"You are the Supervisor Agent. Break down this research goal into 3 clear tasks "
    f"for Researcher, Data Analyst, and Critic: '{user_goal}'. "
    f"Keep it concise in 3 bullet points."
)
supervisor_res = client.models.generate_content(model=MODEL, contents=supervisor_prompt)
shared_state["plan"] = supervisor_res.text.strip()
print("Supervisor Plan:\n", shared_state["plan"])

time.sleep(4)


# --- STEP 2: RESEARCHER AGENT ---
# researcher agent gathers factual industry points
print("\n-> [Researcher Agent] Gathering market facts...")
researcher_prompt = (
    f"You are a Senior Industry Researcher. Based on the plan:\n{shared_state['plan']}\n\n"
    f"Provide 4 key factual data points on global EV sales volume, battery cost trends, "
    f"and charging infrastructure between 2020 and 2025."
)
researcher_res = client.models.generate_content(model=MODEL, contents=researcher_prompt)
shared_state["research"] = researcher_res.text.strip()
print("Research Findings:\n", shared_state["research"])

time.sleep(4)


# --- STEP 3: DATA ANALYST AGENT ---
# analyst agent extracts numbers, calculates growth, and spots trends
print("\n-> [Data Analyst Agent] Performing quantitative analysis...")
analyst_prompt = (
    f"You are a Quantitative Data Analyst. Review these research notes:\n{shared_state['research']}\n\n"
    f"Calculate or estimate the compound annual growth rate (CAGR), identify the top risk factor, "
    f"and give a projected percentage increase for 2026."
)
analyst_res = client.models.generate_content(model=MODEL, contents=analyst_prompt)
shared_state["analysis"] = analyst_res.text.strip()
print("Analyst Output:\n", shared_state["analysis"])

time.sleep(4)


# --- STEP 4: CRITIC AGENT ---
# critic agent checks for gaps, missing perspectives, or optimism bias
print("\n-> [Critic Agent] Reviewing findings and finding gaps...")
critic_prompt = (
    f"You are a Strict Reviewer and Critic. Review the research and analysis below:\n"
    f"Research:\n{shared_state['research']}\n\n"
    f"Analysis:\n{shared_state['analysis']}\n\n"
    f"Point out 2 critical blindspots, supply chain risks, or regulatory hurdles that were missed."
)
critic_res = client.models.generate_content(model=MODEL, contents=critic_prompt)
shared_state["critique"] = critic_res.text.strip()
print("Critique:\n", shared_state["critique"])

time.sleep(4)


# --- STEP 5: WRITER AGENT ---
# writer agent synthesizes everything into a polished final executive briefing
print("\n-> [Writer Agent] Generating final comprehensive report...")
writer_prompt = (
    f"You are the Executive Report Writer. Synthesize the findings into a polished, professional report.\n\n"
    f"Original Query: {shared_state['query']}\n\n"
    f"Research Findings:\n{shared_state['research']}\n\n"
    f"Data Analysis:\n{shared_state['analysis']}\n\n"
    f"Critic Review:\n{shared_state['critique']}\n\n"
    f"Structure the report with:\n"
    f"1. Executive Summary\n"
    f"2. Key Growth Metrics & Trends\n"
    f"3. Risk Factors & Blindspots\n"
    f"4. 2026 Outlook & Recommendations"
)
writer_res = client.models.generate_content(model=MODEL, contents=writer_prompt)
shared_state["final_report"] = writer_res.text.strip()

print("\n" + "=" * 60)
print("FINAL DELIVERABLE: MULTI-AGENT EXECUTIVE REPORT")
print("=" * 60)
print(shared_state["final_report"])
