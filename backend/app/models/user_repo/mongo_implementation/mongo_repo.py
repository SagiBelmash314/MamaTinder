from typing import Any

from models.user_repo.mongo_implementation.base_mongo_repo import BaseMongoRepo
from models.user_repo.user_repo_interface import IUserRepo
from pydantic import UUID4
from schemas.user import User


class MongoUserRepo(IUserRepo, BaseMongoRepo):
    async def get_by_id(self, user_id: UUID4) -> User:
        pass

    async def get_by_username(self, username: str) -> User:
        pass

    async def create(self, user: User) -> User:
        pass

    async def update(self, user_id: UUID4, prop: str, value: Any) -> User:
        pass

    async def delete(self, user_id: UUID4) -> None:
        pass

    async def get_by_prefrences(self, amount: int, user: User) -> list[User]:
        pass
