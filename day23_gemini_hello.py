from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GemINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Hello Gemini! who is famous person in pakistan."
)
print(response.text)