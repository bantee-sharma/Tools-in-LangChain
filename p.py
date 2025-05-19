from langchain_community.tools import DuckDuckGoSearchRun
from pydantic import BaseModel,Field
from langchain.tools import tool,StructuredTool


class MultiplyInput(BaseModel):
    a:int
    b:int

def multiply(a,b):
    return a*b

mult_tool = StructuredTool(
    name="Multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput,
    func=multiply
)

print(mult_tool.invoke({"a":2,"b":3}))
