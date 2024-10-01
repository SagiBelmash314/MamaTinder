from typing import Any
from schemas.user import User
from schemas.utils import Range
from datetime import datetime


def create_user_query(user: User):
    query:dict[str,Any] = {}
    if user.user_profile.preference.age_range:
        current_date = datetime.now()
        min_birthdate = current_date.replace(year=current_date.year - user.user_profile.preference.age_range.maximum)
        max_birthdate = current_date.replace(year=current_date.year - user.user_profile.preference.age_range.minimum)
        query["user_profile.birthdate"] = range_query(Range(min_birthdate.year, max_birthdate.year))
    if user.user_profile.preference.height_range:
        query["user_profile.height"] = range_query(user.user_profile.preference.height_range)
    if user.user_profile.preference.locations:
        query["user_profile.locations"] = in_query(user.user_profile.preference.locations)
    if user.user_profile.preference.relationship_goals:
        query["user_profile.relationship_goals"] = in_query(user.user_profile.preference.relationship_goals)
    return query


def range_query(range:Range) -> dict[str, Any]:
    return{
        "$gte": range.minimum,
        "$lte": range.maximum
    }

def in_query(values:list[Any]) -> dict[str, Any]:
    return{
        "$in": values
    }

def not_in_query(values:list[Any]) -> dict[str, Any]:
    return{
        "$nin": values
    }