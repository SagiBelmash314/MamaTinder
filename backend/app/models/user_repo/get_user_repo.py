from functools import cache

from models.user_repo.mongo_implementation import MongoUserRepo
from models.user_repo.user_repo_interface import IUserRepo


@cache
def get_user_repo() -> IUserRepo:
    return MongoUserRepo()