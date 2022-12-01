import redis

r = redis.Redis(
    host='hostname',
    port=5000,
    password='password'
)

r.set('foo', 'bar')
value = r.get('foo')
print(value)    # bar