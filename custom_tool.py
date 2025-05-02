from langchain_core.tools import tool

def func(a,b):
    '''Multiplying two numbers'''
    return a*b

def multiply(a: int, b: int) -> int:
    '''Multiplying two numbers'''
    return a*b

@tool
def multiply(a: int, b: int) -> int:
    '''Multiplying two numbers'''
    return a*b


res = multiply.invoke({'a':3,'b':5})
print(res)
print(multiply.name)
print(multiply.description)
print(multiply.args)