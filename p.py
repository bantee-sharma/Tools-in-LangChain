from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_experimental.tools import PythonAstREPLTool,PythonREPLTool

load_dotenv()

py = PythonREPLTool()

query = 'print(2+5)'
response = py.invoke(query)
print(query)