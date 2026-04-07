import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from typing import List
from langchain.schema import Document



def extract_text_from_pdf(pdf_path, remove_header_footer=True):
    """
    提取原生PDF文本，处理页眉页脚、双栏排版
    
    Args:
        pdf_path (str): PDF文件的路径
        remove_header_footer (bool): 是否移除页眉页脚，默认True
    
    Returns:
        str: 处理后的完整文本内容
    """
    doc = fitz.open(pdf_path)
    full_text = []
    
    for page_num, page in enumerate(doc):
        # 【重点】处理双栏排版：按块提取文本，自动排序
        # 返回文本块列表，每个块包含坐标和文本 (x0, y0, x1, y1, text, block_no, block_type)
        blocks = page.get_text("blocks")
        
        # 按坐标排序：先从上到下（y坐标），再从左到右（x坐标），解决双栏顺序问题
        blocks.sort(key=lambda b: (b[1], b[0]))
        
        # 提取并清洗文本块内容
        page_text = "\n".join([block[4].strip() for block in blocks if block[4].strip()])
        
        # 【重点】去除页眉页脚：对比当前页和上一页的文本，去除重复的行（简单实现，可优化）
        if remove_header_footer and page_num > 0:
            prev_page_text = full_text[page_num - 1]
            page_lines = page_text.split("\n")
            filtered_lines = [line for line in page_lines if line not in prev_page_text]
            page_text = "\n".join(filtered_lines)
        
        full_text.append(page_text)
    
    # 拼接所有页文本，用两个换行符分隔页面
    return "\n\n".join(full_text)


def split_native_pdf(pdf_path):
    """
    原生PDF文本切分主函数：先提取文本，再按语义切分
    
    Args:
        pdf_path (str): PDF文件的路径
    
    Returns:
        list: 切分后的文本块列表
    """
    # 1. 提取并预处理PDF文本
    raw_text = extract_text_from_pdf(pdf_path)
    
    # 2. 递归字符切分器：优先按段落/标点切分，保留语义完整性
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "。", "！", "？", " ", ""],
        chunk_size=10000,          # 每个文本块的最大长度
        chunk_overlap=100,       # 文本块之间的重叠长度
        length_function=len,     # 长度计算函数
    )
    
    return  text_splitter.create_documents([raw_text])

# 进行文档切分的代码
def load_documents(pdf_path: str) -> List[Document]:

    if not os.path.exists(pdf_path):
        print(f"错误: PDF文件不存在: {pdf_path}")
        return []
    
    print(f"正在处理PDF文件: {pdf_path}")
    print(f"文件大小: {os.path.getsize(pdf_path) / 1024 / 1024:.2f} MB")
    
    try:
        docs = split_native_pdf(pdf_path)
        print(f"处理完成!")
        print(f"PDF文件名: {os.path.basename(pdf_path)}")
        print(f"生成的文档块数: {len(docs)}")
        return docs
    except Exception as e:
        print(f"处理失败: {pdf_path}")
        print(f"错误信息: {str(e)}")
        return []

# ---------------------- 实战演示 ----------------------
if __name__ == "__main__":
    # 替换为你的原生PDF文件路径
    pdf_path = "/root/autodl-tmp/jinxiangshao_projects1/rag_science_speech/data_pdf/merged_pdfs/websec-readthedocs-io-zh-latest.pdf"
    
    # 执行文本切分
    chunks = split_native_pdf(pdf_path)
    
    # 输出结果
    print("\n前几个块示例：")
    print(chunks[0])
    print(chunks[1])
    print(chunks[2])
    print(chunks[3])
    print(chunks[4])
    print(f"切分后块数：{len(chunks)}")