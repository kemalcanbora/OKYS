import redis


class RedisPub:
    def __init__(self):
        self.r = redis.Redis(password="123sifre")

    def set_publish(self, channel, message):
        self.r.publish(channel=channel,
                       message=message)
