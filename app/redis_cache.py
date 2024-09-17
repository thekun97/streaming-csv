import redis 

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)


def get_last_processed_line(redis_key):
    last_line = redis_client.get(redis_key)
    return int(last_line) if last_line else 0

def set_last_processed_line(redis_key, line_number):
    redis_client.set(redis_key, line_number)

def delete_key(redis_key):
    redis_client.delete(redis_key)
