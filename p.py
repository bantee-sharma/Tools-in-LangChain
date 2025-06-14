from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = []

while True:
    query = input("Ask me: ").strip()
    chat_history.append(HumanMessage(content=query))
    if query.lower() in ["exit","quit"]:
        print("Byee, I am exiting...")
        break
    else:
        resopnce = llm.invoke(chat_history)
        chat_history.append(resopnce)
        print("AI: ",resopnce.content)
    
print(chat_history)
