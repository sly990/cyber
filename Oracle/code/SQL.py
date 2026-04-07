import re

def top_sql(input_file,output_file):

    # 需要提取的表格标题
    titles = [
        "SQL ordered by Elapsed Time",
        "SQL ordered by CPU Time",
        "SQL ordered by Gets",
        "SQL ordered by Reads",
        "SQL ordered by Executions",
        "SQL ordered by Parse Calls"
    ]


    def extract_table(text, title):
        """
        提取指定标题下的markdown表格
        """
        pattern = rf"### {title}([\s\S]*?)(?:\n### |\Z)"
        match = re.search(pattern, text)

        if not match:
            return ""

        section = match.group(1)

        lines = section.splitlines()

        table_lines = []
        start = False

        for line in lines:

            # 找到表头
            if "|" in line and not start:
                start = True

            if start:
                if "|" in line:
                    table_lines.append(line)
                else:
                    break

        return "\n".join(table_lines)


    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()


    with open(output_file, "w", encoding="utf-8") as f:

        for title in titles:

            table = extract_table(text, title)

            if table:
                f.write(title + "\n")
                f.write("=" * 80 + "\n")
                f.write(table + "\n\n")
            else:
                f.write(title + "\n")
                f.write("=" * 80 + "\n")
                f.write("未找到该表格\n\n")
                
        f.write("\n")
        f.write("over!")


    print("所有SQL表格提取完成，已保存到 sql.txt")
    
    
    
    
    
if __name__ == "__main__": 
    input_file = r"G:\project_zhou\data\Oracle\extracted_file\report_summary.md"
    output_file = r"G:\project_zhou\data\Oracle\extracted_file\sql.txt"
    top_sql(input_file,output_file)