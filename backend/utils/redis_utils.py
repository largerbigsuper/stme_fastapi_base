
import aioredis 

from core.config import settings


class RedisUtils:
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.pool = None

    async def connect(self):
        self.pool = await aioredis.from_url(self.redis_url)

    async def disconnect(self):
        if self.pool is not None:
            self.pool.close()
            await self.pool.close()

    async def set_captcha_code(self, key: str, value: str):
        await self.pool.set(settings.CACHE_CAPTCHA_PREFIX + key, value, ex=settings.CACHE_CAPTCHA_EXPIRE_SECONDS)

    async def get_captcha_code(self, key: str):
        return await self.pool.get(settings.CACHE_CAPTCHA_PREFIX + key)

redis_utils = RedisUtils(settings.REDIS_URL)