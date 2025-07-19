from lxml import etree


html = etree.parse(
    "./example_web.html", etree.HTMLParser()
)  # <class 'lxml.etree._Element'>
print(etree.tostring(html).decode("utf-8"))
result = html.xpath("//*")
print(result)  # 大的是list 里面每一个都是<class 'lxml.etree._Element'>
