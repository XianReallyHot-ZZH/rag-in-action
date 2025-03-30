# 导入相关的库
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding # 需要pip install llama-index-embeddings-huggingface

# 加载本地嵌入模型，并指定模型缓存路径
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-zh", # 模型路径和名称（首次执行时会从HuggingFace下载）
    cache_folder="D:/Developer/LLM/FuggingFace-cache-model" # 指定模型下载的本地缓存路径
    )

# 加载数据
documents = SimpleDirectoryReader(input_files=["../90-文档-Data/黑悟空/设定.txt"]).load_data()

# 构建索引
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# 创建问答引擎
query_engine = index.as_query_engine()  # 这一步会用到生成模型，默认还是会用到openai的gpt-3.5-turbo，还是要用到openai的api key，如果没有，会报错

# 开始问答
print(query_engine.query("黑神话悟空中有哪些战斗工具?"))