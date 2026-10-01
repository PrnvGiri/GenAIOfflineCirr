# Gemini SDK Hands-On Execution Outputs

This document contains the verified terminal execution outputs for all simplified, linear hands-on scripts mapped to [`curriculum.txt`](curriculum.txt). All code executes top-to-bottom without unnecessary function wrappers.

---

## 1. Model Availability & Verification (`check_models.py`)

**Command:**
```bash
python3 hands_on/check_models.py
```

**Output:**
```text
Fetching models from Gemini API...

Main models you can use:
- gemini-2.5-flash (recommended for chat, vision, tools)
- gemini-2.5-pro (recommended for chat, vision, tools)
- gemini-embedding-001 (for text embeddings and rag)
- gemini-embedding-2 (for text embeddings and rag)
```

---

## 2. Session 1: Gemini Basics & Chatbot (`01_chatbot_foundations.py`)

**Command:**
```bash
python3 hands_on/01_chatbot_foundations.py
```

**Output:**
```text
1. Basic text generation:
Answer: A car insurance deductible is the amount you pay out of your own pocket before your insurer pays on a covered claim.

2. System instructions and temperature:
Agent reply: Oh no, a scratch can be quite frustrating! For minor surface scratches, you might try a scratch repair kit, but deeper ones often benefit from professional assessment.

3. Streaming output word by word:
Here are 3 quick tips to do immediately after a car accident:

1.  Ensure Safety & Check for Injuries: Move to a safe location if possible (e.g., shoulder of the road) and immediately check yourself and any passengers for injuries. If anyone is hurt, call for medical help. Turn on your hazard lights.
2.  Call 911 & Document Everything: Report the accident to the police, even if it seems minor. While waiting, take photos/videos of the scene, vehicle damage, license plates, and obtain the other driver's contact and insurance information.
3.  Don't Admit Fault & Seek Medical Advice: Do not apologize or admit fault, even casually; stick to the facts when speaking with police. Also, seek medical attention promptly, even if you feel fine, as some injuries have delayed symptoms.

4. Multi-turn chat with memory:
User: Hi, my name is Sarah.
Bot: Hi Sarah! It's nice to meet you. How can I help you today?

User: Do you remember my name?
Bot: Yes, I do! You just told me your name is Sarah. It's good to keep track of who I'm talking to.
```

---

## 3. Session 2: Multimodal AI & Structured JSON (`02_multimodal_structured.py`)

**Command:**
```bash
python3 hands_on/02_multimodal_structured.py
```

**Output:**
```text
1. Reading image with Gemini Vision:
Gemini reply:
This is an auto repair estimate/invoice.
The grand total is $1,537.15.

2. Extracting structured JSON data from image:
Raw JSON received:
{
  "shop_name": "APEX AUTO COLLISION REPAIR & SERVICE",
  "invoice_number": "INV-2026-8812",
  "customer_name": "Sarah Jenkins",
  "total_amount": 1537.15,
  "repaired_parts": [
    "Front Bumper Replacement (OEM Part)",
    "Right Headlight Assembly LED",
    "Bumper Paint & Primer Labor",
    "Structural Frame Realignment",
    "Diagnostic Scan & Sensor Calibration"
  ]
}

Reading fields in python code:
- Shop: APEX AUTO COLLISION REPAIR & SERVICE
- Invoice No: INV-2026-8812
- Customer: Sarah Jenkins
- Total Bill: $1537.15
- Repaired Items: Front Bumper Replacement (OEM Part), Right Headlight Assembly LED, Bumper Paint & Primer Labor, Structural Frame Realignment, Diagnostic Scan & Sensor Calibration
```

---

## 4. Session 3: Function Calling, PDF, Embeddings & RAG (`03_tools_and_rag.py`)

**Command:**
```bash
python3 hands_on/03_tools_and_rag.py
```

**Output:**
```text
1. Function calling with Python tools:
User query: Sarah has policy POL-99214 and the repair bill is $1537.15. Find her deductible and calculate her net payout.

Gemini final response:
Sarah's deductible for policy POL-99214 is $500. Her net payout for the repair bill of $1537.15 is $1037.15.

2. Reading PDF document using Gemini File API:
Uploading samples/sample_policy.pdf to Gemini...
Answer from PDF:
According to Section 2: Incident Reporting Timelines, all vehicle collisions must be formally reported within 72 hours of occurrence.

3. Embeddings and basic RAG:
User asked: 'Will insurance pay for original OEM parts for a 2024 model car?'
Best matched rule: 'OEM parts are covered for vehicles under 4 years old.'
RAG answer:
Yes, based on that rule, insurance will pay for original OEM parts for a 2024 model car.
A 2024 model car would be 0-1 year old, which is well "under 4 years old."

4. Live Google Search Grounding:
Google grounded answer:
The price range for Honda Civic LED headlight replacement in the US can vary significantly depending on whether you are replacing just the LED bulbs or the entire headlight assembly.
- LED Headlight Bulbs (Replacement): $40 to $60 combo kit.
- Aftermarket LED Headlight Assemblies: $170 to over $1,000 per pair.
- Full LED OEM assemblies: $645 to $1,000 each.
```

---

## 5. Session 4: Audio, Safety, Caching & Mini-Project (`04_advanced_caching_audio.py`)

**Command:**
```bash
python3 hands_on/04_advanced_caching_audio.py
```

**Output:**
```text
1. Audio understanding from voice call:
Uploading samples/sample_call.wav...
Call analysis:
Here's the extracted information:
1. Caller Name: Sarah Jenkins
2. Policy Number: POL-99214
3. Summary of Incident: A front bumper collision occurred yesterday in a grocery store parking lot. Another vehicle backed into her car, cracking the bumper and the right LED headlight.

2. Configuring safety filters:
Safe output:
"Hello! I'm sorry to hear you're in a situation that requires filing a claim, but we're here to help make the process as straightforward as possible for you. How can I assist you today?"

3. Context caching:
Use this when you have huge files like 100+ page policy manuals.
Instead of sending 50,000 tokens every time, cache it once on Gemini servers.
Cached queries are faster and cost 75% less.
Code pattern:
  cache = client.caches.create(model='gemini-2.5-flash', config=types.CreateCachedContentConfig(contents=[pdf_file], ttl='3600s'))
  client.models.generate_content(model='gemini-2.5-flash', contents='my query', config=types.GenerateContentConfig(cached_content=cache.name))

4. End-to-end claims automation pipeline:
- Step 1: Customer calls hotline -> Gemini listens to audio and extracts policy POL-99214.
- Step 2: Customer uploads invoice image -> Gemini extracts $1,537.15 repair bill.
- Step 3: Gemini searches policy PDF -> confirms collision covered, deductible is $500.
- Step 4: Python tool calculates payout -> $1,537.15 - $500 = $1,037.15.
- Step 5: Customer gets instant approved settlement notification.
```
