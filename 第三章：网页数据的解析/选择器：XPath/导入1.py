from lxml import etree


with open("example_web.html") as f:
    text = f.read()

html = etree.HTML(text)
print(type(html), html)
result = etree.tostring(html)
print(type(result))
print(result.decode("ASCII"))
