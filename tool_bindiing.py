from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

@tool
def multiply(a:int,b:int)->int:
    '''Multiplying'''
    return a*b

'''print(multiply.invoke({"a":9,"b":2}))

print(multiply.name)
print(multiply.description)
print(multiply.args)'''

#tool binding

llm_with_tools = llm.bind_tools([multiply])

print(llm_with_tools.invoke("Hi how are You?"))