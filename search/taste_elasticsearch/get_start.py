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

