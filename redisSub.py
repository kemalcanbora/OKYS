import redis
r = redis.Redis(password="123sifre")


class RedisPubSub:
    def __init__(self):
        self.pubsub = r.pubsub()

    def subscribe(self, channels):
        self.pubsub.subscribe(channels)
        self.get_message(self.pubsub)

    def pattern_subscribe(self, pattern="*"):
        self.pubsub.psubscribe(pattern)
        self.get_message(self.pubsub)

    def get_message(self, pubsub):
        while True:
            message = pubsub.get_message()
            if message:
                print(message)


#test

''' ornek - 1'''
RedisPubSub().subscribe(channels="hakanTV")

''' ornek - 2'''
RedisPubSub().subscribe(channels=["hakanTV", "necatiTV"])

''' ornek - 3'''
RedisPubSub().pattern_subscribe(pattern="hak*")
