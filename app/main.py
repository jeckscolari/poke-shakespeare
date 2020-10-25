from fastapi import FastAPI

from app.routes.router import router
from app.config.events import startup_handler, shutdown_handler


def create_app() -> FastAPI:
    application = FastAPI()

    application.add_event_handler('startup', startup_handler(application))
    application.add_event_handler('shutdown', shutdown_handler(application))

    application.include_router(router)

    return application


app = create_app()
