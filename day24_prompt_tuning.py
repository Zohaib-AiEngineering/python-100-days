from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GemINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_response(prompt, temperature=0.3):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "temperature": temperature
        }
    )
    return response.text
structured_prompt = """
You are a friendly Python teacher.

Always explain concepts step by step.
Use simple English.
Give practical examples.

Now explain Python lists to a complete beginner.
Give one simple example.
"""
structured_response = generate_response(
    structured_prompt,
    temperature=0.2
)
print("\n===== STRUCTURED PROMPT =====")
print(structured_response)
# Zero shot prompt

zero_shot_prompt = """
Classify the following sentence as Positive or Negative:

"I really enjoyed this movie."
"""

zero_shot_response = generate_response(
   zero_shot_prompt,
   temperature=0.2 
)

print("\n ======ZERO-SHOT========")
print(zero_shot_response)

#few_shot_promp
few_shot_prompt = """
Classify the sentiment as Positive or Negative.

Example 1:
"I love this phone." → Positive

Example 2:
"This food is terrible." → Negative

Now classify:
"I really enjoyed this movie."
"""

few_shot_response = generate_response(
    few_shot_prompt,
        
    temperature=0.2

    
)

print("\nFEW-SHOT:")
print(few_shot_response)