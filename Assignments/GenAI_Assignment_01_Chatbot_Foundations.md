# Assignment 1: E-Commerce Customer Support Chatbot

**Module:** GenAI with Gemini SDK — Session 1  
**Estimated Time:** 1.5 – 2 Hours  
**Difficulty:** Beginner  

---

## 🎯 Objective
Build an interactive, persona-driven customer support bot for an online electronics store ("QuickCart") using the Google GenAI SDK (`google-genai`) with Gemini models.

---

## 📌 Problem Scenario
"QuickCart" is experiencing a surge in holiday shopper inquiries. Customers ask about return policies, track orders, and request product recommendations. The company needs a conversational chatbot that:
1. Greets customers politely and stays strictly within a friendly, professional support agent persona.
2. Streams answers in real time so the user experience feels instantaneous.
3. Remembers context across multiple conversation turns (e.g., customer name, order number, and product issue).
4. Maintains factual consistency without guessing return policies (low temperature).

---

## 📋 Tasks & Requirements

### Task 1: Environment Setup & Single Turn Query
- Load `GEMINI_API_KEY` from `.env`.
- Initialize `genai.Client`.
- Ask a basic question: *"What is QuickCart's standard return window?"* using `client.models.generate_content`.

### Task 2: System Instructions & Temperature Tuning
- Define a system instruction for **"Sam"**, QuickCart's senior customer specialist.
- Tone guidelines: Helpful, concise (under 3 sentences per reply), always ask how else you can help.
- Set `temperature=0.2` and `max_output_tokens=200` using `types.GenerateContentConfig`.
- Ask: *"I bought a wireless mouse 10 days ago, can I return it?"*

### Task 3: Streaming Output
- Use `client.models.generate_content_stream` to stream a 3-step checklist: *"What should I do before sending back an item for return?"*
- Loop over the stream chunks and print them with `flush=True`.

### Task 4: Multi-Turn Conversation Memory
- Use `client.chats.create()` to create an ongoing chat session.
- Simulate or implement an interactive 3-turn dialogue:
  - **Turn 1 (Customer):** *"Hi, my name is Rahul and my order number is QC-8812."*
  - **Turn 2 (Customer):** *"The keyboard I received has a broken spacebar."*
  - **Turn 3 (Customer):** *"Can you summarize my issue and who I am?"*
- Verify that Gemini remembers Rahul's name, order ID, and broken keyboard without repeating the prompt context.

---

## 💡 Key SDK Methods to Use
```python
from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

# Single generation with config
client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config=config)

# Streaming
client.models.generate_content_stream(model="gemini-2.5-flash", contents=prompt)

# Multi-turn chat
chat = client.chats.create(model="gemini-2.5-flash")
chat.send_message("...")
```

---

## 🏆 Submission Deliverables
1. Python script: `assignment_01.py`
2. Terminal output log or markdown summary showing all 4 tasks running successfully.
