from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    "https://elastic:E3VUUEUJ5GcLxc2Pp%3D7s@localhost:9200",
    verify_certs=False,
    ssl_show_warn=False,
)

es.options(ignore_status=404).indices.delete(index="news")
es.options(ignore_status=400).indices.create(index="news")

for data in enumerate(json.load(open("novel_data.json", encoding="UTF-8"))):
    es.create(index="news", id=str(data[0]), body=data[1])
    print(f"数据插入成功 id: {data[0]}")

data = {
    "title": "985保送路线有哪些？",
}
status = es.update(index="news", id="3", body={"doc": data})
# status = es.index(index='news', id='3', body=data)
print(status)
doc = es.get(index="news", id="3")
print(doc)

status = es.delete(index="news", id="3")
print(status)
es.indices.refresh()
result = es.search(index="news")
print(result)
