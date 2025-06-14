from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


while True:
    query = input("Ask me: ").strip()
    if query.lower() in ["exit","quit"]:
        print("Byee, I am exiting...")
        break
    else:
        resopnse = llm.invoke(query)
        print("AI: ",resopnse.content)
