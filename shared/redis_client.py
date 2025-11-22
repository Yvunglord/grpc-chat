import redis
import logging
from .config import settings

class RedisClient:
    def __init__(self):
        self.redis_client = None
        self._connect()
    
    def _connect(self):
        try:
            self.redis_client = redis.from_url(
                settings.REDIS_URL,
                encoding="utf-8",
                decode_responses=True
            )
            self.redis_client.ping()
            logging.info("Redis connection successful")
        except Exception as e:
            logging.error(f"Redis connection failed: {e}")
            self.redis_client = None
    
    def get_client(self):
        if self.redis_client is None:
            self._connect()
        return self.redis_client

redis_client = RedisClient()