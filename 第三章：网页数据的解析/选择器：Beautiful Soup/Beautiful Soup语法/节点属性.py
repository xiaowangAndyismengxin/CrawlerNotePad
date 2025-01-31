from bs4 import BeautifulSoup


with open('../../example_web.html') as f:
    soup = BeautifulSoup(f, 'lxml')
# 子节点和子孙节点
# 直接子节点
result = soup.div.contents, type(soup.div.contents)
# result = soup.div.children
# for child in enumerate(soup.div.children):
#     print(child)

# 子孙节点
# result = soup.div.descendants
# for descendant in enumerate(soup.div.descendants):
#     print(descendant)

# 父节点和祖先节点
# 父节点
# result = soup.a.parent
# 祖先节点
# result = soup.ul.li.parents
# print(list(enumerate(soup.ul.li.parents)))

# 兄弟节点
# result = repr(soup.ul.li.next_sibling)
# result = repr(soup.hr.previous_sibling)

# result = soup.ul.li.next_siblings
# print(list(enumerate(soup.ul.li.next_siblings)))

# result = soup.ul.next_sibling.next_sibling.previous_siblings
# print(list(enumerate(soup.ul.next_sibling.next_sibling.previous_siblings)))


print('result: ', result)
