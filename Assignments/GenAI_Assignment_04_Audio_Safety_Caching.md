# Assignment 4: Customer Voicemail Triage, Safety Filters & Context Caching

**Module:** GenAI with Gemini SDK — Session 4  
**Estimated Time:** 1 – 1.5 Hours  
**Difficulty:** Intermediate  

---

## 🎯 Objective
Process recorded customer phone calls with Gemini Audio Understanding, enforce enterprise safety guardrails, explore Context Caching for large technical manuals, and design an end-to-end automated processing pipeline.

---

## 📌 Problem Scenario
A telecommunications provider ("Apex Telecom") receives hundreds of audio voicemails every day from customers reporting broadband outages, billing disputes, and SIM card issues. Customer service representatives spend hours listening to audio messages, transcribing them, and categorizing urgency.

---

## 📋 Tasks & Requirements

### Task 1: Direct Audio Understanding & Triage
- Use [`GenAI/samples/sample_call.wav`](../GenAI/samples/sample_call.wav) (or any sample spoken voice recording in `.wav`, `.mp3`, or `.m4a`).
- Upload the audio file using `client.files.upload()`.
- Ask Gemini to listen to the call and extract structured metadata:
  1. Caller Name
  2. Account or Policy Number
  3. Nature of Complaint / Incident
  4. Customer Emotion (e.g., Calm, Frustrated, Anxious)
  5. Urgency Score (1 to 10)
- Print the model's triage assessment.

### Task 2: Enterprise Safety Guardrails
- Configure safety settings using `types.SafetySetting`:
  - `HARM_CATEGORY_HATE_SPEECH` $\to$ `BLOCK_LOW_AND_ABOVE`
  - `HARM_CATEGORY_HARASSMENT` $\to$ `BLOCK_MEDIUM_AND_ABOVE`
  - `HARM_CATEGORY_DANGEROUS_CONTENT` $\to$ `BLOCK_MEDIUM_AND_ABOVE`
- Send a prompt to Gemini with these safety filters attached.
- Verify that standard customer service responses pass safely and observe how thresholds protect production applications.

### Task 3: Context Caching Architecture
- Explain in comments or code output how Context Caching works when dealing with massive documents (e.g., a 200-page telecommunications router manual of 80,000 tokens).
- Write down the exact SDK code pattern for:
  1. Creating a cache with `client.caches.create()` and a 1-hour TTL (`ttl="3600s"`).
  2. Querying the cache using `types.GenerateContentConfig(cached_content=cache.name)`.
- Explain why caching reduces both latency and API billing costs by up to 75%.

### Task 4: End-to-End Pipeline Synthesis
- Write a short summary connecting all 4 sessions into a single automated architecture:
  - Step 1: Customer Call Audio Ingestion (Session 4)
  - Step 2: Invoice / Photo Structured Extraction (Session 2)
  - Step 3: Policy PDF Verification & Database Tool Lookup (Session 3)
  - Step 4: Streaming Support Notification back to Customer (Session 1)

---

## 💡 Key SDK Methods to Use
```python
from google.genai import types

# 1. Audio Upload & Analysis
audio_file = client.files.upload(file="voicemail.wav")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[audio_file, "Extract caller name, complaint, and urgency score."]
)

# 2. Safety Settings
safety = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    )
]
config = types.GenerateContentConfig(safety_settings=safety)
```

---

## 🏆 Submission Deliverables
1. Python script: `assignment_04.py`
2. Terminal execution output showing the audio triage extraction and safety filter output.
