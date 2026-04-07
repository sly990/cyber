
import os
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_community.chat_models import ChatTongyi
from rerank import Rerank_docs
from langchain.agents import Tool, initialize_agent, AgentType
from local_search import local_hybrid_search
from net_search import tool_web_search
from tool_DataCheck import tool_oracle_inspection



# ======== 提示词统一管理 ========
PROMPTS = {
    "is_cyber_query": [
        SystemMessage(content="请判断以下问题是否属于“网络安全预案生成”或者“与数据巡检相关的指令”，请务必只回答“是”或“否”："),
        HumanMessage(content="{question}")
    ],

    "simple_answer": [
        SystemMessage(content="你是一个理性且友好的网络安全预案生成助手，请简洁、友好、礼貌地回答以下通用问题："),
        HumanMessage(content="{question}")
    ]
}

# 获取通义千问 LLM 客户端
def get_llm():
    api_key = os.getenv("TONGYI_API_KEY")
    if not api_key:
        st.error("通义API密钥未配置！")
        return None
    try:
        return ChatTongyi(
            model_name="qwen-plus",
            dashscope_api_key=api_key,
            temperature=0.7
        )
    except Exception as e:
        st.error(f"通义模型加载失败: {str(e)}")
        return None
    
    
# 辅助函数：格式化消息为通义所需格式
def format_messages(template_messages, **kwargs):
    messages = []
    for msg in template_messages:
        content = msg.content.format(**kwargs)
        if isinstance(msg, SystemMessage):
            messages.append({"role": "system", "content": content})
        else:
            messages.append({"role": "user", "content": content})
    return messages


# 判断问题是否为网络安全预案生成问题 返回True或False
def is_cyber_query(question: str) -> bool:
    llm = get_llm()
    if not llm:
        return True
    try:
        messages = format_messages(PROMPTS["is_cyber_query"], question=question)
        response = llm.invoke(messages)
        if hasattr(response, 'content'):
            result = response.content
        else:
            result = str(response)
        result = result.strip().lower()
        return result.startswith("是") or "是" in result or result.startswith("yes")
    except Exception:
        return True
    
    
    # ======== Agent 核心初始化与工具配置 ========
def init_agent(vector_store, es, chat_history_str):
    llm = get_llm()
    
    #把历史内容里的花括号转义,在拼进 prompt 之前先处理
    chat_history_safe = chat_history_str.replace("{", "{{").replace("}", "}}")
    
    def tool_hybrid_search(query: str):
        st.toast("搜索本地知识库.....", icon="🤖",duration=3600)
        # 1. 混合检索召回较多文档
        docs = local_hybrid_search(query, vector_store, es, k=10)
        if not docs:
            return "本地文档中未找到直接相关的安全规范。"
        
        # 2. 调用 Rerank 机制精选
        try:
            ranked_docs = Rerank_docs(query, docs)
            final_context = "\n\n".join([
                f"【参考片段】: {d.page_content}" 
                for d in ranked_docs[:5]
            ])
            return final_context
        except Exception as e:
            print(f"Rerank 出错: {e}")
            return "\n\n".join([d.page_content for d in docs[:3]])

    tools = [
        Tool(
            name="Security_Knowledge_Base",
            func=tool_hybrid_search,
            description="优先使用。查询本地《Web-Sec Documentation》中的专业安全预案、防御规范和实战建议。"
        ),
        Tool(
            name="Web_Search",
            func=tool_web_search,
            description="联网工具。若用户要求“根据最新的网络安全形势”，请调用该工具。"
        ),
        Tool(
            name="Oracle_Inspection_Tool",
            func=tool_oracle_inspection,
            description="触发条件：当用户输入包含 '数据库检查'、'生成巡检报告'、'分析AWR' 或 'Oracle安全评估' 等意图时，必须调用此工具。它会自动处理用户上传的性能数据并生成包含建议的HTML报告。"
        ),
    ]

    expert_prefix = (
        "你是理性且友好的网络安全预案生成助手，同时是一位精通网络安全实战的专家。\n"
        "你的任务是根据参考资料生成专业、可落地的应急响应预案。\n"
        "执行准则：\n"
        "1. **溯源性**：回答必须指明参考来源（如：根据文档内容...）。\n"
        "2. **标准化**：生成的预案应包含：一、组织架构与职责；二、风险评估与预防；三、攻击监测手段；四、应急处置流程；五、事后溯源与加固。\n"
        "3. **一致性**：请结合下方的【对话历史】理解用户意图，避免提供重复建议。\n"
        "若上下文中缺失特定技术点，请基于通用安全最佳实践给出指引并说明“文档未提及，此为通用建议”。\n\n"
        "4. **工具调用**：若用户要求进行数据库巡检，请直接调用 Oracle_Inspection_Tool 工具，并根据工具返回的结果引导用户下载报告。不需要再调用其他工具\n" # 强化工具调用意识
        f"【对话历史】:\n{chat_history_safe}\n"
    )

    return initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={"prefix": expert_prefix},
        max_iterations=10,
        handle_parsing_errors=True,
        return_intermediate_steps=False
    )