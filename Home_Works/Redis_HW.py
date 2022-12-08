import redis
from redis_lru import RedisLRU


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i



    print(f"Factorial of ({n}) = {fact}")



f(10)
f(10)

