#!/usr/local/bin/python3

from redis_cache.redis_notify import RedisNotify
import time

notify = RedisNotify()
notify.connRedis()
channel = 'labelnet'
notify.subRedis(channel)

if __name__ == '__main__':
    for num in range(10):
        notify.pubRedis(channel, 'hello %d' % num)
        time.sleep(1)
