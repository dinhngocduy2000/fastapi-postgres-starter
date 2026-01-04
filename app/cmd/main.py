from typing import Callable
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.test_controller import TestController
from app.core.config import settings
from app.core.database import create_pg_engine
from loguru import logger

from app.handlers.test_handler import TestHandler
from app.repository.registry import Registry
from app.routes.test_router import TestRoute


class App:
    application: FastAPI

    def on_init_app(self) -> Callable:
        async def start_app() -> None:
            pg_engine = create_pg_engine()
            registry = Registry(pg_engine)
            # --------------- START OF TEST SERVICES ---------------
            test_controller = TestController(registry)
            test_handler = TestHandler(test_controller)
            test_router = TestRoute(test_handler)
            self.application.include_router(
                test_router.router,
                prefix=settings.API_V1_PREFIX,
                tags=["api"],
            )
            # --------------- END OF TEST SERVICES ---------------

        return start_app

    def on_terminate_app(self) -> Callable:
        @logger.catch
        async def stop_app() -> None:
            pass

        return stop_app

    def __init__(self) -> None:
        self.application = FastAPI(**settings.fastapi_kwargs)
        self.application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.application.add_event_handler("startup", self.on_init_app())
        self.application.add_event_handler("shutdown", self.on_terminate_app())


app = App().application
