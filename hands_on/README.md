# GenAI Hands-On Labs

Simple hands-on code matching curriculum.txt for Gemini SDK.

## Models
- Main model: `gemini-2.5-flash` (fast, handles chat, vision, audio, tools)
- Embedding model: `gemini-embedding-001` (for rag and semantic search)

## Test Files Created in `samples/`
- `samples/sample_receipt.png` - mechanic repair bill image with itemized costs
- `samples/sample_policy.pdf` - 2 page auto insurance policy document
- `samples/sample_call.wav` - spoken customer phone call reporting an accident

## Files in `hands_on/`
- `check_models.py` - check which models are enabled on your api key
- `01_chatbot_foundations.py` - basic text generation, system instructions, streaming, multi-turn chat
- `02_multimodal_structured.py` - reading receipt image and extracting clean json using pydantic
- `03_tools_and_rag.py` - python function calling tools, pdf upload, embeddings vector search, google search
- `04_advanced_caching_audio.py` - listening to audio call, safety filters, context caching, full claims flow
