import logging
from typing import AsyncGenerator, Callable, Type, Optional

from fastapi import FastAPI, Depends
from starlette.requests import Request

from aioredis import create_redis_pool, RedisConnection, ConnectionsPool, Redis

from app.config.config import DB_HOST, DB_PORT

logger = logging.getLogger('uvicorn')


async def open_db_connection(app: FastAPI) -> None:
    try:
        app.state.pool = await create_redis_pool((DB_HOST, DB_PORT))
    except ConnectionError:
        logger.warning('No database available, caching disabled.')


async def close_db_connection(app: FastAPI) -> None:
    await app.state.pool.close()


def get_db_connection(request: Request) -> Optional[Redis]:
    if hasattr(request.app.state, 'pool'):
        return request.app.state.pool


def _get_db_pool(request: Request) -> Optional[ConnectionsPool]:
    if hasattr(request.app.state, 'pool'):
        return request.app.state.pool


async def get_connection_from_pool(pool: Optional[ConnectionsPool] = Depends(_get_db_pool)) -> AsyncGenerator[RedisConnection, None]:
    if pool:
        async with pool.acquire() as conn:
            yield conn
    else:
        yield None