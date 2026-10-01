# Problem Statement: Audio Call Triage, Safety Filters & Context Caching

## 1. Business Context
Many customers report vehicular accidents over the phone rather than through online forms. Contact centers are overwhelmed with voice recordings that require manual listening, typing notes, determining urgency, and checking policy manuals. Meanwhile, enterprise policy manuals contain hundreds of pages, causing high token costs if sent repeatedly to AI models.

## 2. Core Problem to Solve
- Ingesting raw audio recordings (.wav / .mp3) directly to extract caller identity, policy numbers, and incident facts without needing third-party speech-to-text tools.
- Preventing toxic or abusive language by enforcing strict enterprise safety guardrails.
- Reducing token latency and API billing costs when repeatedly referencing massive policy manuals.
- Demonstrating the complete, unified claims automation pipeline.

## 3. What the Code Implements (`04_advanced_caching_audio.py`)
1. **Audio Understanding:** Uploads [`samples/sample_call.wav`](../samples/sample_call.wav) to Gemini File API. Gemini listens to the audio and extracts the claimant name (*Sarah Jenkins*), policy number (*POL-99214*), and accident summary.
2. **Safety Settings:** Configures `types.SafetySetting` across `HARM_CATEGORY_HATE_SPEECH` and `HARM_CATEGORY_HARASSMENT` to ensure all generated responses remain compliant.
3. **Context Caching:** Demonstrates how `client.caches.create()` caches large static documents (100k+ tokens) on Gemini servers to reduce latency and cut query costs by up to 75%.
4. **End-to-End Pipeline Overview:** Connects the complete workflow:
   - Voice Audio $\to$ Invoice Vision $\to$ Policy PDF RAG $\to$ Payout Tool $\to$ Instant Settlement.

## 4. Expected Output
An automated triage system that processes customer hotline voice calls, applies strict safety filters, and shows how enterprises scale with Context Caching.
