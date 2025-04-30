from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

res = search.invoke("Top news in India")

print(res)

print(search.name)
print(search.description)
print(search.args)