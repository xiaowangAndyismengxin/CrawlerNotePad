from redis import ConnectionPool, StrictRedis

# redis_connect_pool = ConnectionPool(host='localhost', port='6379', db=0)
redis_connect_pool = ConnectionPool.from_url("redis://localhost:6379/0")
redis = StrictRedis(connection_pool=redis_connect_pool)
redis.set("name", "Andy")
print(redis.get("name"))
redis.flushall()
