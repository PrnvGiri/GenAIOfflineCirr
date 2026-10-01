# Assignment 2: Restaurant Bill Scanner & Expense Report Generator

**Module:** GenAI with Gemini SDK — Session 2  
**Estimated Time:** 1.5 – 2 Hours  
**Difficulty:** Beginner to Intermediate  

---

## 🎯 Objective
Use Gemini Vision and Python Pydantic to scan a restaurant dining receipt/invoice, perform visual analysis, and extract validated structured JSON data directly into Python data models.

---

## 📌 Problem Scenario
A corporate employee expense management company ("ExpenseEase") wants to eliminate manual data entry of food and travel receipts. When an employee takes a photo of their lunch or dinner bill, the system must:
1. Visually identify the restaurant name, date, and tax amounts.
2. Itemize individual food and beverage items with individual prices.
3. Guarantee strict JSON format with type safety (e.g. floats for currency, list of items) that matches a predefined database model.

---

## 📋 Tasks & Requirements

### Task 1: Image Reading & Visual Inspection
- Use `PIL.Image.open()` to load a sample receipt or bill image (you can use [`GenAI/samples/sample_receipt.png`](../GenAI/samples/sample_receipt.png) or any restaurant receipt photo).
- Send the image + prompt to Gemini: *"Describe this document. What is the business name and grand total?"*
- Print the model's visual reasoning.

### Task 2: Pydantic Schema Definition
Define two Pydantic models using `pydantic.BaseModel` and `Field`:
```python
from pydantic import BaseModel, Field
from typing import List

class LineItem(BaseModel):
    item_name: str = Field(description="Name of the food, drink, or service")
    price: float = Field(description="Price in currency units")

class RestaurantReceipt(BaseModel):
    restaurant_name: str = Field(description="Name of the restaurant or vendor")
    bill_number: str = Field(description="Invoice or bill number if available")
    items: List[LineItem] = Field(description="List of ordered items")
    subtotal: float = Field(description="Subtotal before taxes and tips")
    tax: float = Field(description="Tax amount")
    grand_total: float = Field(description="Final amount paid")
```

### Task 3: Schema-Driven Structured Extraction
- Configure `types.GenerateContentConfig`:
  - `response_mime_type="application/json"`
  - `response_schema=RestaurantReceipt`
- Send the image and prompt to Gemini.
- Print the raw JSON string received from Gemini.

### Task 4: Python Model Validation & Field Access
- Parse the response string using `RestaurantReceipt.model_validate_json(response.text)`.
- Print the extracted fields programmatically:
  - Total items ordered count
  - Highest priced item
  - Verified math check: `subtotal + tax == grand_total`

---

## 💡 Key SDK Methods to Use
```python
from PIL import Image
from pydantic import BaseModel
from google.genai import types

img = Image.open("path/to/receipt.png")

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=RestaurantReceipt,
    temperature=0.1
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[img, "Extract all receipt data into JSON"],
    config=config
)
```

---

## 🏆 Submission Deliverables
1. Python script: `assignment_02.py`
2. Sample image used for testing (PNG or JPEG).
3. Terminal output showing the raw JSON and the parsed Pydantic object values.
