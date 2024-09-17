import os
import redis
from dotenv import load_dotenv
load_dotenv() 

redis_client = redis.StrictRedis(
    host=os.getenv("REDIS_HOST"), 
    port=os.getenv("REDIS_PORT"), 
    db=os.getenv("REDIS_DB")
)


def get_last_processed_line(redis_key):
    last_line = redis_client.get(redis_key)
    return int(last_line) if last_line else 0

def set_last_processed_line(redis_key, line_number):
    redis_client.set(redis_key, line_number)

def delete_key(redis_key):
    redis_client.delete(redis_key)
