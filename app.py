import streamlit as st
import pandas as pd
from langchain_community.chat_models import ChatZhipuAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
import os

load_dotenv()

st.title("📊 智能数据分析助手")
uploaded_file = st.file_uploader("上传 CSV 文件", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    llm = ChatZhipuAI(model="glm-4-flash", temperature=0, api_key=os.getenv("ZHIPU_API_KEY"))
    agent = create_pandas_dataframe_agent(
        llm, df, verbose=False, allow_dangerous_code=True,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )

    question = st.text_input("请输入你的问题：")
    if question:
        with st.spinner("AI 正在分析..."):
            response = agent.invoke(question)
            st.write(response["output"])