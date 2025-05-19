from langchain_experimental.tools import PythonREPLTool
from langchain_community.tools import DuckDuckGoSearchRun,GmailSendMessage,WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool,StructuredTool
from pydantic import BaseModel, Field

search = DuckDuckGoSearchRun()

res = search.invoke("Trending news in india")

"""@tool
def multiply(a:int,b:int)->int:
    '''Multiply two numbers'''
    return a*b

print(multiply.invoke({"a":5,"b":5}))
print(multiply.name)
print(multiply.description)
print(multiply.args)
"""

class multiplyinput(BaseModel):
    a:int
    b:int

def multiply(a,b):
    '''Multiply two numbers'''
    return a*b

mult_tool = StructuredTool(
    func=multiply,
    name='multiply',
    description="multiply 2 numbers",
    args_schema=multiplyinput
)

print(mult_tool.invoke({"a":5,"b":5}))