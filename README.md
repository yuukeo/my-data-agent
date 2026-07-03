\# 智能数据分析 Agent
基于 LangChain 和智谱 GLM-4-Flash 的智能数据分析工具，用自然语言提问，自动分析 CSV 数据。
\## ✨ 功能
\- 🤖 用自然语言提问，AI 自动生成并执行 Python 代码
\- 📊 支持数据概览、分类汇总、趋势分析、利润分析、业务建议等维度
\- 🔄 代码出错时自动修正
\- 💬 分析结果用自然语言解释
\- 🆓 使用智谱 AI 免费额度，零成本运行
\## 🛠️ 技术栈
\- Python 3.9+
\- LangChain（模型调用）
\- 智谱 AI GLM-4-Flash（大语言模型）
\- Pandas（数据处理）
\## 🚀 快速开始
\### 1. 克隆仓库
git clone https://github.com/yuukeo/my-data-agent.git
cd my-data-agent
\### 2. 创建虚拟环境并安装依赖
python -m venv venv
venv\\Scripts\\activate  # Windows
\# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
\### 3. 配置 API 密钥
在项目根目录创建 `.env` 文件，写入：
ZHIPU\_API\_KEY=你的智谱API密钥
免费获取地址：https://open.bigmodel.cn/
\### 4. 准备数据
将你的 CSV 文件放在 `data/` 文件夹中。
\### 5. 运行
python data\_agent.py
\## 📊 示例分析
输入示例数据 `data/sales.csv`：
| 月份 | 产品 | 销售量 | 单价 | 成本 |

|------|------|--------|------|------|

| 2024-01 | 手机 | 120 | 3000 | 2000 |

| 2024-01 | 电脑 | 45 | 6000 | 4200 |

| ... | ... | ... | ... | ... |

提问：
\- "哪个产品的平均销售额最高？" → 手机

\- "哪个月利润率最高？" → 2024年2月，38.06%

\- "给出两条业务优化建议。" → 库存和促销策略

\## 📁 项目结构

├── .env # API 密钥（不提交）

├── .gitignore # 忽略规则

├── README.md # 项目说明

├── requirements.txt # 依赖清单

├── hello\_ai.py # 入门：和 AI 说第一句话

├── chain\_demo.py # 进阶：提示词模板

├── data\_agent.py # 核心：数据分析 Agent

└── data/

└── sales.csv # 示例数据





