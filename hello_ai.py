import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatZhipuAI

load_dotenv()

llm = ChatZhipuAI(
    model="glm-4-flash",
    temperature=0.1,
    api_key=os.getenv("ZHIPU_API_KEY")
)

response = llm.invoke("用一句话介绍什么是数据分析")
print(response.content)