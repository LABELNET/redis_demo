from redis_cache.redis_conn import RedisConn


class RedisNotify:
    conn = None
    pubSub = None

    # 连接 redis , 开启订阅
    def connRedis(self):
        self.conn = RedisConn(host='192.168.50.171', port=4000).getRedisCache()
        self.pubSub = self.conn.pubsub()

    # 发送消息
    def pubRedis(self, channel, data):
        self.conn.publish(channel, data)
        print('%s listen and receiver msg : %s' % (self.pubSub.channels, self.pubSub.get_message()))

    # 开启订阅
    def subRedis(self, channel):
        self.pubSub.subscribe(channel)
        # self.pubSub.punsubscribe(channel)
        # self.handlerMsg()

    # 处理消息
    def handlerMsg(self):
        for msg in self.pubSub.listen():
            print('%s listen and receiver msg : %s' % (self.pubSub.channels, msg))
