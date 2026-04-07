import re

def extract_and_save_with_id(input_file, output_file, keywords):
    """
    扫描日志并将包含关键字的片段保存到指定文件，并添加事件编号。
    """
    # 匹配 Oracle 日志的时间戳行格式
    timestamp_pattern = re.compile(r'^[A-Z][a-z]{2} [A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}')
    
    current_chunk = []
    event_count = 0

    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            outfile.write(f"--- Oracle 数据库异常事件提取报告 ---\n")
            outfile.write(f"监控关键字: {', '.join(keywords)}\n")
            outfile.write("="*60 + "\n\n")

            # 辅助函数：检查并写入匹配的块
            def process_and_write(chunk):
                nonlocal event_count
                if chunk:
                    chunk_text = "".join(chunk)
                    # 检查块中是否包含任意关键字
                    if any(kw.upper() in chunk_text.upper() for kw in keywords):
                        event_count += 1
                        # 在文档中明确标注事件编号
                        outfile.write(f"【事件 {event_count}】\n")
                        outfile.write(chunk_text.strip() + "\n")
                        outfile.write("-" * 40 + "\n\n")

            for line in infile:
                if timestamp_pattern.match(line):
                    process_and_write(current_chunk)
                    current_chunk = [line]
                else:
                    current_chunk.append(line)
            
            # 处理文件末尾最后一个块
            process_and_write(current_chunk)

        print(f"提取完成！")
        print(f"共发现并标注了 {event_count} 个事件。")
        print(f"结果已保存至: {output_file}")

    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_file}'。")
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    # --- 配置参数 ---
    input_log = "his02_alert_orcl2_20250120.log"
    output_txt = "database_error1.txt"
    keywords_to_check = ["ORA", "WARNING", "ERROR", "TERMINAL", "CHECKPOINT"]

    # 执行
    extract_and_save_with_id(input_log, output_txt, keywords_to_check)


