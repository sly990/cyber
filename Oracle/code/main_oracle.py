import os

from deepseek import analyze_one_and_append_html,analyze_two_csv_and_append_html,extract_analyze_and_append_html,\
analyze_visible_text_and_append_html
from datetime import datetime
from delete import clean_oracle_data
import mammoth
from bs4 import BeautifulSoup
from docx.oxml.ns import qn
from docx import Document
import re
import base64
import re
import html
from data_processing import process_data
from create_table import extract_and_append_as_table_html,\
extract_and_append_as_table_html_database, extract_multi_tables_append_html



# .nmon文件的路径和输出的csv文件所在文件夹
input_nmon = r"../oral_file/his02_250120_0800.nmon"
output_csv = r"../nmon_csv"

# 各个绘制的图表所需要的csv文件的位置
cpu_csv = os.path.join(output_csv, "csv", "CPU_ALL.csv")
mem_csv = os.path.join(output_csv, "csv", "MEM.csv")
hugepages_csv = os.path.join(output_csv, "csv", "HUGEPAGES.csv")
net_csv = os.path.join(output_csv, "csv", "NET.csv")

#csv文件绘制得到的图表的文件夹
output_graph = r"../graph"

#图表的位置
cpu_graph = os.path.join(output_graph,  "CPU_ALL.png")
mem_graph = os.path.join(output_graph,  "MEM_memory.png")
hugepages_graph = os.path.join(output_graph,  "HUGEPAGES_hugepages.png")
net_graph= os.path.join(output_graph, "nets.png")

# 数据库配置检查相关文件
source_file = r'../oral_file/his02_health_check.txt'
target_file = r'../extracted_file/database_check.txt'

# 数据库错误检查相关文件
keywords_to_check = ["ORA", "WARNING", "ERROR", "TERMINAL", "CHECKPOINT"]
input_log = r"../oral_file/his02_alert_orcl2_20250120.log"
output_txt = r"../extracted_file/database_error2.txt"

# AWR相关
input_html = r'../oral_file/his02_awrrpt_2_73343_73349.html'
output_md = r'../extracted_file/report_summary.md'
input_md = r'../extracted_file/report_summary.md'
output_awr1 = r"../extracted_file/awr.txt"
output_sql = r"../extracted_file/sql.txt"


#生成报告
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
html_path = f"../oracle_report_{timestamp}.html"


#将图片转化为编码形式，便于在html中显示
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
        return f"data:image/png;base64,{encoded}"


def main():
    
    
    #清除缓存,清除上次生成报告得到的中间文件
    clean_oracle_data()
   
   #数据处理
    process_data(input_nmon, output_csv, cpu_csv, mem_csv, hugepages_csv, net_csv,
                output_graph, source_file, target_file, input_log, output_txt,
                input_html, output_md, input_md, output_awr1, output_sql)
    
    
    
    
#=================以下是生成html报告部分========================================================================


    #CPU使用率
    cpu_text = "CPU使用率"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{cpu_text}</p>\n')
    
    #插入CPU使用率的图表
    cpu_graph_base64 = image_to_base64(cpu_graph)
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<img src="{cpu_graph_base64}" style="width:100%; max-width:800px; height:auto;">\n')
    
    # CPU结论
    analyze_one_and_append_html({
    "name": "CPU诊断结论",
    "file": cpu_csv,
    "columns": ["User%", "Sys%", "Wait%"],
    "prompt": "你是一位资深的 Oracle 数据库性能分析专家。以下是某段时间内 Oracle 数据库的 CPU 使用率数据（CSV 格式）\
         请根据 User%、Sys%、Wait% 这三个指标，判断当前 CPU 资源是否满足业务需求。你的分析需要严谨专业。100字以内\
         请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，\
         不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }, html_path)
    


    #内存使用率
    mem_text = "内存使用率"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{mem_text}</p>\n')
    
    #插入内存1使用率的图表
    mem_graph_base64 = image_to_base64(mem_graph)
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<img src="{mem_graph_base64}" style="width:100%; max-width:800px; height:auto;">\n')
    
    #插入内存2使用率的图表
    hugepages_graph_graph_base64 = image_to_base64(hugepages_graph)
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<img src="{hugepages_graph_graph_base64}" style="width:100%; max-width:800px; height:auto;">\n')
    
    # 内存 + HUGEPAGES结论
    analyze_two_csv_and_append_html({
        "name": "内存诊断结论",
        "file1": mem_csv,
        "columns1": ["memfree", "inactive", "active"],
        "file2": hugepages_csv,
        "prompt": "你是一位资深的 Oracle 数据库性能分析专家。以下是某段时间内 Oracle 数据库的两个内存有关的利用率数据（CSV 格式）\
         请根据两个文件的数据，判断当前内存资源是否满足业务需求。你的分析需要严谨专业。100字以内\
         请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，\
         不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
    }, html_path)


    #网络使用情况
    net_text = "网络使用情况"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{net_text}</p>\n')
    
    #插入网络使用情况的图表
    net_graph_base64 = image_to_base64(net_graph)
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<img src="{net_graph_base64}" style="width:100%; max-width:800px; height:auto;">\n')

    #网络使用情况结论
    analyze_one_and_append_html({
        "name": "网络诊断结论",
        "file": net_csv,
        "columns": [
            "public-read-KB/s",
            "private-read-KB/s",
            "public-write-KB/s",
            "private-write-KB/s"
        ],
        "prompt": "你是一位资深的 Oracle 数据库性能分析专家。以下是某段时间内 Oracle 数据库的网络使用情况的数据（CSV 格式）\
         请根据数据，判断当前网络流量是否正常，是否达到万兆网络瓶颈。你的分析需要严谨专业。100字以内\
         请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，\
         不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
    }, html_path)
    
    
    
    
    # 数据库版本分析
    version_text = "数据库版本分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{version_text}</p>\n')
        
    #数据库版本结论
    extract_analyze_and_append_html(
        source_file=target_file,
        html_path=html_path,
        task={
            "name": "数据库版本分析",
            "start": "数据库版本号和实例名",
            "end": "数据库初始化参数",
            "prompt": "以下是oracle数据库的版本信息，请指出版本号，判断是否为最新版本，并给出建议，结论100字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )


    # 数据库参数分析
    param_text = "数据库参数分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{param_text}</p>\n')
        
    #数据库参数结论
    extract_analyze_and_append_html(
        source_file=target_file,
        html_path=html_path,
        task={
            "name": "数据库参数分析",
            "start": "数据库初始化参数",
            "end": "当前用户数",
            "prompt": "以下是oracle数据库的初始参数信息，请分析参数设置是否合理，是否需要改动，结论100字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # RAC数据库配置检查分析
    rac_text = "RAC数据库配置检查分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{rac_text}</p>\n')
    
    #生成小表格以及结论
    extract_analyze_and_append_html(
        source_file=target_file,
        html_path=html_path,
        task={
            "name": "RAC数据库配置检查分析",
            "start": "当前用户数",
            "end": "控制文件的信息",
            "prompt": "以下是oracle数据库的RAC数据库配置，包括当前用户数和磁盘信息，请先以表格的形式分别完整列出2个实例的连接数\
            和ASM磁盘空间，然后请分析数据库会话数总计多少，"
            "请注意，列出的表格数据一定要完整，数据与表头对齐，请不要翻译里面的数据，不要添加多余信息"
                    "ASM磁盘组使用了多少，剩余多少，使用率为多少。结论300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )




    # 控制日志和在线日志文件分析
    log_text = "控制日志和在线日志文件分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{log_text}</p>\n')
        
    # 控制日志
    log1_text = "控制日志"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{log1_text}</p>\n')
        
        
    # 控制日志文件表格
    extract_and_append_as_table_html_database(
    html_path,
    txt_path=target_file,
    start_marker="控制文件的信息",
    end_marker="日志文件信息"
)
    
    # 在线日志
    log2_text = "在线日志"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{log2_text}</p>\n')
        
    # 在线日志文件表格
    extract_multi_tables_append_html(
        html_path,
        txt_path=target_file,
        start_marker="日志文件信息",
        end_marker="临时文件使用情况"
        )
    
    #控制日志和在线日志文件结论
    extract_analyze_and_append_html(
        source_file=target_file,
        html_path=html_path,
        task={
            "name": "控制日志和在线日志文件分析",
            "start": "控制文件的信息",
            "end": "临时文件使用情况",
            "prompt": "以下是oracle数据库的控制日志文件和在线日志文件的信息，\
                并分析文件是否有冗余，状态是否正常，300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # 临时文件分析
    temp_text = "临时文件分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{temp_text}</p>\n')
        
    #临时文件表格
    extract_and_append_as_table_html_database(
    html_path,
    txt_path=target_file,
    start_marker="临时文件使用情况",
    end_marker="--- 预警：表空间使用率超过 85% ---"
)
    #临时文件结论
    extract_analyze_and_append_html(
        source_file=target_file,
        html_path=html_path,
        task={
            "name": "临时文件分析",
            "start": "临时文件使用情况",
            "end": "--- 预警：表空间使用率超过 85% ---",
            "prompt": "以下是oracle数据库的临时文件使用情况，\
                并分析临时表空间的设置是否满足目前数据库的使用，300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # 表空间和数据文件部分分析
    tablespace_text = "表空间和数据文件部分分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{tablespace_text}</p>\n')
        
    # 使用率超过 85%的表空间
    log3_text = "使用率超过 85%的表空间"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{log3_text}</p>\n')
        
    #表空间使用率超过 85%
    extract_and_append_as_table_html_database(
    html_path,
    txt_path=target_file,
    start_marker="--- 预警：表空间使用率超过 85% ---",
    end_marker="--- 数据文件自动扩展信息 (仅保留 AUT=YES) ---"
)
    
     #使用自动扩展的文件
    log4_text = "使用自动扩展的文件"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{log4_text}</p>\n')
        
    #使用自动扩展的文件表格
    extract_and_append_as_table_html_database(
    html_path,
    txt_path=target_file,
    start_marker="--- 数据文件自动扩展信息 (仅保留 AUT=YES) ---",
    end_marker="over!"
)
    #表空间和数据文件部分结论
    extract_analyze_and_append_html(
        source_file=target_file,
        html_path=html_path,
        task={
            "name": "表空间和数据文件部分分析",
            "start": "--- 预警：表空间使用率超过 85% ---",
            "end": "over!",
            "prompt": "以下是oracle数据库的数据库使用率超过85％的表空间，和使用自动扩展的数据文件。"
                    "并分析哪几个表空间的使用率已超过85%，并给出建议，,300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # ========================= 错误日志分析任务 =========================
    error_text = "数据库错误日志分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{error_text}</p>\n')
    extract_analyze_and_append_html(
        source_file=output_txt,
        html_path=html_path,
        task={
            "name": "数据库错误日志分析",
            "start": "--- Oracle 数据库异常事件分析报告 ---",
            "end": "over!",
            "prompt": "以下是oracle数据库的错误日志，请检查是否有特别致命的错误，\
                  先列出一下比较严重的错误事件,然后对其进行分析，并给出建议，分析和建议务必要详细。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要出现事件的序号，例如事件1等"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # ========================= AWR 报告分析任务 =========================
    # 选取的时间段
    time_text = "数据库性能检查选取的时间段"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{time_text}</p>\n')
        
    
    extract_analyze_and_append_html(
        source_file=output_awr1,
        html_path=html_path,
        task={
            "name": "数据库实例性能的各项命中率",
            "start": "系统工作峰值时间段",
            "end": "数据库实例性能的各项命中率",
            "prompt": "以下是oracle数据库系统工作时间段数据，"
            "请以表格的形式列出所有内容"
            "请注意，列出的表格数据一定要完整，数据与表头对齐，请不要翻译里面的数据，不要遗漏数据"
                "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。"
        }
    )
    # 数据库实例命中率分析
    hit_text = "数据库实例命中率分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{hit_text}</p>\n')
        
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_awr1,
    start_marker="数据库实例性能的各项命中率",
    end_marker="数据库实例资源消耗时间模型"
)
    

    extract_analyze_and_append_html(
        source_file=output_awr1,
        html_path=html_path,
        task={
            "name": "数据库实例命中率分析",
            "start": "数据库实例性能的各项命中率",
            "end": "数据库实例资源消耗时间模型",
            "prompt": "以下是oracle数据库的实例性能的各项命中率，"
                    "对于命中率低于85%的指标，解释它是什么，并分析其命中率低的原因。300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # 数据库实例资源消耗时间模型分析
    time_model_text = "数据库实例资源消耗时间模型分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{time_model_text}</p>\n')

    extract_and_append_as_table_html(
    html_path,
    txt_path=output_awr1,
    start_marker="数据库实例资源消耗时间模型",
    end_marker="数据库前台等待事件Top10"
)
        
    extract_analyze_and_append_html(
        source_file=output_awr1,
        html_path=html_path,
        task={
            "name": "数据库实例资源消耗时间模型分析",
            "start": "数据库实例资源消耗时间模型",
            "end": "数据库前台等待事件Top10",
            "prompt": "以下是oracle数据库数据库实例资源消耗时间模型数据，"
                    "分析系统的资源消耗情况。"
                    "然后通过观察时间模型，判断数据库实例资源消耗是否正常。"
                    "300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # 数据库等待事件分析
    wait_text = "数据库等待事件分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{wait_text}</p>\n')
        

    extract_and_append_as_table_html(
    html_path,
    txt_path=output_awr1,
    start_marker="数据库前台等待事件Top10",
    end_marker="over!"
)
    extract_analyze_and_append_html(
        source_file=output_awr1,
        html_path=html_path,
        task={
            "name": "数据库等待事件分析",
            "start": "数据库前台等待事件Top10",
            "end": "over!",
            "prompt": 
                    "以下是一些Oracle 数据库常见的等待事件:\
db file sequential read含义：会话正在等待一个单块物理 I/O 操作完成。典型场景：索引查找、通过 ROWID 访问表。分析方向：索引效率低下、连接顺序不佳或 I/O 子系统延迟高。\
db file scattered read含义：会话正在等待一个多块物理 I/O 操作完成。典型场景：全表扫描或索引快速全扫描。分析方向：缺少索引、统计信息陈旧导致优化器选择全表扫描。\
buffer busy waits含义：会话尝试访问缓冲区缓存中的数据块，但该块正被其他会话占用。典型场景：热点块争用（数据块、索引块、段头）。分析方向：调整 PCTFREE / INITRANS、优化热点块、使用 ASSM。\
log file sync含义：用户会话在 COMMIT 后，等待 LGWR 将重做记录写入日志文件。典型场景：提交过于频繁、重做日志 I/O 缓慢。分析方向：优化事务提交频率、检查存储 I/O 性能。\
enq: TX - row lock contention含义：会话正在等待被其他会话持有的行级锁。典型场景：业务逻辑导致并发更新同一行、长事务未提交。分析方向：审查应用事务逻辑、检查是否存在未提交的长事务。\
cursor: pin S wait on X含义：会话正在等待一个被其他会话以排他模式持有的 Mutex（互斥锁），通常发生在 SQL 解析阶段。典型场景：高并发硬解析、SQL 版本过高（Version Count High）。分析方向：检查绑定变量使用情况、分析 V$SQLAREA 的 VERSION_COUNT、或 SESSION_CACHED_CURSORS 参数的设置。\
row cache lock含义：会话在访问或修改数据字典缓存时发生争用。典型场景：序列（Sequence）配置不当（如 NOCACHE）、频繁的 DDL 操作。分析方向：重点检查序列的 CACHE 设置。\
latch: cache buffers chains含义：会话在搜索缓冲区缓存哈希链表时，无法获取保护该链表的闩锁。典型场景：严重的热点块问题导致特定哈希链被过度扫描。分析方向：定位并优化 SQL 语句，减少逻辑读。\
gc buffer busy acquire /gc cr block busy（RAC 环境）含义：RAC 环境下，本地实例请求远程实例的数据块时发生等待。典型场景：跨实例的数据块争用、私网互联延迟。分析方向：优化跨实例访问的数据分布、检查 RAC 私网性能。\
latch: shared pool含义：会话在 Shared Pool（共享池）中分配内存或查找对象时，无法获取保护 Shared Pool 内存结构的闩锁。典型场景：硬解析过载；共享池碎片化。分析方向：使用绑定变量；调整共享池内存；极端情况调整隐含参数。"
                    "我现在给你一些我的oracle数据库里面的等待事件，"
                    "请参考我给你提供常见的等待事件，解释我的oracle数据库里面的等待事件的含义,\
                    并列出值得关注的等待事件，最后给出你的建议"
                    "300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )

    # ========================= TOP SQL 分析任务 =========================
    sql_text = "TOP SQL分析"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{sql_text}</p>\n')
    
    
    sql1_text = "SQL ordered by Elapsed Time"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{sql1_text}</p>\n') 
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_sql,
    start_marker="SQL ordered by Elapsed Time",
    end_marker="SQL ordered by CPU Time"
)
    
    sql2_text = "SQL ordered by CPU Time"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{sql2_text}</p>\n')   
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_sql,
    start_marker="SQL ordered by CPU Time",
    end_marker="SQL ordered by Gets"
)


    sql3_text = "SQL ordered by Gets"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{sql3_text}</p>\n')   
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_sql,
    start_marker="SQL ordered by Gets",
    end_marker="SQL ordered by Reads"
)
    
    sql4_text = "SQL ordered by Reads"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{sql4_text}</p>\n')   
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_sql,
    start_marker="SQL ordered by Reads",
    end_marker="SQL ordered by Executions"
)    
    


    sql5_text = "SQL ordered by Executions"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{sql5_text}</p>\n')   
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_sql,
    start_marker="SQL ordered by Executions",
    end_marker="SQL ordered by Parse Calls"
)    
    
    sql6_text = "SQL ordered by Parse Calls"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:20px; font-weight:bold;">{sql6_text}</p>\n')   
    extract_and_append_as_table_html(
    html_path,
    txt_path=output_sql,
    start_marker="SQL ordered by Parse Calls",
    end_marker="over!"
)    
    
    
    
    extract_analyze_and_append_html(
        source_file=output_sql,
        html_path=html_path,
        task={
            "name": "TOP SQL分析",
            "start": "SQL ordered by Elapsed Time",
            "end": "over!",
            "prompt": "以下是oracle数据库的TOP SQL分析,包括SQL ordered by Elapsed Time，"
                    "SQL ordered by CPU Time , SQL ordered by Gets, SQL ordered by Reads"
                    "SQL ordered by Executions以及SQL ordered by Parse Calls。"
                    "请分析监控时间段内系统的前端业务反映是否正常，"
                    "有没有发现长时间和能够导致业务正常运行的等待事件。"
                    "并给出建议。"
                    "300字以内。"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
)
    
    final_text = "总结"
    with open(html_path, "a", encoding="utf-8") as f:
        f.write(f'<p style="font-size:40px; font-weight:bold;">{final_text}</p>\n')

    analyze_visible_text_and_append_html(
        source_file=html_path,   # 这里直接传入当前生成的 HTML 文件
        html_path=html_path,
        task={
            "name": "总结",
            "prompt": "以下是oracle数据库的健康检查报告"
                    "请对以下数据库健康检查报告内容进行总结，提取主要问题，并严格按照如下格式输出（每一行一个问题）：\
                    NO：序号\
                    问题描述：xxx\
                    参考章节：xxx\
                    建议解决时间：尽快"
                    "注意：\
                    1. 严格按照字段输出\
                    2. 不要添加额外解释\
                    3. 多个问题按顺序编号"
                    "\n请注意，严禁使用“好的”、“作为一名资深专家”、“根据您提供的文档”等开场白，"
                    "不要输出任何承诺性或自我介绍的语言。请直接输出分析结论和具体建议。"
        }
    )



    return 0
   
   
if __name__ == "__main__": 
    main()