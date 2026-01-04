from typing import Any, Dict

from app.controller.test_controller import TestController


class TestHandler:
    controller: TestController

    def __init__(self, controller: TestController) -> None:
        self.controller = controller

    async def test(self) -> Dict[str, Any]:
        return await self.controller.test()
