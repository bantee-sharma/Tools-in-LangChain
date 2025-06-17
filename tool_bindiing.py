from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

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

query = HumanMessage('Can you multiply 3 with 100')

message = [query]

result = llm_with_tools.invoke(message)

message.append(result)

tool_res = multiply.invoke(result.tool_calls[0])

message.append(tool_res)

print(llm_with_tools.invoke(message).content)
    
