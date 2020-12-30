import redis
import json


class RedisPub:
    def __init__(self):
        self.r = redis.Redis(password="123sifre")

    def set_publish(self, channel, message):
        self.r.publish(channel=channel,
                       message=message)


RedisPub().set_publish(channel="deneme", message=json.dumps({"deneme": 13,
                                                             "bisiler": 33,
                                                             "vuhuuu": [{"name": "du dudu du"}]}))
