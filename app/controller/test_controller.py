from typing import Any, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.registry import Registry


class TestController:
    repo: Registry

    def __init__(self, repo: Registry) -> None:
        self.repo = repo

    async def test(self) -> Dict[str, Any]:
        async def _test(session: AsyncSession) -> Dict[str, Any]:
            test = await self.repo.test_repo().test(session)
            return test

        return await self.repo.transaction_wrapper(_test)
