from parsel import Selector

"""https://parsel.readthedocs.io"""


selector = Selector(text=open("../example_web.html").read())
lis = selector.css("ul li")
print(lis, type(lis))
print(lis.get())
print(type(lis.get()))
print(type(lis[0]))
