
import anyio
import asyncio
import logging

# 导入包
import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
project_root= os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from core.db.init_db import init_db
from core.db.session import async_session


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def init() -> None:
    # db = async_session()
    async with async_session() as db:
        await init_db(db)


if __name__ == "__main__":
    logger.info("Creating initial data")
    anyio.run(init)
    logger.info("Initial data created")