# 第一行代码：导入相关的库
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os

# 调试路径

print("当前工作目录:", os.getcwd())
file_path = "../90-文档-Data/黑悟空/设定.txt"
print("文件是否存在?", os.path.exists(file_path))  # 调试输出

# 第二行代码：加载数据
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
# 第三行代码：构建索引
index = VectorStoreIndex.from_documents(documents)
# 第四行代码：创建问答引擎
query_engine = index.as_query_engine()  # 这里默认使用openai的gpt-3.5-turbo模型，需要用到openai的api key，没有就跳过吧
# 第五行代码: 开始问答
print(query_engine.query("黑神话悟空中有哪些战斗工具?"))

