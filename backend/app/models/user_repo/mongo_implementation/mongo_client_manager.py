from functools import cache
from typing import Optional
from uuid import UUID, uuid4

from motor.motor_asyncio import AsyncIOMotorClient


class MongoClientManager:
    """
    class managing singel mongo client
    """

    def __init__(self, connection_string: str) -> None:
        self._connection_string: str = connection_string
        self._mongo_client: Optional[AsyncIOMotorClient] = None
        self._repos_list: list[UUID] = []

    def get_client(self) -> tuple[UUID, AsyncIOMotorClient]:
        """
        returning mongo client with licensing key

        Raises:
            ConnectionError: when unabel to connect to mongo

        Returns:
            tuple[UUID, AsyncIOMotorClient]: mongo client with licensing key
        """
        if not self._mongo_client:
            try:
                self._mongo_client = AsyncIOMotorClient(self._connection_string)
            except ConnectionError as e:
                raise ConnectionError("failed to connect to mongo") from e
        repo_key: UUID = uuid4()
        self._repos_list.append(repo_key)
        return repo_key, self._mongo_client

    def redeem_key(self, repo_key: UUID) -> None:
        """
        allows the repose to declare day wont be using the client
        closing the client when no repo is using it

        Args:
            repo_key (UUID): licensing key got from get_client()

        Raises:
            ValueError: whn the key not in the list
        """
        try:
            self._repos_list.remove(repo_key)
        except ValueError as e:
            raise ValueError("invalid repo key") from e

        if not self._repos_list:
            self._mongo_client.close()
            self._mongo_client = None


@cache
def get_client(connection_string: str) -> MongoClientManager:
    """gets the client with cache for singlton"""
    return MongoClientManager(connection_string)
