from typing import Any

from models.user_repo.mongo_implementation.base_mongo_repo import BaseMongoRepo
from models.user_repo.user_repo_interface import IUserRepo
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorCursor
from pydantic import UUID4
from pymongo.results import DeleteResult
from schemas.user import User
from utils import MongoSettings, get_mongo_settings

from app.models.user_repo.mongo_implementation.motor_query import create_user_query, in_query

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
        """overriding inherited from IUserRepo"""
        res = await self._perform_db_action(
            lambda: self._collection.find_one({"uuid": user_id}, projection=self._projection),
            "failed to find user",
        )
        return User(**res)

    async def get_by_id_list(self, user_ids: list[UUID4]) -> list[User]:
        """overriding inherited from IUserRepo"""
        documents: list[dict] = await self._perform_db_action(
            lambda: self._collection.find({"uuid": in_query(user_ids)}, projection=self._projection).to_list(
                length=None
            ),
            "failed to get objects",
        )
        return [User(**doc) for doc in documents]

    async def get_by_username(self, username: str) -> User:
        """overriding inherited from IUserRepo"""
        res = await self._perform_db_action(
            lambda: self._collection.find_one({"username": username}, projection=self._projection),
            "failed to find user",
        )
        return User(**res)

    async def _count_property_docs(self, prop_name: str, value: Any) -> int:
        """
        counts the amount of documents with the same value for the prop

        Raises:
            DBOperationError: couldent perform the db action

        Args:
            prop_name (str): the property name
            value (Any): value the object has in the prop

        Returns:
            int: amount of documents with the same value for the prop
        """
        old_user_count: int = await self._perform_db_action(
            lambda: self._collection.count_documents({prop_name: value}),
            "failed to check for existing user",
        )
        return old_user_count

    async def create(self, new_user: User) -> User:
        """overriding inherited from IUserRepo"""
        async with await self._mongo_client.start_session() as session:
            async with session.start_transaction():
                if self._count_property_docs("username", new_user.username):
                    raise ValueError("user already existes")
                created_user: dict[str, Any] = await self._perform_db_action(
                    lambda: self._collection.insert_one(new_user.model_dump(), return_document=True),
                    "failed to create object",
                )
        return User(**created_user)

    async def update(self, user_id: UUID4, prop: str, value: Any) -> User:
        """overriding inherited from IUserRepo"""
        async with await self._mongo_client.start_session() as session:
            async with session.start_transaction():
                if prop == "username":
                    if self._count_property_docs("username", value) > 1:
                        raise ValueError("user already existes")
                updated_doc = await self._perform_db_action(
                    lambda: self._collection.find_one_and_update(
                        {"uuid": user_id}, {"$set": {prop: value}}, return_document=True
                    ),
                    "Failed to update user",
                )
        if not updated_doc:
            raise ValueError(f"User with id {user_id} not found or update failed.")
        return User(**updated_doc)

    async def delete_by_id(self, user_id: UUID4) -> bool:
        """overriding inherited from IUserRepo"""
        deleted_count: DeleteResult = await self._perform_db_action(
            lambda: self._collection.delete_one({"uuid": user_id}), "failed to delete object"
        )
        if deleted_count.deleted_count == 0:
            raise ValueError("user not found")
        return True

    async def get_by_prefrences(self, amount: int, user: User) -> list[User]:
        """overriding inherited from IUserRepo"""
        curser: AsyncIOMotorCursor = self._perform_db_action(
            lambda: self._collection.find(create_user_query(user), projection=self._projection).limit(amount),
            "failed to get objects",
        )
        data: list[dict[str, Any]] = await curser.to_list(length=amount)
        return [User(**doc) for doc in data]
