# Near Realtime:近实时
# cluster：簇,聚集,一个或多个节点的容器
# node：节点
# index:索引,相似特性的文件 容器
# type：在index可定义多个type（逻辑 分类/划分）
# document:能 被索引 信息 的基本单位
# shards & replicas:碎片（细分索引为多个 片块， 1.可以分割/缩放内容量.2.可以跨分片[多个节点]分布和并行化操作）
# 和副本(提供高可用性,扩展搜索量/吞吐量,并行地在所有副本上执行)

# install:java
# java -version
# echo $JAVA_HOME
# https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.4.1/elasticsearch-2.4.1.deb
# dpkg -i elasticsearch-2.4.1.deb
# sudo mkdir -p /usr/share/elasticsearch/config/scripts
# sudo cp /etc/elasticsearch/elasticsearch.yml /usr/share/elasticsearch/config
# sudo cp /etc/elasticsearch/elasticsearch.yml /usr/share/elasticsearch/config
# sudo cp /etc/elasticsearch/logging.yml /usr/share/elasticsearch/config
# sudo chmod o+rwx /usr/share/elasticsearch/config/elasticsearch.yml /usr/share/elasticsearch/config/logging.yml
# sudo chmod g+rwx /usr/share/elasticsearch/config/elasticsearch.yml /usr/share/elasticsearch/config/logging.yml
# sudo mkdir /usr/share/elasticsearch/logs
# sudo mkdir /usr/share/elasticsearch/data
# sudo chmod -R 777 /usr/share/elasticsearch/

# 手动执行 elasticsearch
# /usr/share/elasticsearch/bin/elasticsearch
# /usr/share/elasticsearch/bin/elasticsearch --cluster.name my_cluster_name --node.name my_node_name

# Exploring Your Cluster
# the rest api:
# 1.Check your cluster, node, and index health, status, and statistics
# Check cluster:curl 'localhost:9200/_cat/health?v'

# 2.Administer your cluster, node, and index data and metadata
# get a list of nodes in our cluster as follows:curl 'localhost:9200/_cat/nodes?v'
# list all indices: curl 'localhost:9200/_cat/indices?v'

# 3.Perform CRUD (Create, Read, Update, and Delete) and search operations against your indexes
# create an index named "customer" and then list all the indexes again:curl -XPUT 'localhost:9200/customer?pretty'
#                               curl 'localhost:9200/_cat/indices?v'
# index a simple customer document into the customer index, "external" type, with an ID of 1:
#               curl -XPUT 'localhost:9200/customer/external/1?pretty' -d '
#                             {
#                               "name": "John Doe"
#                             }'
# retrieve that document that we just indexed:curl -XGET 'localhost:9200/customer/external/1?pretty'
# delete the index: curl -XDELETE 'localhost:9200/customer?pretty'
#                   curl 'localhost:9200/_cat/indices?v'
# curl -X<REST Verb> <Node>:<Port>/<Index>/<Type>/<ID>
# modifying data:
#   indexing/replacing documents( curl -XPUT/XPOST 'localhost:9200/customer/external/1?pretty' -d  'json' )
#   updating documents: curl -XPOST 'localhost:9200/customer/external/1/_update?pretty' -d '
#                             {
#                               "doc": { "name": "Jane Doe" }
#                             }'
# deleting document:curl -XDELETE 'localhost:9200/customer/external/2?pretty'


# 4.Execute advanced search operations such as paging, sorting, filtering, scripting, aggregations, and many others


# the search API: GET /bank/_search?q=*&sort=account_number:asc
# took – time in milliseconds for Elasticsearch to execute the search
# timed_out – tells us if the search timed out or not
# _shards – tells us how many shards were searched, as well as a count of the successful/failed searched shards
# hits – search results
# hits.total – total number of documents matching our search criteria
# hits.hits – actual array of search results (defaults to first 10 documents)
# sort - sort key for results (missing if sorting by score)
# _score and max_score - ignore these fields for now


# excute searchs:
# {
#     "query": {
#         { "match_all": {} },
#         "bool": {
#           "should": [
#             { "match": { "address": "mill" } },
#             { "match": { "address": "lane" } }
#           ]
#             过滤
#           "filter": {}
#         }
#     }
#     "size": 0,
#       "aggs": {
#         聚合
#         "group_by_state": {
#           "terms": {
#             "field": "state.keyword"
#           }
#         }
#       }
#   "_source": ["account_number", "balance"]
# }
