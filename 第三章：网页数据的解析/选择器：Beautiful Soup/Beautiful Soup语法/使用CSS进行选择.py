from bs4 import BeautifulSoup


with open('../../example_web.html') as f:
    soup = BeautifulSoup(f, 'lxml')


result = soup.select('.title_a.first_a')
# result = soup.select('a')
# result = soup.select_one('a')

# Soup Sieve 提供的是比 select() 和 select_one() 更底层的方法，
# 通过 Tag 或 Beautiful Soup 对象的 .css 属性，可以调用大部分的 API。
# 下面是支持这种调用方式的方法列表，
# 查看 Soup Sieve 文档了解全部细节。
# iselect() 方法与 select() 效果相同，区别是返回的结果是迭代器。
# result = soup.css.iselect('a')
# closest() 方法与 find_parent() 方法相似，返回符合 CSS 选择器的 Tag 对象的最近父级。
# result = soup.a.css.closest('h1')
# match() 方法返回布尔结果，标记指定 Tag 是否符合指定筛选器
# result = soup.a.css.match('.title_a')
# result = soup.a.css.match('.second_a')
# filter() 方法返回 tag 直接子节点中符合筛选器的节点列表
# result = soup.ul.css.filter('li')
# escape() 方法可以对 CSS 标识符中的特殊字符进行转义，否则是非法 CSS 标识符
# result = soup.css.escape('.')


print('result: ', result)
