from abc import ABC, abstractmethod
from typing import Any

from pydantic import UUID4
from schemas.user import User


class IUserRepo(ABC):
    """interface for the user repo"""

    @abstractmethod
    async def get_by_id(self, user_id: UUID4) -> User:
        """
        getting user by id

        Raises:
            DBOperationError: cannot complete the action
            ValueError: user not found

        Args:
            user_id (UUID4): userid

        Returns:
            User: user with wanted id
        """

    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        """
        getting user by username

        Raises:
            DBOperationError: cannot complete the action
            ValueError: user not found

        Args:
            username (str): username

        Returns:
            User: user with the wanted username
        """

    @abstractmethod
    async def create(self, user: User) -> User:
        """
        creating user shuld override id and not allow multiple users with same username

        Raises:
            DBOperationError: cannot complete the action
            ValueError: user wit same username already exists

        Args:
            user (User): the user to create

        Returns:
            User: created user
        """

    @abstractmethod
    async def update(self, user_id: UUID4, prop: str, value: Any) -> User:
        """
        update user to new user data

        Raises:
            DBOperationError: cannot complete the action

        Args:
            user_id (UUID4): userid of the user to update
            prop (str): prop to update
            value (Any): the new value

        Returns:
            User: returning the new user
        """

    @abstractmethod
    async def delete(self, user_id: UUID4) -> None:
        """
        delete the user with that id

        Raises:
            DBOperationError: cannot complete the action

        Args:
            user_id (UUID4): id of the user to delete
        """

    @abstractmethod
    async def get_by_prefrences(self, amount: int, user: User) -> list[User]:
        """
        methode for getting multiple users by prefrences

        Raises:
            DBOperationError: cannot complete the action

        Args:
            amount (int): amount of people wanted
            user (user): user requesting for filtering

        Returns:
            list[User]: list of users that match the prefrences
        """
