
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# .env se API key load karo
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY .env file mein nahi mili.")

# Gemini model configure karo
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
)

# PromptTemplate banao
prompt = PromptTemplate.from_template(
    "Mujhe {topic} ke bare mein asaan alfaaz mein samjhao."
)

# Prompt ko LLM ke saath connect karo
chain = prompt | llm

# Chain run karo
response = chain.invoke({"topic": "LangChain"})

print(response.content)
