import bs4
from bs4 import BeautifulSoup
import re


with open("../../example_web.html") as f:
    soup = BeautifulSoup(f, "lxml")


result = soup.find_all("b"), type(soup.find_all("b"))
# result = [repr(str(tag))[:100] + '...' for tag in soup.find_all(['body', 'b'])]
# 用True匹配任何值
# for tag in soup.find_all(True):
#     print(tag.name)
# result = soup.find_all(re.compile('ody'))此处正则是用search()搜索的


# 函数
# 如果没有合适过滤器，那么还可以定义一个函数方法，参数是一个元素 [4],
# 如果这个方法返回 True 表示当前元素匹配并且被找到，如果不是则反回 False。
def has_class_and_id(tag: bs4.Tag) -> bool:
    return tag.has_attr("class") and tag.has_attr("id")


# result = soup.find_all(has_class_and_id)


def href_include_bing(href: str | None) -> bool:
    return bool(href and re.compile("bing").search(href))


# result = soup.find_all(href=href_include_bing)
#
# 如果动态参数中出现未能识别的参数名，
# 搜索时会把该参数当作 tag 属性来搜索，
# 比如搜索参数中包含一个名字为 id 的参数，
# Beautiful Soup 会搜索每个 tag 上的 id 属性
# result = soup.find_all(href=re.compile('bing'))
# result = soup.find_all(id=True)
# result = soup.find_all(attrs={'href': href_include_bing})
# result = soup.find_all(class_='tes')

# 还有
# result = soup.find('a')
# result = soup.ul.find_parents()  # 从小到老
# result = soup.a.find_parent()
# result = soup.ul.li.find_next_siblings()
# result = soup.ul.li.find_next_sibling()
# result = soup.hr.find_previous_siblings()
# result = soup.hr.find_previous_sibling()
# 这 2 个方法通过 .next_elements 属性对当前 tag 的之后的 [5] tag 和字符串进行迭代
# find_all_next() 方法返回所有符合条件的节点，
# find_next() 方法返回第一个符合条件的节点:
# soup.find_all_next()
# soup.find_next()
# 这 2 个方法通过 .previous_elements 属性对当前节点前面 [5] 的 tag 和字符串进行迭代，
# find_all_previous() 方法返回所有符合条件的节点
# find_previous() 方法返回第一个符合条件的节点。
# soup.find_all_previous()
# soup.find_previous()


print("result: ", result)
