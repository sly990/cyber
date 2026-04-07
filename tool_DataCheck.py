import os
import streamlit as st
import subprocess
import glob

# 定义工具调用的逻辑
def tool_oracle_inspection(query: str):
    """调用外部 Oracle 巡检脚本并获取报告路径"""
    # 1. 提示用户正在处理
    st.toast("🚀 正在启动 Oracle 数据库安全评估程序...", icon="⏳",duration=3600)
    
    try:
        # 2. 执行你的主程序（请确保 code 文件夹路径正确）
        # 如果 main_oracle.py 在 G:\BiShe\cyber\Oracle\code 目录下
        script_dir = r"G:\BiShe\cyber\Oracle\code" 
        result = subprocess.run(
            ["python", "main_oracle.py"],
            cwd=script_dir,
            capture_output=True,
            text=True,
            encoding='gbk',  # Windows 环境下建议使用 gbk
            errors='ignore'  # 即使有字符解不出来也跳过，保证程序不中断
        )
        
        if result.returncode != 0:
            return f"脚本执行出错：{result.stderr}"

        # 3. 在目标目录搜索最新的报告
        report_dir = r"G:\BiShe\cyber\Oracle"
        # 匹配所有 oracle_report_*.html 文件
        list_of_files = glob.glob(os.path.join(report_dir, "oracle_report_*.html"))
        
        if not list_of_files:
            return "巡检完成，但在目录中未找到生成的报告文件。"

        # 获取最新创建的文件
        latest_file = max(list_of_files, key=os.path.getctime)
        
        # 将路径存入 session_state 供前端下载按钮读取
        st.session_state['latest_report'] = latest_file
        
        return f"分析完成！报告已生成：{os.path.basename(latest_file)}。请告知用户点击下方的下载按钮查看详细安全评估报告。"

    except Exception as e:
        return f"工具调用异常: {str(e)}"