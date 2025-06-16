from typing import TypedDict,Optional,Literal,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Review(BaseModel):

    summary: str = Field(description="summary of the review")
    sentiment: str 
    pros: list[str]
    cons: list[str]

parser = PydanticOutputParser(pydantic_object=Review)

prompt = PromptTemplate(
    template="Give the sentiment of the following review:{review}. \n {format_instruction}",
    input_variables=["review"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

query = """Upgraded to the 16 from my 12 and it is a great phone. The Ultramarine Blue looks and feels sooo good. 
    The photos don't do enough justice to this variant.

    You definitely do not need to upgrade to this if you are having a 14 or a 15, unless Apple Intelligence 
    is something that you do not want to live without.
    
    Camera is great, though not very sure of the Camera Control thing, cuz all that is pretty much available on-screen UI.

    Also, got a great deal on the exchange and bank offer, so zero complaints."""

chain = prompt | llm | parser

response = chain.invoke({"review":query})
print(response)

