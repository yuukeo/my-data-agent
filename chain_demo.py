import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatZhipuAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

# 创建模型（和之前一样）
llm = ChatZhipuAI(
    model="glm-4-flash",
    temperature=0.1,
    api_key=os.getenv("ZHIPU_API_KEY")
)

# 定义提示词模板——这里让 AI 扮演数据分析师
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名资深的数据分析师，回答问题时请用清晰的结构，先给结论，再分点阐述。"),
    ("human", "{user_input}")
])

# 把模板和模型串成一条链
chain = prompt | llm

# 运行链
response = chain.invoke({"user_input": "如何分析一家公司的销售数据？"})
print(response.content)