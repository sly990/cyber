
import streamlit as st
import trafilatura
from ddgs import DDGS

# 联网搜索辅助函数
def web_search(query: str, top_k=5):
    urls = []
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=top_k)
            for r in results:
                url = r.get("href")
                if url:
                    urls.append(url)
    except Exception as e:
        print("DuckDuckGo搜索失败:", e)
        return []
    return urls

def fetch_webpage(url: str, max_length=2000):
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            return ""
        text = trafilatura.extract(downloaded)
        if not text:
            return ""
        return text[:max_length]
    except Exception as e:
        print("网页抓取失败:", url, e)
        return ""

def tool_web_search(query: str):
    st.toast("🔍 本地库信息不足，正在尝试联网搜索...", icon="🌐",duration=3600)
    urls = web_search(query)
    if not urls:
        return "[WEB_SEARCH_FAILED]"
    contents = []
    for url in urls[:3]:
        text = fetch_webpage(url)
        if text:
            contents.append(f"来源:{url}\n{text}")
    if not contents:
        return "[WEB_SEARCH_EMPTY]"
    return "\n\n".join(contents)