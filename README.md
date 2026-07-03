这是一个智能数据分析 Agent————一个基于 LangChain 和智谱 AI 的智能数据分析工具，能用自然语言提问，自动分析 CSV 数据并给出结论。

它能做什么？
- 你用人话提问，AI 自动写 Python 代码来分析数据
- 支持数据概览、分类汇总、趋势分析、利润分析、业务建议等维度
- 代码写错了会自动修正，不需要你懂编程
- 分析结果用中文解释，直接可读
- 使用智谱 AI 免费额度，不用花钱

使用了什么技术栈？
- Python 3.9+
- LangChain（模型调用）
- 智谱 AI GLM-4-Flash（大语言模型）
- Pandas（数据处理）

怎么跑起来？
1.克隆仓库
终端内-git clone https://github.com/yuukeo/my-data-agent.git
cd my-data-agent
2.创建虚拟环境并安装依赖
终端内-python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
3.配置api秘钥
在项目根目录创建 .env 文件，写入：
终端内-ZHIPU_API_KEY=你的智谱API密钥
4.准备数据
把 CSV 文件放到 data/ 文件夹里。
5.运行
python data_agent.py

运行效果
输入示例数据 data/sales.csv：
月份	产品	销售量	单价	成本
2024-01	手机	120	3000	2000
2024-01	电脑	45	6000	4200
2024-02	手机	150	2950	2000
2024-02	电脑	55	5900	4200
2024-03	手机	130	3100	2100
2024-03	电脑	48	6200	4300

提问与回答：
销售额最高的是哪个月？
2024年2月的销售额最高。
哪种产品的总利润最高？
手机的总利润最高。
哪个月利润率最高？
2024年2月，利润率38.06%。

项目结构
├── .env                # API 密钥（不提交）
├── .gitignore          # 忽略规则
├── README.md           # 项目说明
├── requirements.txt    # 依赖清单
├── hello_ai.py         # 入门：和 AI 说第一句话
├── chain_demo.py       # 进阶：提示词模板
├── data_agent.py       # 核心：数据分析 Agent
└── data/
    └── sales.csv       # 示例数据



