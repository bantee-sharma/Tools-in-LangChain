

llm = model.with_structured_output(Review)
query = """Upgraded to the 16 from my 12 and it is a great phone. The Ultramarine Blue looks and feels sooo good. 
    The photos don't do enough justice to this variant.

    You definitely do not need to upgrade to this if you are having a 14 or a 15, unless Apple Intelligence 
    is something that you do not want to live without.
    
    Camera is great, though not very sure of the Camera Control thing, cuz all that is pretty much available on-screen UI.

    Also, got a great deal on the exchange and bank offer, so zero complaints."""



response = llm.invoke(query)
print(response)