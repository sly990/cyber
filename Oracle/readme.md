Oracle 数据库安全评估工具




项目概述
本项目用于自动化处理 Oracle 数据库的日常巡检数据，生成一份图文并茂的 HTML 安全评估报告。




输入文件包括：
nmon 性能数据
数据库配置检查文本
告警日志
AWR HTML 报告





工具将执行以下任务：
解析 nmon 文件，生成 CSV 并绘制 CPU、内存、网络等性能图表。
提取数据库配置参数、表空间使用率、ASM 磁盘信息等。
提取告警日志中的关键错误（ORA、ERROR 等）。
转换 AWR HTML 为 Markdown，提取性能指标（命中率、等待事件、TOP SQL）。
调用 DeepSeek API 对各项数据进行分析，给出结论和建议。
最终将所有图表、表格和分析结论整合到一个 HTML 报告 中。






目录结构说明
text
.
├── oral_file/                 # 原始数据输入目录（用户需放置以下文件）
│   ├── his02_250120_0800.nmon          # nmon 性能文件
│   ├── his02_health_check.txt          # 数据库配置检查输出（文本）
│   ├── his02_alert_orcl2_20250120.log  # 告警日志
│   └── his02_awrrpt_2_73343_73349.html # AWR HTML 报告
├── nmon_csv/                  # nmon 转换后的 CSV 文件（自动生成）
│   └── csv/                    # 各指标子目录
├── graph/                      # 生成的性能图表图片（自动生成）
├── extracted_file/             # 提取的中间文本文件（自动生成）
│   ├── database_check.txt       # 数据库配置检查提取结果
│   ├── database_error2.txt      # 告警日志错误提取结果
│   ├── report_summary.md        # AWR 转换后的 Markdown
│   ├── awr.txt                  # AWR 性能指标提取
│   └── sql.txt                  # TOP SQL 提取
├── requirements.txt            # Python 依赖包列表
├── readme.md                   # 本文件
├── code/                       # 主程序及模块目录（以下文件均位于 code/ 内）
│   ├── main_oracle.py          # 主入口脚本（执行此文件即可）
│   ├── data_processing.py      # 数据预处理，整合所有提取和绘图逻辑
│   ├── convert_nmon.py         # nmon 转 CSV 模块
│   ├── draw.py                 # CSV 绘图模块
│   ├── database_check.py       # 提取数据库配置
│   ├── database_error2.py      # 提取告警日志错误
│   ├── AWR_to_md.py            # AWR HTML 转 Markdown
│   ├── md_extract.py           # 从 Markdown 提取性能指标
│   ├── SQL.py                  # 提取 TOP SQL
│   ├── deepseek.py             # 调用 DeepSeek API 进行分析
│   ├── create_table.py         # 制作各类数据表格
│   └──  delete.py               # 清理之前生成的中间文件
└── oracle_report_YYYYMMDD_HHMMSS.html   # 最终生成的 HTML 报告（自动生成）






使用步骤

1. 环境准备
安装 Python 3.9+
安装依赖包：在项目根目录下执行
bash
pip install -r requirements.txt



2. 配置 DeepSeek API 密钥
在 code/deepseek.py 中（或环境变量）设置您的 API Key。



3. 准备输入文件
将以下文件放入 oral_file/ 目录：
nmon 文件：例如 his02_250120_0800.nmon
数据库配置检查文本：例如 his02_health_check.txt（通常由 database_check.sql 脚本生成）
告警日志：例如 his02_alert_orcl2_20250120.log
AWR HTML 报告：例如 his02_awrrpt_2_73343_73349.html
⚠️ 注意：如果文件名与代码中不一致，请修改 main_oracle.py 开头的路径变量。




4. 运行主程序
进入 code/ 目录，执行：
bash
python main_oracle.py



5. 查看输出
中间文件自动生成在 nmon_csv/、graph/、extracted_file/ 中，请不要删除这几个目录。
最终报告以 oracle_report_时间戳.html 命名，出现在项目根目录。







注意事项
1.请确保所有输入文件存在且格式正确，否则程序可能报错。

2.首次运行时会清理nmon_csv/、graph/、extracted_file/ 中的旧文件（由 delete.py 控制）。

3.DeepSeek 分析需要网络连接，且 API 调用可能产生费用，请确保账户余额充足。

4.如果不需要重新生成图表或提取数据，可以注释掉 main_oracle.py 中对应的处理部分，直接使用已有的中间文件。

5.报告格式为 HTML，可直接用浏览器打开查看。所有图片已转为 Base64 编码嵌入，无需额外文件。

6.代码中的锚点（如 "--- 预警：表空间使用率超过 85% ---"）用于定位数据提取区间，请勿随意修改。

7.自定义提示词
在 main_oracle.py 中可以修改 analyze_one_and_append_html、extract_analyze_and_append_html 等函数中的 prompt 参数，以调整 DeepSeek 的分析风格和结论长度。