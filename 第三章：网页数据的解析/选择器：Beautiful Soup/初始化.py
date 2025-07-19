import bs4.formatter
from bs4 import BeautifulSoup


# Beautiful Soup 将复杂的 HTML 文档转换成一个复杂的由 Python 对象构成的树形结构，
# 但处理对象的过程只包含 4 种类型的对象: Tag,
# NavigableString, BeautifulSoup, 和 Comment。


"""
BeautifulSoup提供最大的兼容性， 有时把节点中间的空格和换行也看作节点(如果有)，
这只是一个大概的说法，实际上是一个NavigableString类型的节点。
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""


with open("../example_web.html") as f:
    soup = BeautifulSoup(f, "lxml")
print(soup.prettify(formatter=bs4.formatter.HTMLFormatter(indent=4)))
print(soup.ul.get_text("|", strip=True))  # str
# 若想强制将所有属性当做多值进行解析，可以在 BeautifulSoup 构造方法中设置 multi_valued_attributes=None 参数
# 如果以 XML 方式解析文档，则没有多值属性,但是，可以通过配置 multi_valued_attributes 参数来修改
# class_is_multi = {'*': 'class'}
# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
# 可能实际当中并不需要修改默认配置，默认采用的是HTML标准
