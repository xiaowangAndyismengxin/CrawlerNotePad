import re


s = """ex sentence Hello world 1234 8888
hi hi hi Demo"""
print(len(s))
res = re.findall(r"((\d)\d)(\d)", s, re.S)
print(type(res), res)
