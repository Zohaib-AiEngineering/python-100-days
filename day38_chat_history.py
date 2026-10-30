import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")

# Connect Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key
)

# Previous conversation
chat_history = [
    HumanMessage(content="My name is Ali."),
    AIMessage(content="Nice to meet you, Ali!"),
    HumanMessage(content="I am learning Python."),
    AIMessage(content="Great! Keep learning Python.")
]

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI teacher. Use conversation history to understand the user."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# Connect prompt with Gemini
chain = prompt | llm

# Ask question
response = chain.invoke({
    "chat_history": chat_history,
    "question": "What is my name and what am I learning?"
})

print("\nGEMINI RESPONSE:\n")
print(response.content)