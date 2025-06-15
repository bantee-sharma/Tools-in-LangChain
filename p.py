from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import numpy as np
import streamlit as st

load_dotenv()

st.set_page_config(page_title="CSV AI Agent", layout="wide")
st.header("📁 CSV-AI-Agent")

file_uploaded = st.file_uploader("upload your file",type=["csv"])

if file_uploaded is not None:
    df = pd.read_csv(file_uploaded)
    st.write("Data Preview")
    st.dataframe(df)
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    csv_agent = create_pandas_dataframe_agent(
    llm=llm,
    df=df,
    agent_type="openai-tools",
    allow_dangerous_code=True,
    verbose=True,
    pandas_kwargs={"encoding": "latin1"},
    agent_executor_kwargs={"handle_parsing_errors": True}
)


    query = st.text_input("💬 Ask a question about your data:")
    if st.button("Submit") and query:
        with st.spinner("Thinking..."):
            try:
                response = csv_agent.run(query)
                st.success("✅ Answer:")
                st.write(response)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
