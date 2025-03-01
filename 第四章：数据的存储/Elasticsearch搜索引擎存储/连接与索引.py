from elasticsearch import Elasticsearch

es = Elasticsearch(
    'https://elastic:E3VUUEUJ5GcLxc2Pp=7s@localhost:9200',
    verify_certs=False,
    ssl_show_warn=False
)
# print(es.info())  # 打印集群信息，确认连接成功
# status = es.options(ignore_status=400).indices.create(index='news')
# print(status)
status = es.options(ignore_status=(400, 404)).indices.delete(index='news')
print(status)
