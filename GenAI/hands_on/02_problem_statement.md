# Problem Statement: Automated Repair Invoice Parsing & Structured Extraction

## 1. Business Context
Claimants submit repair estimates and mechanic bills as images, photos, and scanned receipts. Human adjusters spend hours manually typing line items, tax numbers, and invoice codes into claims management software. This manual process causes delayed claim settlements and high data entry error rates.

## 2. Core Problem to Solve
- Plain OCR tools extract raw text but lose table layout and cannot understand whether an item is labor or a part.
- Standard LLMs output unstructured markdown or messy text that cannot be directly inserted into backend databases or APIs.
- We need guaranteed, schema-validated JSON with exact data types (strings, floats, lists of items).

## 3. What the Code Implements (`02_multimodal_structured.py`)
1. **Multimodal Vision:** Feeds [`samples/sample_receipt.png`](../samples/sample_receipt.png) directly into Gemini Vision to describe the invoice and read the total.
2. **Schema Definition:** Uses Python Pydantic (`ReceiptData`) to enforce the exact JSON schema required by backend systems:
   - `shop_name`: Name of repair shop
   - `invoice_number`: Unique invoice ID
   - `customer_name`: Policyholder name
   - `total_amount`: Numeric dollar total
   - `repaired_parts`: List of parts and services
3. **Structured JSON Output:** Passes `response_mime_type="application/json"` and `response_schema=ReceiptData` to Gemini.
4. **Validation:** Directly converts the model output into Python objects using `ReceiptData.model_validate_json()`.

## 4. Expected Output
A verified, machine-readable JSON object extracted from an invoice photo that backend databases can consume instantly without manual typing.
