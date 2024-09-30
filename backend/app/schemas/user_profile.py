from typing import List, Optional

from enums import Regions, RelationshipGoal
from pydantic import BaseModel


class UserProfile(BaseModel):
    """
    Defines the user profile model class.
    - age : int > User's profile age.
    - height : float > User's profile height.
    - location : (optional) `Regions` > User's profile region location.
    - relationship_goal : `RelationshipGoal` > User's profile relationship goal.
    - about_me : (optional) string > User's profile "about me".
    - pictures : List[string] > User's profile pictures.
    - preferences: `UserPreferences` > User's profile preferences.
    """

    age: int
    height: float
    location: Optional[Regions] = None
    relationship_goal: RelationshipGoal
    about_me: Optional[str] = None
    pictures: List[str] = []
    preference: UserPreferences
