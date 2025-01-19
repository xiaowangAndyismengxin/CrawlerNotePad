from urllib.parse import urljoin  # 自动合并


"""
不过多介绍，简单来说就是提供一个基础链接作为该函数的第一个参数。
将新的链接作为第二个参数。 
urljoin会分析基础链接的scheme, netloc和path这三项内容，
如果新链接不存在这三项，给予补充，如果存在，则用新连接里的。  
"""
