file_name = "index.html"

with open(file_name, "a", encoding="utf-8") as f:
    # 插入一段文字
    f.write("\n<p>这是 Python 插入的一段文字</p>")