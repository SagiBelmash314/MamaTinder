from functools import cache

from pydantic_settings import BaseSettings


class S3Settings(BaseSettings):
    """
    s3 settings
    """

    connection_str: str = "http://192.168.1.134:9000/"
    username: str = "minioadmin"
    password: str = "minioadmin123"


@cache
def get_s3_settings() -> S3Settings:
    """
    getting s3 settings
    with cache for singelton
    """
    return S3Settings()
