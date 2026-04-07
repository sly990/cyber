import os
import streamlit as st
import torch
import pickle
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import numpy as np
from chunk_cyber import load_documents


VECTOR_STORE_PATH = os.path.join("vector_store", "vector_store.pkl")
ES_INDEX_NAME = "rag_docs"

# 进行文档切分时使用这个路径
pdf_path = r"G:\BiShe\cyber\data_pdf\merged_pdfs\websec-readthedocs-io-zh-latest.pdf" 


# 简单向量存储替代类
class InMemorySimpleVectorStore:
    def __init__(self, embedding_function, texts, metadatas=None):
        self.embedding_function = embedding_function
        self.texts = texts
        self.metadatas = metadatas or [{} for _ in texts]
        self.doc_embeddings = []
        for text in texts:
            try:
                embedding = embedding_function.embed_query(text)
                self.doc_embeddings.append(embedding)
            except Exception:
                self.doc_embeddings.append(np.zeros(768, dtype=np.float32))

    def similarity_search(self, query, k=4):
        query_embedding = self.embedding_function.embed_query(query)
        query_vec = np.array(query_embedding, dtype=np.float32)
        similarities = []
        for doc_embedding in self.doc_embeddings:
            doc_vec = np.array(doc_embedding, dtype=np.float32)
            dot_product = np.dot(query_vec, doc_vec)
            query_norm = np.linalg.norm(query_vec)
            doc_norm = np.linalg.norm(doc_vec)
            similarity = dot_product / (query_norm * doc_norm) if query_norm > 0 and doc_norm > 0 else 0
            similarities.append(similarity)
        top_indices = np.argsort(similarities)[-k:][::-1]
        return [Document(page_content=self.texts[i], metadata=self.metadatas[i]) for i in top_indices]

# 获取向量模型
@st.cache_resource
def get_embeddings():
    try:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model_kwargs = {'device': device}
        embedder = HuggingFaceEmbeddings(
            model_name=r"G:\BiShe\cyber\models\xiaobu-embedding-v2",
            model_kwargs=model_kwargs,
            encode_kwargs={'normalize_embeddings': True}
        )
        _ = embedder.embed_query("测试")
        return embedder
    except Exception:
        return None
    
    

# 加载向量数据库的函数
def load_or_create_vector_store():
    if os.path.exists(VECTOR_STORE_PATH):
        try:
            with open(VECTOR_STORE_PATH, "rb") as f:
                vector_store = pickle.load(f)
            return vector_store
        except Exception:
            return None
    return None


# 构建向量数据库和索引
@st.cache_resource
def build_vector_store_and_index():
    vector_store = load_or_create_vector_store()
    if vector_store:
        try:
            es = Elasticsearch("http://localhost:9200")
            es.info()
            return vector_store, es
        except Exception:
            return vector_store, None

    docs = load_documents(pdf_path)
    embedder = get_embeddings()
    if not embedder:
        return None, None

    docs = [doc for doc in docs if doc.page_content and doc.page_content.strip()]
    if not docs:
        return None, None

    try:
        try:
            vector_store = FAISS.from_documents(docs, embedder)
        except Exception:
            texts = [doc.page_content for doc in docs]
            metadatas = [doc.metadata for doc in docs]
            vector_store = InMemorySimpleVectorStore(embedder, texts, metadatas)

        os.makedirs(os.path.dirname(VECTOR_STORE_PATH), exist_ok=True)
        with open(VECTOR_STORE_PATH, "wb") as f:
            pickle.dump(vector_store, f)

        try:
            es = Elasticsearch("http://localhost:9200")
            es.info()
            if not es.indices.exists(index=ES_INDEX_NAME):
                actions = [{
                    "_index": ES_INDEX_NAME,
                    "_id": i,
                    "_source": {
                        "content": doc.page_content,
                        "source": doc.metadata.get("source", "unknown")
                    }
                } for i, doc in enumerate(docs)]
                bulk(es, actions)
            return vector_store, es
        except Exception:
            return vector_store, None

    except Exception:
        return None, None

# 关键字匹配        
def keyword_search(es, query, top_k=5):
    if not es:
        return []
    try:
        res = es.search(
            index=ES_INDEX_NAME,
            query={"match": {"content": query}},
            size=top_k
        )
        return [Document(page_content=hit["_source"]["content"], metadata={"source": hit["_source"]["source"]}) 
                for hit in res["hits"]["hits"]]
    except Exception:
        return []
    
    
# 封装一个纯本地的混合搜索函数
def local_hybrid_search(query, vector_store, es, k=5):
    local_docs = []
    if vector_store:
        try:
            local_docs.extend(vector_store.similarity_search(query, k=k))
        except Exception: pass
    if es:
        try:
            local_docs.extend(keyword_search(es, query, top_k=k))
        except Exception: pass
    return local_docs
