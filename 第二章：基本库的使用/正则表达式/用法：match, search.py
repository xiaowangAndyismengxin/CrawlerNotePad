import re


s = """ex sentence Hello world 1234 88
hi hi hi Demo"""
print(len(s))
# res = re.match(r'\w{5}\s\w{5}\s(\d*)?\s\d\d.*', s, re.S | re.I)
res = re.search(r"\w{5}\s\w{5}\s(\d*)?\s\d\d.*", s, re.S | re.I)
print(type(res), res)
print(type(res.span()), res.span())
print(res.group())
print(res.group(1))
