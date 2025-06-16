from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Review(TypedDict):

    key_themes = list[str]
    summary:str
    sentiment:str
    pros:str
    cons:str
    
llm = model.with_structured_output(Review)
query = '''Just upgraded to the iPhone 16 and I'm genuinely impressed. Apple has really stepped up their game with this one. The design is sleek and premium as always, but what really blew me away is the performance — everything feels lightning fast thanks to the new A18 chip.

The camera system is phenomenal. The photos are sharper, low-light performance is better than ever, and the new AI-powered editing tools are a game changer. Battery life easily lasts me a full day, even with heavy use.

I'm also loving the improved display — it’s super bright, color-accurate, and perfect for streaming or editing content on the go. iOS 18 runs flawlessly and the new features feel intuitive and genuinely useful.

If you're on the fence about upgrading, go for it. The iPhone 16 is hands down the best iPhone yet.'''

response = llm.invoke(query)
print(response)