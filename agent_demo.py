import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatZhipuAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_experimental.tools import PythonREPLTool

load_dotenv()

# 1. 创建模型
llm = ChatZhipuAI(
    model="glm-4-flash",
    temperature=0,
    api_key=os.getenv("ZHIPU_API_KEY")
)

# 2. 创建 Python 执行工具
python_tool = PythonREPLTool()
tools = [python_tool]

# 3. 提示词——用 {tool_names} 不要加方括号
react_template = """你是一个能够使用 Python 解决问题的助手。当你编写 Python 代码时，必须使用 print() 输出计算结果。

你可以使用以下工具：

{tools}

使用以下格式回答：

Question: 用户的问题
Thought: 思考需要做什么
Action: 工具名称，必须是 {tool_names} 中的一个，不要加方括号或引号
Action Input: 传给工具的 Python 代码（必须包含 print()）
Observation: 工具返回的输出结果
...（Thought/Action/Action Input/Observation 可以重复多次）
Thought: 我现在知道最终答案了
Final Answer: 用中文给出最终答案

开始！

Question: {input}
Thought: {agent_scratchpad}"""

prompt = PromptTemplate.from_template(react_template)

# 4. 创建 Agent
agent = create_react_agent(llm, tools, prompt)

# 5. 用 AgentExecutor 运行
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=10
)

# 6. 提问
response = agent_executor.invoke({
    "input": "计算 123 乘以 456，然后告诉我结果的平方根是多少"
})

print("\n📌 最终答案：", response["output"])