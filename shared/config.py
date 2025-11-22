from decouple import config
from typing import Optional

class Settings:
    DATABASE_URL: str = config("DATABASE_URL")
    
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = config("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
    REFRESH_TOKEN_EXPIRE_DAYS: int = config("REFRESH_TOKEN_EXPIRE_DAYS", cast=int)
    
    REDIS_URL: str = config("REDIS_URL")
    
    RABBITMQ_URL: str = config("RABBITMQ_URL")
    
    AUTH_SERVICE_PORT: int = config("AUTH_SERVICE_PORT", default=50051, cast=int)
    CHAT_SERVICE_PORT: int = config("CHAT_SERVICE_PORT", default=50052, cast=int)
    PRESENCE_SERVICE_PORT: int = config("PRESENCE_SERVICE_PORT", default=50053, cast=int)
    NOTIFICATION_SERVICE_PORT: int = config("NOTIFICATION_SERVICE_PORT", default=50054, cast=int)

settings = Settings()