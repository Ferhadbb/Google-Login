
# Source: https://testdriven.io/blog/fastapi-redis/
import redis
from app.config import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
    decode_responses=True
)