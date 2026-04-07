# data_processing.py
import os
from convert_nmon import run_nmon_analyzer
from draw import csv_to_graph
from database_check import database_check
from database_error2 import extract_clean_report
from AWR_to_md import html_to_markdown_file
from md_extract import md_extract
from SQL import top_sql

def process_data(input_nmon, output_csv, cpu_csv, mem_csv, hugepages_csv, net_csv,
                 output_graph, source_file, target_file, input_log, output_txt,
                 input_html, output_md, input_md, output_awr1, output_sql):
    #==================这里为数据处理部分，可在extracted_file，graph和nmon_csv三个文件夹查看提取后的文件和数据图表======================
   
    #将.nmon文件处理成.csv文件
    run_nmon_analyzer(input_nmon,output_csv)
   
    #将.csv文件绘制成图表
    csv_to_graph(cpu_csv,mem_csv,hugepages_csv,net_csv,output_graph)
   
    #提取数据库配置检查部分
    database_check(source_file,target_file)
   
    #提取数据库错误检查部分
    keywords_to_check = ["ORA", "WARNING", "ERROR", "TERMINAL", "CHECKPOINT"]
    extract_clean_report(input_log, output_txt, keywords_to_check)
   
    #将AWR的html文件处理成markdown格式
    html_to_markdown_file(input_html, output_md)
   
    #提取数据库性能检查部分
    md_extract(input_md,output_awr1)

    #提取TOP SQL部分
    top_sql(input_md,output_sql)

    #=================================================================