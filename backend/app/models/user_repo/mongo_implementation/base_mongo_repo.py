from typing import Any, Awaitable, Callable
from uuid import UUID

from models.user_repo.db_operation_error import DBOperationError
from models.user_repo.mongo_implementation.mongo_client_manager import MongoClientManager
from motor.motor_asyncio import AsyncIOMotorClient


class BaseMongoRepo:
    """
    repository for mongodb
    managing the mongo connection as singleton in all of its inheriting classes
    using the mongo client manager for it
    """

    def __init__(self, connection_string: str) -> None:
        self._manager: MongoClientManager = MongoClientManager(connection_string)
        res = self._manager.get_client()
        self._client_key: UUID = res[0]
        self._mongo_client: AsyncIOMotorClient = res[1]

    def close(self) -> None:
        """overriding inherited for mongodb"""
        self._manager.redeem_key(self._client_key)

    async def _perform_db_action(self, async_func: Callable[[], Awaitable[Any]], error_mesage: str) -> Any:
        """enveloping db actions in try exaption

        Args:
            async_func (Callable[[],Awaitable[Any]]): action to envelop
            error_mesage (str): the error message to raise

        Raises:
            DBOperationError: cannot complete the action

        Returns:
            Any: returning the result of the action
        """
        try:
            return await async_func()
        except Exception as e:
            raise DBOperationError(f"{error_mesage}: {e}") from e
