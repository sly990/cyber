import os
import re
import html
import pandas as pd
from openai import OpenAI
from bs4 import BeautifulSoup



# ==========================================
# 初始化 DeepSeek 客户端
# ==========================================
api_key = "sk-e6b8462b812c475a82076c124c53d628"  
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# =========================
# CSV 读取函数（统一版）
# =========================
def extract_csv_content(file_path, target_columns=None):
    """
    - target_columns=None：读取全部列
    - target_columns=[...]：读取指定列 + 第一列
    - 每5行取1行
    """
    try:
        df = pd.read_csv(file_path)

        # 每5行取1行
        df = df.iloc[::5].reset_index(drop=True)

        # 全部列
        if target_columns is None:
            return df.to_csv(index=False)

        # 指定列
        time_col = df.columns[0]

        missing = [col for col in target_columns if col not in df.columns]
        if missing:
            raise ValueError(f"缺失列: {missing}")

        cols_to_keep = [time_col] + target_columns
        df_filtered = df[cols_to_keep]

        return df_filtered.to_csv(index=False)

    except Exception as e:
        print(f"CSV处理失败 [{file_path}]: {e}")
        return None


# =========================
# 通用 AI 分析函数（无 max_tokens）
# =========================
def analyze_with_prompt(csv_data, prompt, system_role="你是一个严谨的 Oracle 性能分析专家。"):
    if not csv_data:
        return "数据无效，无法分析。"

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": f"{prompt}\n\n数据如下：\n{csv_data}"}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"分析失败: {e}"


# =========================
# HTML 追加函数
# =========================
def append_to_html(html_path, title, content):
    title_safe = html.escape(title)
    content_safe = html.escape(content).replace("\n", "<br>")

    block = f"""
    <section style="margin-bottom:24px;">
        <h3 style="font-size:18px; margin:0 0 8px 0;">{title_safe}</h3>
        <p style="font-size:14px; line-height:1.7; margin:0;">
            {content_safe}
        </p>
    </section>
    """

    # 文件不存在就创建基础HTML
    if not os.path.exists(html_path):
        with open(html_path, "w", encoding="utf-8") as f:
            f.write("<html><head><meta charset='utf-8'></head><body></body></html>")

    with open(html_path, "r", encoding="utf-8") as f:
        html_text = f.read()

    # 插入到 </body> 前
    match = re.search(r"</body\s*>", html_text, flags=re.IGNORECASE)
    if match:
        idx = match.start()
        new_html = html_text[:idx] + block + "\n" + html_text[idx:]
    else:
        new_html = html_text + block

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)


# =========================
# 单任务分析
# =========================
def analyze_one_and_append_html(task, html_path):
    """
    task:
    {
        "name": "CPU诊断结论",
        "file": "...",
        "columns": [...],  # None=全部列
        "prompt": "...",
        "system_role": "..."
    }
    """

    print(f"正在分析: {task['name']}")

    csv_data = extract_csv_content(
        task["file"],
        task.get("columns", None)
    )

    result = analyze_with_prompt(
        csv_data,
        task["prompt"],
        task.get("system_role", "你是一个严谨的 Oracle 性能分析专家。")
    )

    append_to_html(html_path, task["name"], result)

    print(result)
    return result


# =========================
# 双CSV分析（内存专用）
# =========================
def analyze_two_csv_and_append_html(task, html_path):
    """
    task:
    {
        "name": "...",
        "file1": "...",
        "columns1": [...],
        "file2": "...",
        "columns2": None,
        "prompt": "..."
    }
    """

    print(f"正在分析: {task['name']}")

    csv1 = extract_csv_content(task["file1"], task.get("columns1", None))
    csv2 = extract_csv_content(task["file2"], task.get("columns2", None))

    combined_data = f"""
=== 表1 ===
{csv1}

=== 表2 ===
{csv2}
"""

    result = analyze_with_prompt(
        combined_data,
        task["prompt"],
        task.get("system_role", "你是一个严谨的 Oracle 性能分析专家。")
    )

    append_to_html(html_path, task["name"], result)

    print(result)
    return result


def extract_analyze_and_append_html(source_file, html_path, task):
    """
    单任务分析：提取数据 → AI分析 → 追加写入HTML
    
    task: {
        "name": "CPU分析",
        "start": "CPU SECTION START",
        "end": "CPU SECTION END",
        "prompt": "请分析CPU使用情况..."
    }
    """

    if not os.path.exists(source_file):
        print(f"错误：源文件 {source_file} 不存在")
        return

    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    name = task['name']
    start = task['start']
    end = task['end']
    specific_prompt = task['prompt']

    print(f"正在处理任务: {name}...")

    # --- 提取片段 ---
    pattern = re.escape(start) + r'(.*?)' + re.escape(end)
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print(f"[跳过] 未匹配到标记: {start}")
        ai_result = "未获取到相关数据，无法分析。"
    else:
        data_fragment = match.group(1).strip()

        # --- 调用 AI ---
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个严谨的 Oracle 性能分析专家。"},
                    {"role": "user", "content": f"{specific_prompt}\n\n数据如下：\n{data_fragment}"}
                ],
                temperature=0.2
            )
            ai_result = response.choices[0].message.content.strip()
        except Exception as e:
            ai_result = f"AI 分析失败: {e}"

    # --- 写入 HTML ---
    with open(html_path, "a", encoding="utf-8") as f:

        # AI结论（支持换行）
        formatted_result = ai_result.replace("\n", "<br>")
        f.write(f'<p style="font-size:16px; line-height:1.6;">{formatted_result}</p>\n')

    print(f"任务 {name} 已写入 HTML")
    
    
    
    
def extract_visible_text_from_html(html_content):
    """
    提取 HTML 渲染后可见的正文文本
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # 去掉不需要分析的标签
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    # 提取可见文本，保留段落换行
    text = soup.get_text(separator="\n", strip=True)

    # 清理多余空行
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def analyze_visible_text_and_append_html(source_file, html_path, task):
    """
    读取 HTML 渲染出来的正文文本 → AI 分析 → 追加写入原 HTML 文档末尾

    task: {
        "name": "整体内容分析",
        "prompt": "请对以下正文内容进行分析，给出简要结论。"
    }
    """

    if not os.path.exists(source_file):
        print(f"错误：源文件 {source_file} 不存在")
        return

    if not os.path.exists(html_path):
        print(f"错误：HTML文件 {html_path} 不存在")
        return

    # 读取 HTML
    with open(source_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 提取可见正文文本
    visible_text = extract_visible_text_from_html(html_content)

    name = task["name"]
    specific_prompt = task["prompt"]

    print(f"正在处理任务: {name}...")

    # --- 调用 AI ---
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个严谨的分析专家。"},
                {"role": "user", "content": f"{specific_prompt}\n\n以下是HTML渲染后的正文文本：\n{visible_text}"}
            ],
            temperature=0.2
        )
        ai_result = response.choices[0].message.content.strip()
    except Exception as e:
        ai_result = f"AI 分析失败: {e}"

    # --- 读取原 HTML 并追加结果 ---
    with open(html_path, "r", encoding="utf-8") as f:
        original_html = f.read()

    formatted_result = html.escape(ai_result).replace("\n", "<br>")

    insert_html = f"""
<div style="margin-top:20px; padding:15px; border:1px solid #ddd; border-radius:8px;">
    <p style="font-size:18px; font-weight:bold; margin:0 0 10px 0;">{html.escape(name)}</p>
    <p style="font-size:16px; line-height:1.6; margin:0;">{formatted_result}</p>
</div>
"""

    # 优先插入到 </body> 前
    lower_html = original_html.lower()
    if "</body>" in lower_html:
        idx = lower_html.rfind("</body>")
        new_html = original_html[:idx] + insert_html + original_html[idx:]
    else:
        new_html = original_html + insert_html

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"任务 {name} 已写入 HTML")
    
    

