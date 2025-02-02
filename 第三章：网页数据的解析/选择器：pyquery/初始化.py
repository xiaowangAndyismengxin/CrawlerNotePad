from pyquery import PyQuery
"""https://pyquery.readthedocs.io/"""


# 传文本
# doc = PyQuery(open('../example_web.html').read())

# 传url
# doc = PyQuery(url='https://ssr1.scrape.center')
# 默认情况下，它使用 python 的 urllib。
# 如果安装了 requests，则它将使用它。这允许您使用大多数 requests 参数：

# 传文件
doc = PyQuery(filename='../example_web.html')
print(doc, type(doc))
print(doc('li'), type(doc('li')))
