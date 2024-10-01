from typing import List, Optional

from enums import Regions, RelationshipGoal
from pydantic import BaseModel
from utils import Range


class UserPreferences(BaseModel):
    """
    Defines the user's preferences model class. all parameters are optional.
    - age_range : `Range` > age range
    - height_range : `Range` > height range
    - locations : `List[Regions]` > preferred regions
    - relationship_goals : `List[RelationshipGoal]` > preffered relationship types
    """

    age_range: Optional[Range] = None
    height_range: Optional[Range] = None
    locations: Optional[List[Regions]] = None
    relationship_goals: Optional[List[RelationshipGoal]] = None
