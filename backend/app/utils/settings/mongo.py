from functools import cache

from pydantic_settings import BaseSettings


class MongoSettings(BaseSettings):
    """
    mongo settings
    """

    connection_str: str = "mongodb://mongoadmin:mongopassword@192.168.1.134:27017"
    db_name: str = "test"
    user_collection: str = "users"
    user_exclude_properties: list[str] = ["_id", "age", "user_profile.pictures"]




@cache
def get_mongo_settings() -> MongoSettings:
    """
    getting mongo settings
    with cache for singelton
    """
    return MongoSettings()
