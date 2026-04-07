# 将检索功能和巡检工具放到智能体
import os
import streamlit as st
import torch
import traceback
from local_search import build_vector_store_and_index
from agent import get_llm,format_messages,is_cyber_query,init_agent,PROMPTS

#用于解决streamlit的某个冲突问题
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 


# 配置路径和环境变量（使用相对路径）
DATA_DIR = os.path.join("data_pdf", "merged_pdfs")

os.environ['HF_ENDPOINT'] = "https://hf-mirror.com"


# 设置成自己的密钥
os.environ["TONGYI_API_KEY"] = "sk-506a5c243ac3445caea6be389b0025fb"  


# ======== Streamlit 主程序 ========
def main():
    
    
    st.set_page_config(page_title="网络与数据安全巡检预案生成助手", layout="wide")
    st.title("🌟 网络与数据安全预案生成助手")
    
    
    # ======== 新增：侧边栏文件上传 ========
    with st.sidebar:
        st.header("📤 数据库巡检文件上传")
        st.markdown("请上传 `nmon`, `txt`, `log`, `html` 等源文件至 `oral_file` 目录。")
        uploaded_files = st.file_uploader(
            "选择文件", 
            accept_multiple_files=True,
            type=['nmon', 'txt', 'log', 'html']
        )
        
        if uploaded_files:
            # 确保目录存在
            upload_dir = r"G:\BiShe\cyber\Oracle\oral_file"
            os.makedirs(upload_dir, exist_ok=True)
            
            for uploaded_file in uploaded_files:
                file_path = os.path.join(upload_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            st.success(f"成功上传 {len(uploaded_files)} 个文件！可以对我说：'开始数据库巡检'")
    # ====================================
    
    
    
    # 1. 初始化数据库和索引
    vector_store, es = build_vector_store_and_index()
    if vector_store is None:
        st.error("向量数据库初始化失败，系统可能无法正常生成网络安全预案。")
    if es is None:
        st.warning("ES 索引未连接，系统将仅使用向量检索。")

    # 2. 初始化对话历史
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "system", "content": "你是理性且友好的网络安全预案生成助手"}
        ]

    # 3. 渲染历史消息
    for msg in st.session_state.chat_history:
        if msg["role"] == "system":
            continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 4. 获取用户输入
    user_input = st.chat_input("请输入您的问题（如：生成一份完整的企业 Web 应用网络安全防护与应急处置预案）")
  
    if user_input:
        
        #清理下载按钮
        st.session_state['latest_report'] = None
        
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("助手正在分析资料并构建网络与数据安全巡检预案..."):
            try:
                # 判断是否为安全意图
                is_cyber = is_cyber_query(user_input)
                
                # 提取最近 5 轮对话作为 Agent/LLM 的上下文记忆
                history_summary = "\n".join([
                    f"{m['role']}: {m['content']}" 
                    for m in st.session_state.chat_history[-6:]
                    if m['role'] != 'system'
                ])

                if is_cyber:
                    st.toast("🛡️ 启动 Agent 进行网络与数据安全巡检报告生成与预案规范...", icon="🤖",duration=3600)
                    agent = init_agent(vector_store, es, history_summary)
                    response = agent.invoke({"input": user_input})
                    answer = response["output"]
                else:
                    st.toast("🍃 识别为通用对话", icon="💬",duration=3600)
                    llm = get_llm()
                    messages = format_messages(PROMPTS["simple_answer"], question=user_input)
                    messages.insert(0, {"role": "system", "content": f"历史背景：\n{history_summary}"})
                    res = llm.invoke(messages)
                    answer = res.content if hasattr(res, 'content') else str(res)

                # 存储并显示助手回复
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                with st.chat_message("assistant"):
                    st.markdown(answer)
                    
                    # ======== 新增：如果状态中存在报告，则渲染下载按钮 ========
                    if 'latest_report' in st.session_state and st.session_state['latest_report']:
                        report_path = st.session_state['latest_report']
                        if os.path.exists(report_path):
                            with open(report_path, "r", encoding="utf-8") as f:
                                report_data = f.read()
                            st.download_button(
                                label="📥 下载 Oracle 安全评估与巡检报告 (HTML)",
                                data=report_data,
                                file_name=os.path.basename(report_path),
                                mime="text/html",
                                key=f"download_{len(st.session_state.chat_history)}" # 防止重复键值
                            )
                            
                    # =========================================================

            except Exception as e:
                error_msg = f"抱歉，处理时出现了点问题：{str(e)}"
                st.error(error_msg)
                print(traceback.format_exc())
                st.session_state.chat_history.append({"role": "assistant", "content": error_msg})

if __name__ == "__main__":
    main()