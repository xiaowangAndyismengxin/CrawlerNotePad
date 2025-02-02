from parsel import Selector


selector = Selector(text=open('../example_web.html').read())


result = selector.xpath('//ul/li/text()').get()
# result = selector.xpath('//ul/li/text()').getall()  # list
# result = selector.css('ul li ::text').getall()
# result = selector.css('h1 a::attr(href)').get()
# result = selector.xpath('//ul').re('>([^<]*)</(.*?)>')  # list[str]
# result = selector.xpath('//ul').re_first('>([^<]*)</(.*?)>')


print('result: ', result)
