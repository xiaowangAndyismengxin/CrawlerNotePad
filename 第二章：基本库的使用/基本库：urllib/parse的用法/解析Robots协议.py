from time import sleep
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen


url = "https://www.baidu.com/robots.txt"
rp = RobotFileParser(url="https://www.example.com")
print(rp.mtime())
rp.set_url(url)
print(rp.mtime())
rp.parse(lines=[])  # 可迭代对象
print(rp.mtime())
sleep(3)
print(rp.mtime())
# 如果用parse导就不用read(), 不建议rp同时存在url和parse。
# rp.read()
print(rp.mtime())
print(rp.can_fetch("Baiduspider", "https://www.baidu.com"))
print(rp.can_fetch("Baiduspider", "https://www.baidu.com/homepage/"))
print(rp.can_fetch("Googlebot", "https://www.baidu.com/homepage/"))
print(rp.mtime())
rp.modified()
print(rp.mtime())
