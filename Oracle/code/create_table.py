import os
from deepseek import api_key,analyze_one_and_append_html,analyze_two_csv_and_append_html,extract_analyze_and_append_html,\
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



#针对不同数据形式写了几个制作表格的函数


#提取文件内容生成表格
def extract_and_append_as_table_html(html_path, txt_path, start_marker, end_marker, include_markers=False):
    """
    从 txt 中提取 | 分隔表格，并追加为 HTML table 到 html 文件末尾
    """

    def is_separator_line(line: str) -> bool:
        s = line.strip()
        if not s:
            return True
        return bool(re.fullmatch(r"[\s\-\=\|]{3,}", s))

    def parse_pipe_row(line: str):
        parts = [p.strip() for p in line.rstrip("\n\r").split("|")]

        while parts and parts[0] == "":
            parts.pop(0)
        while parts and parts[-1] == "":
            parts.pop()

        return parts

    def normalize_row(row, col_count):
        if len(row) < col_count:
            return row + [""] * (col_count - len(row))
        if len(row) > col_count:
            return row[:col_count - 1] + [" | ".join(row[col_count - 1:])]
        return row

    def build_html_table(rows):

        thead = rows[0]
        tbody = rows[1:]

        html_table = []
        html_table.append('<table border="1" cellspacing="0" cellpadding="6" '
                          'style="border-collapse:collapse;width:100%;margin-top:10px;">')

        # 表头
        html_table.append("<thead><tr>")
        for cell in thead:
            html_table.append(f"<th>{html.escape(str(cell))}</th>")
        html_table.append("</tr></thead>")

        # 表体
        html_table.append("<tbody>")
        for row in tbody:
            html_table.append("<tr>")
            for cell in row:
                html_table.append(f"<td>{html.escape('' if cell is None else str(cell))}</td>")
            html_table.append("</tr>")
        html_table.append("</tbody></table>")

        return "".join(html_table)

    # 读取 txt
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"读取 txt 失败: {e}")
        return False

    # 提取区间
    pattern = re.escape(start_marker) + r"(.*?)" + re.escape(end_marker)
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print("未找到目标区间")
        return False

    fragment = match.group(0) if include_markers else match.group(1)

    # 解析表格
    rows = []
    for raw_line in fragment.splitlines():
        line = raw_line.strip("\n\r")

        if not line.strip():
            continue
        if is_separator_line(line):
            continue
        if "|" not in line:
            continue

        row = parse_pipe_row(line)
        if row:
            rows.append(row)

    if not rows:
        print("没有解析到表格")
        return False

    col_count = len(rows[0])
    rows = [normalize_row(row, col_count) for row in rows]

    table_html = build_html_table(rows)

    # 读取 HTML
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        html_content = "<html><head><meta charset='utf-8'></head><body></body></html>"

    # 插入到 </body> 前
    if "</body>" in html_content.lower():
        html_content = re.sub(r"</body>", table_html + "\n</body>", html_content, flags=re.IGNORECASE, count=1)
    else:
        html_content += table_html

    # 写回
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("表格已追加到 HTML")
    return True

#提取文件内容生成表格
def extract_and_append_as_table_html_database(html_path, txt_path, start_marker, end_marker, include_markers=False):
    """
    从 txt 中提取数据库查询结果，自动处理列偏移，并过滤 total/横线等污染字段。
    """
    
    # 1. 读取文件
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"读取 txt 失败: {e}")
        return False

    # 清洗 AI 注入的标签和干扰
    content = re.sub(r'\\s*\n?', '', content)

    # 2. 提取区间
    pattern = re.escape(start_marker) + r"(.*?)" + re.escape(end_marker)
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print("未找到目标区间")
        return False

    fragment = match.group(0) if include_markers else match.group(1)

    # 3. 增强版污染过滤
    def is_pollution(line: str) -> bool:
        s = line.strip()
        if not s: return True
        # 过滤数字序号如 "2."
        if re.fullmatch(r'\d+\.', s): return True
        # 过滤统计行 (以 total 或 sum 开头，不区分大小写)
        if re.match(r'^(total|sum|avg|max|min|count)\b', s, re.IGNORECASE): return True
        # 过滤纯横线行 (长度超过 3 的横线，且中间没有空格或只有空格)
        if re.fullmatch(r'[- ]{3,}', s) and '-' in s:
            # 如果这行是类似 "--- ---" 的结构，可能是表头标尺，暂时保留给后续逻辑判断
            if ' ' in s.strip(): return False 
            return True
        # 过滤 Oracle 提示信息
        if "rows selected" in s.lower() or s.lower() == "over!": return True
        return False

    raw_lines = fragment.splitlines()
    # 初步清洗：去掉明显不需要的行
    valid_lines = [l for l in raw_lines if not is_pollution(l)]

    if not valid_lines:
        print("没有有效数据")
        return False

    # 4. 解析表格
    rows = []
    col_spans = []
    header_idx = -1

    # 寻找标尺行 (类似 ---------- ----------)
    for i, line in enumerate(valid_lines):
        if re.fullmatch(r'^[-]+(?:\s+[-]+)+$', line.strip()):
            header_idx = i
            matches = list(re.finditer(r'-+', line))
            for j, m in enumerate(matches):
                start = m.start()
                end = matches[j+1].start() if j + 1 < len(matches) else None
                col_spans.append((start, end))
            break

    if col_spans and header_idx > 0:
        # 获取表头
        header_line = valid_lines[header_idx - 1]
        headers = [header_line[start:end].strip() if end else header_line[start:].strip() for start, end in col_spans]
        rows.append(headers)
        num_cols = len(headers)

        # 解析数据行
        for line in valid_lines[header_idx + 1:]:
            if not line.strip(): continue
            
            # 策略 A: 固定宽度截取
            row_fw = [line[start:end].strip() if end else line[start:].strip() for start, end in col_spans]
            
            # 策略 B: 按空格切分
            parts_space = line.strip().split()

            # 逻辑判断：如果固定宽度截取导致最后一列落空，或者第一列包含了明显的空格（如 "24 BAS"）
            # 且空格切分后的数量正好等于列数，则采用空格切分
            if len(parts_space) == num_cols and (not row_fw[-1] or (len(row_fw[0].split()) > 1)):
                rows.append(parts_space)
            else:
                if any(row_fw): rows.append(row_fw)
    else:
        # 后备方案：如果没有标尺，使用多空格切分
        for line in valid_lines:
            parts = re.split(r'\s{2,}', line.strip())
            if len(parts) > 1: rows.append(parts)

    if not rows: return False

    # 5. 生成 HTML (保持一致)
    max_c = max(len(r) for r in rows)
    html_table = ['<table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse;width:100%;margin-top:10px;font-size:14px;">']
    
    for i, row in enumerate(rows):
        tag = "th" if i == 0 else "td"
        bg = " style='background-color:#f2f2f2;'" if i == 0 else ""
        html_table.append(f"<tr{bg}>")
        # 补齐缺失列
        full_row = row + [""] * (max_c - len(row))
        for cell in full_row:
            html_table.append(f"<{tag}>{html.escape(str(cell))}</{tag}>")
        html_table.append("</tr>")
    html_table.append("</table>")

    table_html = "".join(html_table)

    # 6. 写入 HTML
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        html_content = "<html><body></body></html>"

    if "</body>" in html_content.lower():
        html_content = re.sub(r"</body>", table_html + "\n</body>", html_content, flags=re.IGNORECASE, count=1)
    else:
        html_content += table_html

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("已清理污染行并追加表格")
    return True

#提取文件内容生成表格
def extract_multi_tables_append_html(
    html_path,
    txt_path,
    start_marker,
    end_marker,
    include_markers=False
):
    """
    从 txt 中提取指定区间，并解析其中多个数据库表格，
    每个表格生成一个 HTML table 追加到 html 文件。
    """

    # 读取 txt
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 提取区间
    pattern = re.escape(start_marker) + r"(.*?)" + re.escape(end_marker)
    match = re.search(pattern, content, re.S)

    if not match:
        print("未找到目标区间")
        return False

    fragment = match.group(0) if include_markers else match.group(1)

    # 按 rows selected 分割表格
    blocks = re.split(r"\d+\s+rows\s+selected\.", fragment, flags=re.I)

    tables_html = []

    for block in blocks:

        lines = [l.rstrip() for l in block.splitlines() if l.strip()]

        if len(lines) < 3:
            continue

        header_idx = -1
        col_spans = []

        # 查找标尺行
        for i, line in enumerate(lines):
            if re.fullmatch(r'^[-]+(?:\s+[-]+)+$', line.strip()):
                header_idx = i

                matches = list(re.finditer(r'-+', line))

                for j, m in enumerate(matches):
                    start = m.start()
                    end = matches[j+1].start() if j+1 < len(matches) else None
                    col_spans.append((start, end))

                break

        if header_idx <= 0:
            continue

        header_line = lines[header_idx - 1]

        headers = [
            header_line[s:e].strip() if e else header_line[s:].strip()
            for s, e in col_spans
        ]

        rows = [headers]

        # 解析数据行
        for line in lines[header_idx + 1:]:

            if re.match(r'^(total|sum)', line.strip(), re.I):
                continue

            row = [
                line[s:e].strip() if e else line[s:].strip()
                for s, e in col_spans
            ]

            if any(row):
                rows.append(row)

        if len(rows) <= 1:
            continue

        # 生成 HTML
        max_c = max(len(r) for r in rows)

        html_table = [
            '<table border="1" cellspacing="0" cellpadding="6" '
            'style="border-collapse:collapse;width:100%;margin-top:10px;font-size:14px;">'
        ]

        for i, row in enumerate(rows):

            tag = "th" if i == 0 else "td"
            bg = " style='background-color:#f2f2f2;'" if i == 0 else ""

            html_table.append(f"<tr{bg}>")

            row = row + [""] * (max_c - len(row))

            for cell in row:
                html_table.append(f"<{tag}>{html.escape(cell)}</{tag}>")

            html_table.append("</tr>")

        html_table.append("</table>")

        tables_html.append("".join(html_table))

    if not tables_html:
        print("未解析出表格")
        return False

    final_html = "\n".join(tables_html)

    # 写入 HTML
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except:
        html_content = "<html><body></body></html>"

    if "</body>" in html_content.lower():
        html_content = re.sub(
            r"</body>",
            final_html + "\n</body>",
            html_content,
            flags=re.I
        )
    else:
        html_content += final_html

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"成功解析 {len(tables_html)} 个表格")

    return True