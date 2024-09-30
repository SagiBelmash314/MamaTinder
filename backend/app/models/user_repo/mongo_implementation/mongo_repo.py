from typing import Any

from models.user_repo.mongo_implementation.base_mongo_repo import BaseMongoRepo
from models.user_repo.user_repo_interface import IUserRepo
from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import UUID4
from schemas.user import User
from utils import MongoSettings, get_mongo_settings

settings: MongoSettings = get_mongo_settings()


class MongoUserRepo(IUserRepo, BaseMongoRepo):
    """mongo user repo implementatin"""

    def __init__(self) -> None:
        super().__init__(settings.connection_str)
        self._collection: AsyncIOMotorCollection = self._mongo_client[settings.db_name][
            settings.user_collection
        ]
        self._projection: dict[str, int] = {field: 0 for field in settings.user_exclude_properties}

    async def get_by_id(self, user_id: UUID4) -> User:
        res = await self._perform_db_action(
            lambda: self._collection.find_one({"uuid": user_id}, projection=self._projection),
            "failed to find user",
        )
        return User(**res)

    async def get_by_username(self, username: str) -> User:
        res = await self._perform_db_action(
            lambda: self._collection.find_one({"username": username}, projection=self._projection),
            "failed to find user",
        )
        return User(**res)

    async def _check_property_existes(self,prop_name:str, value: Any) -> bool:
        old_user: dict = await self._perform_db_action(
            lambda: self._collection.find_one({prop_name: value}),
            "failed to check for existing user",
        )
        if old_user:
            raise ValueError("user already existes")
    
    async def create(self, new_user: User) -> User:
        async with await self._mongo_client.start_session() as session:
            async with session.start_transaction():
                old_user: dict = await self._perform_db_action(
                    lambda: self._collection.find_one({"username": new_user.username}),
                    "failed to check for existing user",
                )
                if old_user:
                    raise ValueError("user already existes")
                await self._perform_db_action(
                    lambda: self._collection.insert_one(new_user.model_dump(exclude={"id"})),
                    "failed to create object",
                )

    async def update(self, user_id: UUID4, prop: str, value: Any) -> User:
        pass

    async def delete(self, user_id: UUID4) -> None:
        pass

    async def get_by_prefrences(self, amount: int, user: User) -> list[User]:
        pass
