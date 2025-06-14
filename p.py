from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [SystemMessage(content="You are a helpful AI Assistant")]


print("🤖 Hey! I'm your AI buddy. Ask me anything! Type 'exit' or 'quit' whenever you're done chatting.")


while True:
    query = input("Ask me: ").strip()
    chat_history.append(HumanMessage(content=query))
    if query.lower() in ["exit","quit"]:
        print("AI : Goodbye! Have a great day!")
        break
    else:
        resopnce = llm.invoke(chat_history)
        chat_history.append(AIMessage(content=resopnce.content))
        print("AI: ",resopnce.content)
    
print(chat_history)
