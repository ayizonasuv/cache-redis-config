import os
import logging
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB

def get_redis_client():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def set_cache(key, value):
    client = get_redis_client()
    client.set(key, value)
    logging.info(f"Set cache for key: {key}")

def get_cache(key):
    client = get_redis_client()
    value = client.get(key)
    if value is None:
        value = "None"
    logging.info(f"Fetched cache for key: {key}")
    return value

def delete_cache(key):
    client = get_redis_client()
    client.delete(key)
    logging.info(f"Deleted cache for key: {key}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    cache_key = "example_cache_key"
    cache_value = "example_cache_value"
    set_cache(cache_key, cache_value)
    fetched_cache = get_cache(cache_key)
    print(f"Fetched Cache: {fetched_cache}")
    delete_cache(cache_key)