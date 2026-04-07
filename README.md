# 网络与数据安全巡检预案生成助手
本项目是一个基于 Streamlit 的智能助手，结合 RAG（检索增强生成） 与 Agent 工具调用，实现网络与数据安全巡检预案生成功能。



# 主要功能
网络安全预案生成：基于本地《Web-Sec Documentation》PDF 文档，生成结构化、专业的安全预案。
混合检索（向量 + 关键字）：使用 FAISS（或内存向量库）与 Elasticsearch 进行文档召回。
重排序（Rerank）优化：对召回文档进行精排，提升上下文质量。
联网搜索补充：当本地文档信息不足时，通过 DuckDuckGo + trafilatura 获取最新信息。
Oracle 数据库巡检工具：调用外部脚本生成 HTML 报告，并在界面中提供下载。
智能对话管理：自动判断用户意图，区分通用问答与专业安全查询。



# 环境要求
操作系统：Windows / Linux
Python：3.10.17
Elasticsearch：9.0.1（可选，用于关键字检索）
Oracle 巡检脚本（可选）：需提前准备 main_oracle.py 及相关数据目录





# 快速开始
1. 安装 Elasticsearch（可选）
若需要使用关键字检索，请先安装 Elasticsearch 并启动：

bash
进入 elasticsearch 的 bin 目录
cd G:\BiShe\cyber\elasticsearch-9.0.1-windows-x86_64\elasticsearch-9.0.1\bin
elasticsearch.bat
若不需要关键字检索，可跳过此步，系统将仅使用向量检索。



2. 创建并激活 Conda 环境
bash
conda create -n rag_cyber python=3.10.17
conda activate rag_cyber



3. 安装依赖
进入项目根目录（包含 requirements.txt）后执行：

bash
pip install -r requirements.txt



4. 配置 API 密钥
在代码文件 rag_cyber.py 中设置通义千问 API 密钥：

python
os.environ["TONGYI_API_KEY"] = "sk-xxxxxx"



5. 准备模型与文档
Embedding 模型：默认路径为 G:\BiShe\cyber\models\xiaobu-embedding-v2，请确保该路径存在或自行修改。

PDF 文档：默认使用 G:\BiShe\cyber\data_pdf\merged_pdfs\websec-readthedocs-io-zh-latest.pdf，请根据实际情况修改代码中的路径。



6. 启动应用
bash
streamlit run rag_cyber.py



# 项目结构

cyber/                                 # 项目根目录
├── code_all_versions/                 # 历史代码版本/备份目录
├── data_pdf/                          # PDF 原始数据目录
├── elasticsearch-9.0.1-windows-x86_64/ # Elasticsearch 本地服务目录
├── models/                            # 本地模型目录
│   ├── all-MiniLM-L6-v2/              # 重排序模型
│   └── xiaobu-embedding-v2/           # 向量模型
├── Oracle/                            # Oracle 数据库检查程序
├── vector_store/                      # 向量库缓存目录
├── agent.py                           # Agent 调用入口
├── chunk_cyber.py                     # 文档切分模块
├── delete.py                          # 清理/删除相关脚本
├── download.py                        # 下载相关脚本
├── local_search.py                    # 本地检索模块
├── net_search.py                      # 联网搜索模块
├── ocr.py                             # OCR 识别模块
├── rag_cyber.py                       # RAG 主程序入口
├── ReadME.md                          # 项目说明文档
├── requirements.txt                   # Python 依赖列表
├── rerank.py                          # 重排序模块
└── tool_DataCheck.py                  # 调用Oracle 数据库检查工具函数


# 使用说明

利用本地知识库生成预案：
“生成一份完整的企业 Web 应用网络安全防护与应急处置预案”

数据库巡检：
先在侧边栏上传 .nmon / .txt / .log 等文件，然后输入：
“开始数据库巡检”
系统将调用 Oracle 巡检工具，并在回复中提供 HTML 报告下载按钮。

联网查询：
“2024年最新的 Log4j 漏洞修复方案是什么？”



# 常见问题
Q1: 启动后提示“向量数据库初始化失败”
检查 data_pdf/merged_pdfs/ 下是否存在可用的 PDF 文件。

确认 embedding 模型路径是否正确。

若仍失败，可查看控制台错误日志。


Q2: Elasticsearch 未连接
系统会自动降级为纯向量检索，不影响基础问答功能。


Q3: Oracle 巡检工具调用失败
确保 Oracle/code/main_oracle.py 文件存在且可执行。

确认已通过侧边栏上传了必要的源文件。

检查 Python 环境是否包含巡检脚本所需的依赖。


Q4: 联网搜索无结果
网络环境可能需要代理，请确保能访问 DuckDuckGo。

部分网站可能被防火墙拦截，可尝试调整 trafilatura 的抓取逻辑。



# 注意事项
首次启动会自动切分 PDF 并构建向量库，耗时约几分钟，之后会缓存至 vector_store/ 目录。

请勿在公共环境中暴露 API 密钥。

若需更换 LLM 模型，可修改 ChatTongyi 的 model_name 参数，或替换为其他 LangChain 兼容模型
