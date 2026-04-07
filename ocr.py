import fitz
from rapidocr_onnxruntime import RapidOCR


#OCR处理pdf扫描件
def ocr_pdf(pdf_path):
    
    engine = RapidOCR()
    doc = fitz.open(pdf_path)
    full_text = []
    
    for page_index in range(len(doc)):
        page = doc[page_index]

        pix = page.get_pixmap(dpi=300)
        img_bytes = pix.tobytes()

        result, _ = engine(img_bytes)

        if result:
            page_text = "\n".join([line[1] for line in result])
            full_text.append(f"--- Page {page_index + 1} ---\n{page_text}")

    return "\n\n".join(full_text)


if __name__ == "__main__":
    text = ocr_pdf(r"G:\BiShe\cyber\data_pdf\Informationsecuritytechnology.pdf")
    print(text)

