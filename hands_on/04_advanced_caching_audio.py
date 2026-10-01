# session 4: audio understanding, safety settings, caching and mini project
import os
import time
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
AUDIO_PATH = "samples/sample_call.wav"


# 1. upload audio recording and extract information
print("\n1. Audio understanding from voice call:")

# upload audio file to gemini
print(f"Uploading {AUDIO_PATH}...")
audio_file = client.files.upload(file=AUDIO_PATH)

# prompt model to listen to audio and pull key details
prompt = (
    "Listen to this customer call recording. "
    "Extract: 1. Caller Name, 2. Policy Number, 3. Summary of incident."
)

response = client.models.generate_content(
    model=MODEL,
    contents=[audio_file, prompt]
)
print("Call analysis:\n", response.text.strip())


# pause to avoid free tier rate limit
time.sleep(10)


# 2. configure safety settings
print("\n2. Configuring safety filters:")

# block hate speech and harassment
safety = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    )
]

response = client.models.generate_content(
    model=MODEL,
    contents="Say a polite greeting to customer filing a claim.",
    config=types.GenerateContentConfig(safety_settings=safety)
)
print("Safe output:\n", response.text.strip())


# 3. how context caching works
print("\n3. Context caching:")
print("Use this when you have huge files like 100+ page policy manuals.")
print("Instead of sending 50,000 tokens every time, cache it once on Gemini servers.")
print("Cached queries are faster and cost 75% less.")
print("Code pattern:")
print("  cache = client.caches.create(model='gemini-2.5-flash', config=types.CreateCachedContentConfig(contents=[pdf_file], ttl='3600s'))")
print("  client.models.generate_content(model='gemini-2.5-flash', contents='my query', config=types.GenerateContentConfig(cached_content=cache.name))")


# 4. complete mini-project pipeline overview
print("\n4. End-to-end claims automation pipeline:")
print("- Step 1: Customer calls hotline -> Gemini listens to audio and extracts policy POL-99214.")
print("- Step 2: Customer uploads invoice image -> Gemini extracts $1,537.15 repair bill.")
print("- Step 3: Gemini searches policy PDF -> confirms collision covered, deductible is $500.")
print("- Step 4: Python tool calculates payout -> $1,537.15 - $500 = $1,037.15.")
print("- Step 5: Customer gets instant approved settlement notification.")
