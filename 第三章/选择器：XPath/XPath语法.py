from lxml import etree


html = etree.parse('./example_web.html', etree.HTMLParser())
# /: 直接子节点 //: 子孙节点
result = html.xpath('//*')
# result = html.xpath('//ul/li')

# 子节点，父节点
# result = html.xpath('//li/..')
# result = html.xpath('//li/parent::*')
# result = html.xpath('//li/parent::ol')

# 匹配
# result = html.xpath('//li[@class="tto"]')
# result = html.xpath('//h1[contains(@class, "page_title")]')
# result = html.xpath('//h1[name()="h1"]')

# 获取信息
# result = html.xpath('//li/..')[0].tag  # 不能name()
# result = html.xpath('//li[@class="tto"]/text()')
# result = html.xpath('//h1[contains(@class, "et_title")]/@class')
# result = html.xpath('//h1[contains(@class, "et_title")]/a/@href')

# 运算符: or and mod     |    +  - *  div  =   !=    <    <=    >    >=
#       或  与  除余 两个节点集 加 减 乘  除  等于 不等于 小于 小于等于 大于 大于等于
# result = html.xpath('//ol/* | //ul/*')
# result = html.xpath('//ul/li[position() < 3]/text()')
# result = html.xpath('//ul/li[position() = 3]/text()')

# 只选取其中某些
# result = html.xpath('//ul/li[1]/text()')  # 从1开始
# result = html.xpath('//ul/li[last()]/text()')
# result = html.xpath('//ul/li[position() < 3]/text()')
# result = html.xpath('//ul/li[last()-1]/text()')

# 节点轴选择方法
#  :: + 元素名 + (条件)
# result = html.xpath('//ul/li[1]/ancestor::*')  # 从老到小
# result = html.xpath('//h1//attribute::href')
# result = html.xpath('//ul/child::*[contains(@class, "tto") or contains(@class, "tes") or contains(@class, "tst")]')
# result = html.xpath('//div[@class = "toppings"]/descendant::*')  # 由上至下
# result = html.xpath('//ol/following::*')  # 当前节点以后的所有节点, 由上至下
# result = html.xpath('//ol/following-sibling::*/@class')


print(result)
