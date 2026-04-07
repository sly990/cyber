from sentence_transformers import SentenceTransformer, util
import torch

model_path = r"G:\BiShe\cyber\models\all-MiniLM-L6-v2"  # 根据你的实际路径修改
model = SentenceTransformer(model_path, device='cuda' if torch.cuda.is_available() else 'cpu')

def Rerank_docs(query, unique_docs):

    if not unique_docs:
        return []

    doc_texts = [doc.page_content for doc in unique_docs]

    query_embedding = model.encode(query, convert_to_tensor=True)
    doc_embeddings = model.encode(doc_texts, convert_to_tensor=True)

    cosine_scores = util.cos_sim(query_embedding, doc_embeddings)[0]

    sorted_docs = [unique_docs[i] for i in cosine_scores.argsort(descending=True)][:5]

    return sorted_docs