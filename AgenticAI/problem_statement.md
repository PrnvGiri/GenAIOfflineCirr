# Problem Statement: Autonomous Multi-Agent Smart Travel & Budget Planner

## 1. Real-World Context
Planning a trip involves multiple distinct cognitive tasks:
1. Finding places to visit and hotel options within a budget.
2. Calculating exact costs (stay, food, local transport, activities) and checking if they fit within a financial ceiling.
3. Assembling a structured Day-by-Day schedule and identifying practical travel tips.

A single general-purpose prompt sent to an LLM often produces generic, unbalanced recommendations where the budget math does not add up, or hotel prices are unrealistic.

## 2. Core Problem to Solve
- **Why a Single Agent Falls Short:** A single agent trying to research, do math, verify constraints, and write schedules all at once often loses focus, hallucinates numbers, or ignores budget limits.
- **The Agentic AI Solution:** Build a specialized **Multi-Agent Team** where each agent has one specific role, uses specialized tools, and shares findings through a central state.

## 3. What the Code Implements (`multi_agent_system.py`)

### Part 1: Single Agent with Tools
- Demonstrates how a single agent connects to a Python calculator tool (`split_budget`) to compute exact per-person costs without mathematical guessing.

### Part 2: Autonomous Multi-Agent Team Collaboration
- **User Goal:** *"Plan a 2-day weekend trip to Goa for 2 friends with a total budget of Rs 20,000."*
- **Researcher Agent:** Identifies top must-visit locations (Vagator, Chapora Fort, Baga/Calangute) and finds clean budget accommodations (~Rs 2,000/night).
- **Budget Agent (Analyst):** Calculates itemized expenses in Indian Rupees (Stay: Rs 4,000 + Food: Rs 4,000 + Scooty/Petrol: Rs 1,300 + Activities: Rs 1,000 = Rs 10,300) and confirms a healthy buffer of Rs 9,700 remaining.
- **Writer Agent:** Synthesizes the research and financial numbers into an actionable, clean 2-day schedule (Morning, Afternoon, Evening) complete with money-saving pro-tips.

## 4. Expected Output
A complete, practical, ready-to-use 2-day travel itinerary with verified budget calculations, delivered autonomously through multi-agent collaboration.
