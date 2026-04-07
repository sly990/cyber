import html2text

def html_to_markdown_file(html_path, md_path):
    # 1. 创建转换器对象
    converter = html2text.HTML2Text()
    
    # 2. 关键配置（针对 AWR 等含有大量表格的文档）
    converter.bypass_tables = False      # 保留表格结构 (False 表示不跳过表格)
    converter.ignore_links = False       # 是否忽略链接
    converter.ignore_images = True       # 是否忽略图片
    converter.body_width = 0             # 设为 0 表示不对文本进行自动换行，保持长行
    converter.unicode_snob = True        # 尽可能使用 Unicode 字符

    try:
        # 3. 读取 HTML 内容
        # 使用 errors='ignore' 避免 AWR 报告中可能存在的特殊字符导致解码失败
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        
        # 4. 执行转换
        markdown_text = converter.handle(html_content)
        
        # 5. 写入 Markdown 文件
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
            
        print(f"转换成功！文件已保存至: {md_path}")
        
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    # --- 使用示例 ---
    input_html = 'his02_awrrpt_2_73343_73349.html'
    output_md = 'report_summary.md'

    html_to_markdown_file(input_html, output_md)