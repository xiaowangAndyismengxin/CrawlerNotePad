from bs4 import BeautifulSoup


with open('../../example_web.html') as f:
    soup = BeautifulSoup(f, 'lxml')


result = soup.title.name, type(soup.title.name)
# print(list(enumerate(soup.ul.li.next_siblings))[0][1].name)
# result = soup.a.attrs, soup.a.attrs['class'], soup.a['class'], type(soup.a.attrs)
# result = soup.ul.li.string, type(soup.ol.li.string)

# 如果 tag 中包含多个字符串 ,可以使用 .strings 来循环获取
# result = soup.body.strings
# for string in enumerate(result):
#     print(repr(string))

# # 输出的字符串中可能包含了很多空格或空行，使用 .stripped_strings 可以去除多余空白内容
# result = soup.body.stripped_strings
# for string in enumerate(result):
#     print(repr(string))  # 全部是空格的行会被忽略掉，段首和段末的空白会被删除


# tag 的属性可以被添加、删除或修改。tag的属性操作方法与字典一样
# del soup.a['class']
# result = soup.a
# soup.a['class'] = ["title_a", "first_a"]
# result = soup.a

# tag 中包含的字符串不能直接编辑，但是可以被替换成其它的字符串，用 replace_with() 方法
# soup.h1.a.string.replace_with('new title')
# result = soup.h1.a
# 如果想在 Beautiful Soup 之外使用 NavigableString 对象，需要调用 unicode() 方法，将该对象转换成普通的Unicode字符串，
# 否则就算 Beautiful Soup 方法已经执行结束，该对象的输出 也会带有对象的引用地址。这样会浪费内存。


print('result: ', result)
