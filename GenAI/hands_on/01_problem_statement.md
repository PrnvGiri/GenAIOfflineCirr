# Problem Statement: Customer Claims Intake Chatbot

## 1. Business Context
An insurance company (*Veritas Mutual*) receives thousands of customer inquiries every day regarding accidents, claims, and policies. Traditional scripted chatbots (IVR/rule-based) are robotic, fail to understand context, and cannot maintain natural multi-turn conversations.

## 2. Core Problem to Solve
When a customer gets into an accident, they are stressed and need:
- An empathetic and reassuring support agent persona (not a generic robot).
- Fast, real-time responses without waiting for full paragraphs to load (streaming).
- A bot that remembers facts shared earlier in the conversation (claimant name, policy number) across multiple chat turns.
- Deterministic, hallucination-free answers about policies (controlled temperature).

## 3. What the Code Implements (`01_chatbot_foundations.py`)
1. **Basic Generation:** Connects to Gemini to answer general policy questions in one sentence.
2. **System Instructions:** Sets a specific persona (`Alex`, empathetic customer agent) with low temperature (`0.2`) for factual consistency.
3. **Streaming:** Uses `generate_content_stream` to print words in real time as they arrive.
4. **Multi-Turn Chat:** Uses `client.chats.create` to remember customer details (e.g. claimant Sarah) across multiple turns.

## 4. Expected Output
A responsive customer intake bot that welcomes the user, answers immediate safety questions with streaming text, and accurately recalls past conversation context.
