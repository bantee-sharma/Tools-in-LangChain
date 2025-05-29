from langchain_experimental.tools import PythonREPLTool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import tool,create_react_agent,AgentExecutor, initialize_agent,Agent,AgentType

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

repl = PythonREPLTool()

agent = initialize_agent(
    llm=llm,
    tools=[repl],
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.invoke("write a func of adding 2 number in pyhton")