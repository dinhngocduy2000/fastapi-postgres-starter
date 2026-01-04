from fastapi import APIRouter

from app.handlers.test_handler import TestHandler


class TestRoute:
    router: APIRouter
    handler: TestHandler

    def __init__(self, handler: TestHandler) -> None:
        self.router = APIRouter()
        self.handler = handler
        self.router.add_api_route(
            path="/test",
            endpoint=self.handler.test,
            methods=["GET"],
        )
