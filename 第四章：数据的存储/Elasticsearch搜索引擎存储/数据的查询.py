from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    'https://elastic:E3VUUEUJ5GcLxc2Pp=7s@localhost:9200',
    verify_certs=False,
    ssl_show_warn=False
)

es.options(ignore_status=404).indices.delete(index='news')
es.options(ignore_status=400).indices.create(index='news')

mapping = {
    "properties": {
        "title": {
            "type": "text",
            "analyzer": "ik_max_word",
            "search_analyzer": "ik_smart"
        }
    }
}
result = es.indices.put_mapping(index='news', body=mapping)
print(result)

for data in enumerate(json.load(open("novel_data.json", encoding='UTF-8'))):
    status = es.create(index='news', id=str(data[0]), body=data[1])
    print('数据插入成功', end='')
    print(status)

es.indices.refresh()
print(es.search(index='news'))

dsl = {
    "query": {
        "match_phrase": {
            "title": "高考"
        }
    }
}

result = es.search(index='news', body=dsl)
print(result)
