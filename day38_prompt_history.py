from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Previous conversation
chat_history = [
    HumanMessage(content="My name is Ali."),
    AIMessage(content="Nice to meet you, Ali!"),
    HumanMessage(content="I am learning Python."),
    AIMessage(content="Great! Keep learning Python.")
]

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI teacher."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# Insert history and new question
response = prompt.invoke({
    "chat_history": chat_history,
    "question": "How can I start learning AI?"
})

# Print complete messages
print("\nCOMPLETE PROMPT\n")

for message in response.to_messages():
    print(type(message).__name__, ":", message.content)