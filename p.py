from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
import pandas as pd
import numpy as np
import streamlit as st

load_dotenv()

df = pd.read_excel("dataset netflix.xlsx")
print(df.head())

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# csv_agent = create_csv_agent(
#     llm=llm,
#     path="dataset netflix.xlsx",
#     allow_dangerous_code=True,
#     verbose=True
# )

# query = "how many rows are there?"
# response = csv_agent.invoke(query)
# print(response)

