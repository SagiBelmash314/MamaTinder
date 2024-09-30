from functools import cache

from pydantic_settings import BaseSettings


class GeneralSettings(BaseSettings):
    """
    general settings
    """

    fastapi_host: str = "0.0.0.0"
    fastapi_port: int = 8080


@cache
def get_general_settings() -> GeneralSettings:
    """
    getting general settings
    with cache for singelton
    """
    return GeneralSettings()
