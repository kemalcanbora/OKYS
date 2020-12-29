import redis

r = redis.Redis(password="123sifre")

data = {
    "necatiates@gmail.com": {
        "name": "necati ates",
        "request_limit": 10,
        "age": 45
    },
    "hakantasiyan@gmail.com": {
        "name": "hakan tasiyan",
        "request_limit": 10,
        "age": 47
    },
    "aysekeci@gmail.com": {
        "name": "ayse keci",
        "request_limit": 10,
        "age": 65
    }
}


def save(data):
    with r.pipeline() as pipe:
        for item_id, item in data.items():
            pipe.hmset(item_id, item)
        pipe.execute()

    r.bgsave()


def set_request(user_email, field, value=-1):
    r.hincrby(user_email, field, value)
    return r.hgetall(user_email)


def find_keys(pattern="*"):
    return r.keys(pattern=pattern)


def get_values(user_email):
    return r.hmget(user_email, keys=["name",
                                     "age",
                                     "request_limit"])
