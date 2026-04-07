from pathlib import Path



def md_extract(input_file,output_file):
    text = Path(input_file).read_text(encoding="utf-8")
    lines = text.splitlines()

    # ==============================
    # 1 提取系统工作峰值时间段
    # ==============================

    def extract_snap_table(lines):

        table = []
        capture = False

        for line in lines:

            if "Snap Id" in line and "Snap Time" in line:
                capture = True

            if capture:
                if line.strip() == "":
                    break
                table.append(line)

        return "\n".join(table)


    # ==============================
    # 2 提取实例效率命中率
    # ==============================

    def extract_instance_efficiency(lines):

        table = []
        capture = False

        for line in lines:

            if "Instance Efficiency Percentages" in line:
                capture = True
                continue

            if capture:

                if line.strip() == "":
                    if table:
                        break
                    else:
                        continue

                # 跳过markdown分隔线
                if line.strip().startswith("---"):
                    continue

                if "%:" in line:
                    table.append(line)

        return "\n".join(table)


    # ==============================
    # 3 提取 Time Model Statistics
    # ==============================

    def extract_time_model(lines):

        table = []
        capture = False

        for line in lines:

            if "Statistic Name| Time (s)| % of DB Time" in line:
                capture = True
                table.append(line)   # 保留表头
                continue

            if capture:

                if line.strip() == "":
                    break



                if "|" in line:
                    table.append(line)

        return "\n".join(table)


    # ==============================
    # 4 提取 Top Wait Events
    # ==============================

    def extract_wait_events(lines):

        table = []
        capture = False

        for line in lines:

            if "Event| Waits| Total Wait Time" in line:
                capture = True
                table.append(line)
                continue

            if capture:

                if line.strip() == "":
                    break



                if "|" in line:
                    table.append(line)

        return "\n".join(table)


    # ==============================
    # 执行提取
    # ==============================

    snap_text = extract_snap_table(lines)

    eff_text = extract_instance_efficiency(lines)

    time_model_text = extract_time_model(lines)

    wait_event_text = extract_wait_events(lines)


    # ==============================
    # 写入文件
    # ==============================

    with open(output_file, "w", encoding="utf-8") as f:

        f.write("系统工作峰值时间段\n\n")
        f.write(snap_text)
        f.write("\n\n")

        f.write("数据库实例性能的各项命中率\n\n")
        f.write(eff_text)
        f.write("\n\n")

        f.write("数据库实例资源消耗时间模型\n\n")
        f.write(time_model_text)
        f.write("\n\n")

        f.write("数据库前台等待事件Top10\n\n")
        f.write(wait_event_text)
        f.write("\n")
        f.write("\n")
        f.write("over!")


    print("AWR关键指标提取完成，结果已保存为 awr.txt")
    
    
    
if __name__ == "__main__":  
    input_file = r"G:\project_zhou\data\Oracle\extracted_file\report_summary.md"
    output_file = "awr.txt"
    md_extract(input_file,output_file)