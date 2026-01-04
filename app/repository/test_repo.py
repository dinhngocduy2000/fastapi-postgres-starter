from typing import Any, Dict
from sqlalchemy.ext.asyncio import AsyncSession


class TestRepository:

    def __init__(self) -> None:
        pass

    async def test(self, session: AsyncSession) -> Dict[str, Any]:
        return {"message": "Hello, World From Repository!"}
