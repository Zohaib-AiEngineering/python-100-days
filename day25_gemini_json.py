from google import genai
from dotenv import load_dotenv
import os
import json
load_dotenv()
api_key = os.getenv("Gemini_API_KEY")
client = genai.Client(api_key=api_key)
prompt ="""
Extract the following information from this text:
name, age, and city.

Return the result as JSON only.
Do not include markdown or extra explanation.

Text: Ali is 25 years old and lives in Lahore.
"""
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={"temperature": 0.2}
)
print(response.text)

try:
    data = json.loads(response.text)

    print("Name:", data["name"])
    print("Age:", data["age"])
    print("City:", data["city"])

except json.JSONDecodeError:
    print("Error: Gemini returned invalid JSON.")