import os
import pandas as pd
import io
import sys
from dotenv import load_dotenv
from langchain_community.chat_models import ChatZhipuAI

load_dotenv()

# ==================== 1. 加载数据 ====================
df = pd.read_csv("datasales.csv")
print("✅ 数据加载成功，形状：", df.shape)
print(df.head())

# 把数据的前 5 行和列信息转成文本，作为上下文给模型
data_context = f"""
数据列名：{list(df.columns)}
数据类型：
{df.dtypes.to_string()}

数据前5行：
{df.head().to_string()}
"""

# ==================== 2. 创建模型 ====================
llm = ChatZhipuAI(
    model="glm-4-flash",
    temperature=0,
    api_key=os.getenv("ZHIPU_API_KEY")
)

# ==================== 3. 定义函数：执行代码并捕获输出 ====================
def execute_python_code(code):
    """执行 Python 代码，返回 print() 输出的内容"""
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try:
        exec(code, {"df": df, "pd": pd})
        output = new_stdout.getvalue()
        if output.strip() == "":
            output = "代码执行成功，但没有 print() 输出。请用 print() 输出结果。"
    except Exception as e:
        output = f"代码执行出错：{str(e)}"
    finally:
        sys.stdout = old_stdout
    return output

# ==================== 4. 核心分析循环 ====================
def ask_agent(question, max_attempts=3):
    """向 Agent 提问，最多尝试 max_attempts 次"""
    
    # 第 1 步：让模型生成 Python 代码
    code_prompt = f"""你是一个数据分析助手。根据以下数据信息，生成 Python 代码来回答用户的问题。

{data_context}

用户问题：{question}

请只输出 Python 代码，不要输出任何解释。代码中必须用 print() 输出最终结果。
变量 df 是已经加载好的 DataFrame，可以直接使用。
注意：
- 如果计算利润，要先算每行的利润（销售量 * (单价 - 成本)），再按维度汇总。
- 避免出现 nan，确保数值列都是有效数字。
"""

    for attempt in range(max_attempts):
        print(f"\n{'='*50}")
        print(f"🔄 第 {attempt+1}/{max_attempts} 次尝试")
        print(f"{'='*50}")

        # 生成代码
        code_response = llm.invoke(code_prompt)
        code = code_response.content.strip()
        
        # 去掉可能的 markdown 代码块标记
        if code.startswith("```python"):
            code = code[9:]
        if code.startswith("```"):
            code = code[3:]
        if code.endswith("```"):
            code = code[:-3]
        code = code.strip()

        print(f"📝 生成的代码：\n{code}")

        # 执行代码
        print(f"\n🔧 执行结果：")
        result = execute_python_code(code)
        print(result)

        # 如果执行成功且不是错误提示，跳出循环
        if not result.startswith("代码执行出错") and "没有 print() 输出" not in result and "nan" not in result.lower():
            break
        else:
            # 把错误信息加入提示，让模型修正
            code_prompt += f"\n\n上一次代码执行结果：{result}\n请修正代码。"
    
    # 第 2 步：让模型用自然语言解释结果
    explanation_prompt = f"""根据以下信息，用中文简洁地回答用户的问题。

{data_context}

用户问题：{question}

代码执行结果：{result}

请用自然语言给出答案，不需要输出代码。"""

    explanation = llm.invoke(explanation_prompt)
    return explanation.content
# ==================== 5. 测试 ====================
# ==================== 5. 测试 ====================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🤖 智能数据分析 Agent 启动")
    print("="*60)

    questions = [
        "哪个产品的平均销售额最高？",
        "计算每个月的总成本和总利润，哪个月利润率最高？",
        "按产品统计总销售量，并用一句话总结销售情况。",
        "给出两条业务优化建议。",
    ]

    for q in questions:
        print(f"\n❓ 问题：{q}")
        answer = ask_agent(q)
        print(f"\n📌 最终答案：{answer}")
        print("\n" + "-"*50)