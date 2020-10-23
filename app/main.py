from fastapi import FastAPI

from app.routes.router import router


def create_app() -> FastAPI:
    application = FastAPI()

    application.include_router(router)

    return application


app = create_app()
