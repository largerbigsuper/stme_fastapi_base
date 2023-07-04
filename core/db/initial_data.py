import logging

# 导入包
import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
project_root= os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from core.db.init_db import init_db
from core.db.session import SessionLocal


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
