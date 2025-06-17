from typing import TypedDict,Optional,Literal,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

llm = model.with_structured_output(Review)
