from fastapi import FastAPI

from utils.redis_utils import redis_utils


def register_redis(app: FastAPI) -> None:
    @app.on_event('startup')
    async def startup_event():
        """
        获取链接池
        :return:
        """
        await redis_utils.connect()
        # app.state.redis = await redis_utils.connect()

    @app.on_event('shutdown')
    async def shutdown_event():
        """
        关闭链接池
        :return:
        """
        await redis_utils.disconnect()
        # app.state.redis.close()
