from bs4 import BeautifulSoup


with open('../example_web.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# 获取信息
# result = soup.title.name, type(soup.title.name)
# result = soup.a.attrs, soup.a.attrs['class'], soup.a['class'], type(soup.a.attrs)
# result = soup.ul.li.string, type(soup.ol.li.string)

# 子节点和子孙节点
# 直接子节点
# result = soup.div.contents, type(soup.div.contents)
# result = soup.div.children, type(soup.div.children)
# for child in enumerate(soup.div.children):
#     print(child)

# 子孙节点
# result = soup.div.descendants, type(soup.div.descendants)
# for descendant in enumerate(soup.div.descendants):
#     print(descendant)

# 父节点和祖先节点
# 父节点
# result = soup.a.parent, type(soup.a.parent)
# 祖先节点
# result = soup.ul.li.parents, type(soup.ul.li.parents)
# print(list(enumerate(soup.ul.li.parents)))




print('result: ', result)
