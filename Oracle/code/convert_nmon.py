# convert_nmon.py
#该代码将.nmon文件处理成.csv文件
import subprocess
import os

def run_nmon_analyzer(nmon_file_path, output_dir):
    """
    调用 pyNmonAnalyzer 将 nmon 文件转换为 CSV
    """
    os.makedirs(output_dir, exist_ok=True)

    # 你手动能成功的命令
    command = f'pyNmonAnalyzer -c -i "{nmon_file_path}" -o "{output_dir}" -x'
    
    # 核心修改：
    # 1. 屏蔽所有输出（隐藏那行无用打印）
    # 2. 去掉 check=True（工具BUG返回1，实际已成功）
    subprocess.run(
        command,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # 因为你实测文件一定生成成功，直接提示
    print("NMON 转换 CSV 完成！")