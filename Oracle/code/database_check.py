import re

# 1. 提取数据库版本并【创建/重置】文件 (原有代码不变)
def extract_oracle_info(file_path, output_file):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        version_match = re.search(r'VERSION\s*-+\s*([^\n]+)', content)
        db_version = version_match.group(1).strip() if version_match else "未找到版本信息"
        instance_match = re.search(r'INSTANCE_NAME\s*-+\s*(\w+)', content)
        instance_name = instance_match.group(1).strip() if instance_match else "未找到实例名"
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("=" * 60 + "\n")
            f_out.write(f"【数据库版本】: {db_version}\n")
            f_out.write(f"【实例名】: {instance_name}\n")
            f_out.write("=" * 60 + "\n\n")
        print("1. 基础信息已写入。")
        return db_version, instance_name
    except Exception as e:
        print(f"提取版本出错: {e}")

# 通用的区间提取函数 (原有代码不变)
def append_section(input_file, output_file, start_kw, end_kw, section_name):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        start_idx = content.find(start_kw)
        end_idx = content.find(end_kw)
        if start_idx != -1:
            extracted = content[start_idx:].strip() if end_idx == -1 else content[start_idx:end_idx].strip()
            with open(output_file, 'a', encoding='utf-8') as f_out:
                f_out.write(extracted + "\n\n")
                f_out.write("-" * 60 + "\n\n")
            print(f"成功追加: {section_name}")
    except Exception as e:
        print(f"提取 {section_name} 出错: {e}")

# 2. 筛选高使用率表空间 (保持之前的逻辑)
def append_high_usage_tablespaces(input_file, output_file, threshold=85.0):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        start_pos = content.find("表空间使用情况")
        end_pos = content.find("rows selected.", start_pos)
        if start_pos == -1: return
        lines = content[start_pos:end_pos].split('\n')
        with open(output_file, 'a', encoding='utf-8') as f_out:
            f_out.write("--- 预警：表空间使用率超过 85% ---\n")
            f_out.write("TABLESPACE                   SUM_SPACE(M) SUM_BLOCKS USED_SPACE(M) USED_RATE(%) FREE_SPACE(M)\n")
            f_out.write("---------------------------- ------------ ---------- ------------- ------------ -------------\n")
            for line in lines:
                parts = line.split()
                if len(parts) >= 5:
                    try:
                        if float(parts[-2]) > threshold: f_out.write(line.strip() + "\n")
                    except: continue
            f_out.write("-" * 60 + "\n\n")
        print("2. 高使用率表空间已追加。")
    except Exception as e: print(f"筛选表空间出错: {e}")

# --- 新增：筛选 AUT 为 YES 的数据文件 ---
def append_autoextend_files(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 定位区间
        start_idx = content.find("数据文件大小与自动扩展")
        end_idx = content.find("total", start_idx)
        if start_idx == -1: return

        lines = content[start_idx:end_idx].split('\n')
        
        with open(output_file, 'a', encoding='utf-8') as f_out:
            f_out.write("--- 数据文件自动扩展信息 (仅保留 AUT=YES) ---\n")
            f_out.write("   FILE_ID TABLESPACE_NAME                AUT       MBYTES  MAXGBYTES\n")
            f_out.write("---------- ------------------------------ --- ------------ ----------\n")
            
            for line in lines:
                # 检查行中是否包含 YES，并且不是表头或分割线
                if "YES" in line and "FILE_ID" not in line and "---" not in line:
                    f_out.write(line.strip() + "\n")
            
            f_out.write("-" * 60 + "\n\n")
            f_out.write("over!")
        print("3. 已筛选并追加自动扩展文件。")
    except Exception as e:
        print(f"筛选自动扩展文件出错: {e}")

def database_check(source_file,target_file):

    # extract_oracle_info(source_file, target_file)
    append_section(source_file, target_file, "数据库版本号和实例名", "当前用户数", "数据库版本号和实例名部分")
    append_section(source_file, target_file, "数据库初始化参数", "数据库系统信息", "初始化参数部分")
    append_section(source_file, target_file, "当前用户数", "SGA大小", "当前用户数部分")
    append_section(source_file, target_file, "ASM磁盘信息", "over!!", "ASM磁盘空间部分")
    append_section(source_file, target_file, "控制文件的信息", "数据库初始化参数", "控制文件部分")
    append_section(source_file, target_file, "日志文件信息", "归档统计", "日志文件信息")
    append_section(source_file, target_file, "临时文件使用情况", "表空间基本信息", "临时文件使用情况")
    # 筛选表空间 > 85%
    append_high_usage_tablespaces(source_file, target_file)
    # --- 替换原来的 append_section，改为筛选 YES 的函数 ---
    append_autoextend_files(source_file, target_file)
    print(f"\n任务全部完成！")
    
if __name__ == "__main__":
    source_file = 'G:\project_zhou\data\Oracle\oral_file\his02_health_check.txt'
    target_file = 'G:\project_zhou\data\Oracle\extracted_file\database_check.txt'
    database_check(source_file,target_file)
    
