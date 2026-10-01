# session 1: gemini basics and chatbot setup
import os
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

# 1. basic text generation
print("\n1. Basic text generation:")
prompt = "What is car insurance deductible in one simple sentence?"

# send prompt directly to model
response = client.models.generate_content(
    model=MODEL,
    contents=prompt
)
print("Answer:", response.text.strip())


# 2. system instructions and temperature
print("\n2. System instructions and temperature:")

# config with agent role and low temperature
config = types.GenerateContentConfig(
    system_instruction="You are a polite customer support agent named Alex. Answer in max 2 sentences.",
    temperature=0.2
)

response = client.models.generate_content(
    model=MODEL,
    contents="My car has a scratch, what should I do?",
    config=config
)
print("Agent reply:", response.text.strip())


# 3. stream output word by word
print("\n3. Streaming output word by word:")
prompt = "Give 3 quick tips to do immediately after a car accident."

stream = client.models.generate_content_stream(
    model=MODEL,
    contents=prompt
)

# print words as they arrive in real time
for chunk in stream:
    print(chunk.text, end="", flush=True)
print()


# 4. multi-turn chat with memory
print("\n4. Multi-turn chat with memory:")

# create chat session that tracks history
chat = client.chats.create(model=MODEL)

# message 1
print("User: Hi, my name is Sarah.")
r1 = chat.send_message("Hi, my name is Sarah.")
print("Bot:", r1.text.strip())

# message 2: check if bot remembers sarah
print("\nUser: Do you remember my name?")
r2 = chat.send_message("Do you remember my name?")
print("Bot:", r2.text.strip())
