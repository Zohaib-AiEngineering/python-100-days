
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

# Empty chat history
chat_history = []

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI teacher. Remember the conversation history."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# Create chain
chain = prompt | llm

# Function to chat and update history
def chat(question):

    # Save user's message
    chat_history.append(
        HumanMessage(content=question)
    )

    # Send history to Gemini
    response = chain.invoke({
        "chat_history": chat_history[:-1],
        "question": question
    })

    # Save Gemini's response
    chat_history.append(
        AIMessage(content=response.text)
    )

    print("\nGemini:", response.text)


# Test conversation
chat("My name is Ali.")
chat("I am learning Python.")
chat("What is my name and what am I learning?")

# Show complete history
print("\n--- COMPLETE CHAT HISTORY ---")

for message in chat_history:
    print(type(message).__name__, ":", message.content)
