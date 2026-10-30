
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

# Store conversation history
chat_history = []

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI teacher. Use previous conversation to understand the user."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# Create chain
chain = prompt | llm

print("=== DAY 38 FINAL AI CHATBOT ===")
print("Type 'exit' to stop the chatbot.\n")

# Interactive conversation
while True:

    question = input("You: ")

    if question.lower().strip() == "exit":
        print("Chatbot stopped!")
        break

    # Send previous history and new question
    response = chain.invoke({
        "chat_history": chat_history,
        "question": question
    })

    answer = response.text

    print("\nGemini:", answer, "\n")

    # Automatically save both messages
    chat_history.append(
        HumanMessage(content=question)
    )

    chat_history.append(
        AIMessage(content=answer)
    )

# Display complete history
print("\n=== COMPLETE CHAT HISTORY ===")

for message in chat_history:
    print(type(message).__name__, ":", message.content)
