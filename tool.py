from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

res = search.invoke("create a func that check a string is palindrome or not")

print(res)

print(search.name)
print(search.description)
print(search.args)