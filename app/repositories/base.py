from typing import Callable, Type

from aioredis import Redis
from fastapi import Depends

from app.config.database import get_db_connection


class BaseRepository:
    def __init__(self, conn: Redis) -> None:
        self._conn = conn

    @property
    def connection(self) -> Redis:
        return self._conn


def get_repository(repo_type: Type[BaseRepository]) -> Callable[[Redis], BaseRepository]:
    def get_repo(conn: Redis = Depends(get_db_connection)) -> BaseRepository:
        if conn:
            return repo_type(conn)
        else:
            return None
    return get_repo



