from redis import StrictRedis  # StrictRedis类实现了绝大部分的Redis命令,

#                             参数也一一对应，而Redis是StrictRedis的子类，
#                             Redis是为了兼容旧版数据库, 对部分方法进行了改写，
#                             例如将lrem方法中的参数位置互换。
#                             官方更推荐使用StrictRedis
from redis import ConnectionPool

redis = StrictRedis()
redis.set("name", "Andy")
print(redis.get("name"))
redis.flushall()
