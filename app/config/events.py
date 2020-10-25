from typing import Callable

from fastapi import FastAPI

from app.config.database import open_db_connection, close_db_connection


def startup_handler(app: FastAPI) -> Callable:
    async def startup() -> None:
        await open_db_connection(app)
    return startup


def shutdown_handler(app: FastAPI) -> Callable:
    async def shutdown() -> None:
        await close_db_connection(app)
    return shutdown
