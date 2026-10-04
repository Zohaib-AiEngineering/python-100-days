import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. .env file se API key load karein
load_dotenv()
my_key = os.getenv("GEMINI_API_KEY")

# 2. Gemini ko configure karein
genai.configure(api_key=my_key)

# 3. Model select karein (Naya list kiya hua model)
model = genai.GenerativeModel('gemini-3.6-flash')

# 4. Prompt bhejein
prompt = "Python seekhne ke liye mujhe 1 line ki motivation do."
print("Gemini se pooch rahe hain...")

response = model.generate_content(prompt)

# 5. Output print karein
print("\nGemini ka Jawab:")
print(response.text)