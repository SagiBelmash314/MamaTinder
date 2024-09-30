from typing import Union

from pydantic import BaseModel, field_validator


class Range(BaseModel):
    """
    Model describing range of values : minimum & maximum.
    Validates minimum < maximum.
    """

    minimum: Union[int, float]
    maximum: Union[int, float]

    @field_validator("maximum")
    @classmethod
    def validate_range(cls, v: int | float, values: dict):
        """
        Validates input `maximum` bigger than `minimum` for `Range` schema model
        """
        minimum = values.get("minimum")
        if minimum is not None and v is not None and minimum >= v:
            raise ValueError("Maximum value must be greater than minimum value")
        return v
