
import re

def extract_clean_report(input_file, output_file, keywords):
    """
    更智能地抓取 Oracle 日志块，并清理掉原日志中杂乱的分隔符。
    """
    # 匹配时间戳
    timestamp_pattern = re.compile(r'^[A-Z][a-z]{2} [A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}')
    # 匹配原日志中那些讨厌的干扰线
    clutter_pattern = re.compile(r'^(\*+|-+|_+)$')

    current_chunk = []
    event_count = 0

    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            outfile.write("--- Oracle 数据库异常事件分析报告 ---\n")
            outfile.write(f"监控关键字: {', '.join(keywords)}\n")
            outfile.write("="*60 + "\n\n")

            def save_event(chunk):
                nonlocal event_count
                if not chunk:
                    return
                
                # 合并块内容，并过滤掉原日志里的长横线/星号线，保持整洁
                clean_lines = [line.strip() for line in chunk if not clutter_pattern.match(line.strip()) and line.strip()]
                chunk_text = "\n".join(clean_lines)

                # 检查块中是否包含关键字
                if any(kw.upper() in chunk_text.upper() for kw in keywords):
                    event_count += 1
                    outfile.write(f"【事件 {event_count}】\n")
                    outfile.write(chunk_text + "\n")
                    outfile.write("-" * 50 + "\n\n")

            for line in infile:
                # 遇到新的日期行，说明旧的事件结束了
                if timestamp_pattern.match(line):
                    save_event(current_chunk)
                    current_chunk = [line]
                else:
                    current_chunk.append(line)
                    
            outfile.write("over!")
            # 处理最后一个
            save_event(current_chunk)

        print(f"整理完成！共处理 {event_count} 个事件，分隔符已规范化。")

    except Exception as e:
        print(f"处理失败: {e}")


if __name__ == "__main__":
    # --- 参数设定 ---
    input_log = "G:\project_zhou\data\Oracle\oral_file\his02_alert_orcl2_20250120.log"
    output_txt = "G:\project_zhou\data\Oracle\extracted_file\database_error2.txt"
    keywords_to_check = ["ORA", "WARNING", "ERROR", "TERMINAL", "CHECKPOINT"]

    extract_clean_report(input_log, output_txt, keywords_to_check)