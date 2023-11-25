from elasticsearch import Elasticsearch

# 创建 Elasticsearch 客户端
client = Elasticsearch(hosts=['127.0.0.1'])

# 指定索引和查询条件
index = 'your_index_name'
query = {
  "query": {
    "match_all": {}
  }
}

# 执行搜索操作
response = client.search(index=index, body=query)

# 处理搜索结果
for hit in response['hits']['hits']:
  print(hit['_source'])

# 关闭 Elasticsearch 客户端连接
client.close()
