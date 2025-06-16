from typing import TypedDict,Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Review(TypedDict):

    key_themes = list[str]
    summary:str
    sentiment:str
    pros:Optional[list[str]]
    cons:Optional[list[str]]
    
llm = model.with_structured_output(Review)
query = '''Hey folks, it's Bob here. I’ve been using the new iPhone 16 for about two weeks now, and here’s my honest take. First off, the performance is incredible—the new A18 Bionic chip handles everything I throw at it like a champ. Whether I'm gaming, editing videos, or just multitasking with a bunch of apps, it never lags. The display is another highlight: the ProMotion OLED screen is bright, super smooth, and a joy to look at, especially when watching Netflix or scrolling social media. Battery life has definitely improved—I'm easily getting through a full day with 30–40% left, which is impressive considering how much I use my phone. The camera system is a big win too—low-light photography has improved a lot, and the AI-powered portrait mode actually makes me look photogenic (miracle, I know!). Also, USB-C is finally here—no more Lightning cable drama, which I really appreciate. Now, on the flip side, the price is still ridiculous. Even with all the upgrades, it stings to spend that much. Plus, the design hasn’t changed much—it still looks like my old iPhone 14, so it’s not exactly exciting in the looks department. Another letdown is that some of the cooler AI features are limited to the Pro models, which feels a bit unfair. Oh, and that glossy back? Smudge city. Still, all in all, the iPhone 16 is a powerful, premium device. If you're using an older iPhone like the 12 or earlier, this is definitely worth the upgrade. But if you're already on the 14 or 15, you might not notice a huge difference. That’s my take—hope it helps!'''

response = llm.invoke(query)
print(response)