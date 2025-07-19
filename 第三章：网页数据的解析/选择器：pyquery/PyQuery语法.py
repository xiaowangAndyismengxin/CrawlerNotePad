from pyquery import PyQuery


doc = PyQuery(filename="../example_web.html")


# 查找节点
# 子孙节点
result = doc(".toppings").find("li")
# 子节点
# result = doc('.toppings').children()
# 父节点
# result = doc('.toppings .tes').parent()
# 祖先节点
# result = doc('.toppings .tes').parents('ul')
# result = doc('.toppings .tes').parents('html title')
# 兄弟节点
# result = doc('.tse').siblings('tmo')

# 遍历节点
# result = doc('.tse').siblings().items()
# for li in result:
#     print(li, type(li))

# 属性获取
# result = doc('a').attr('href')
# result = doc('body a:only-child').attr.href
# result = doc('ul li:nth-of-type(2)').text()  # str
# result = repr(doc('ul li').text())  # str

# ---------------------------------------------------------------

# 节点操作
# element_a = doc('a.title_a')
# result = element_a
# element_a.remove_class('first_a')
# element_a.add_class('first_a')

# element_a.attr('name', 'aaaa')
# element_a.remove_attr('name')
# element_a.text('new text')
# element_a.html('<sth>change html directly</sth>')
# element_sth = element_a.find('sth')
# print(element_sth.remove())


print("result: ", result)
