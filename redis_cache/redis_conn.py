#!/usr/local/bin/python3

import redis


class RedisConn:
    __pool = None

    # 构造函数
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    # redis pool
    def __redisPool(self):
        return redis.ConnectionPool(host=self.__host, port=self.__port)

    # redis conn
    def getRedisCache(self):
        self.__pool = self.__redisPool()
        print('Redis already connection success and pid : %d' % self.__pool.pid)
        return redis.Redis(connection_pool=self.__pool)

    # redis disconn
    def __del__(self):
        print("Redis Pid %d disconnect" % self.__pool.pid)
        self.__pool.disconnect()
