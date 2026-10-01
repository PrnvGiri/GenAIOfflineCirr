# session 2: reading images and getting structured json output
import os
import time
from dotenv import load_dotenv
from PIL import Image
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# load api key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "").strip()

# connect to gemini client
client = genai.Client(api_key=api_key)

# using 2.5 flash
MODEL = "gemini-2.5-flash"
IMAGE_PATH = "samples/sample_receipt.png"


# 1. pass image directly to gemini vision
print("\n1. Reading image with Gemini Vision:")

# open image file from disk
img = Image.open(IMAGE_PATH)

# send image and question together
prompt = "Look at this image. Tell me what type of receipt this is and the grand total."
response = client.models.generate_content(
    model=MODEL,
    contents=[img, prompt]
)
print("Gemini reply:\n", response.text.strip())


# pause to avoid free tier rate limit
time.sleep(10)


# define schema format we want back from gemini
class ReceiptData(BaseModel):
    shop_name: str = Field(description="Name of the mechanic or shop")
    invoice_number: str = Field(description="Invoice number")
    customer_name: str = Field(description="Customer name")
    total_amount: float = Field(description="Total price in USD")
    repaired_parts: list[str] = Field(description="List of parts replaced or repaired")


# 2. get guaranteed json back matching our pydantic model
print("\n2. Extracting structured JSON data from image:")

prompt = "Extract receipt details into structured json."

# pass response_schema to force gemini to return clean json
config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=ReceiptData
)

response = client.models.generate_content(
    model=MODEL,
    contents=[img, prompt],
    config=config
)

print("Raw JSON received:\n", response.text.strip())

# parse json string to python object
data = ReceiptData.model_validate_json(response.text)

# access fields directly in python
print("\nReading fields in python code:")
print(f"- Shop: {data.shop_name}")
print(f"- Invoice No: {data.invoice_number}")
print(f"- Customer: {data.customer_name}")
print(f"- Total Bill: ${data.total_amount}")
print(f"- Repaired Items: {', '.join(data.repaired_parts)}")
