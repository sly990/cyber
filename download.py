
# import os
# import torch
# from modelscope import snapshot_download, AutoModel, AutoTokenizer
# model_dir = snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='/root/autodl-tmp', revision='master')


from huggingface_hub import snapshot_download

# 模型ID
model_id = "sentence-transformers/all-MiniLM-L6-v2"
# 指定你想保存模型的本地路径
local_model_path = r"G:\BiShe\cyber\models\all-MiniLM-L6-v2"

# 下载整个模型仓库
snapshot_download(repo_id=model_id, local_dir=local_model_path)

print(f"模型已下载到: {local_model_path}")


# from huggingface_hub import snapshot_download

# # 替换成你想存放模型的路径，比如 D:\models
# local_model_path = snapshot_download(
#     repo_id="lier007/xiaobu-embedding-v2",
#     local_dir=r"G:\BiShe\cyber\models\xiaobu-embedding-v2", # 指定你想放的文件夹
#     local_dir_use_symlinks=False # 推荐设置为False，直接下载文件而不是创建符号链接
# )
# print(f"模型已下载到: {local_model_path}")




