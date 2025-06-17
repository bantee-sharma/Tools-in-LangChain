from typing import TypedDict,Optional,Literal,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

llm = model.with_structured_output(Review)

query = """Upgraded to the 16 from my 12 and it is a great phone. The Ultramarine Blue looks and feels sooo good. 
    The photos don't do enough justice to this variant.

    You definitely do not need to upgrade to this if you are having a 14 or a 15, unless Apple Intelligence 
    is something that you do not want to live without.
    
    Camera is great, though not very sure of the Camera Control thing, cuz all that is pretty much available on-screen UI.

    Also, got a great deal on the exchange and bank offer, so zero complaints."""


s