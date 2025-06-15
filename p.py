from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
import pandas as pd
import numpy as np
import streamlit as st

load_dotenv()

df = pd.read_csv("dataset_netflix.csv",encoding='latin1')
# print(len(df))

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

csv_agent = create_csv_agent(
    llm=llm,
    path="dataset_netflix.csv",
    allow_dangerous_code=True,
    verbose=True,
    pandas_kwargs={"encoding": "latin1"}
)

query = "how many rows are there?"
response = csv_agent.invoke(query)
print(response)

