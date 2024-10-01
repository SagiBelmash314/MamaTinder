from datetime import date
from typing import List, Optional

from enums import Regions, RelationshipGoal
from pydantic import UUID4, BaseModel, computed_field
from schemas import UserPreferences


class UserProfile(BaseModel):
    """
    Defines the user profile model class.
    - birthdate : `date` > User's profile birthdate.
    - height : float > User's profile height.
    - location : (optional) `Regions` > User's profile region location.
    - relationship_goal : `RelationshipGoal` > User's profile relationship goal.
    - about_me : string > User's profile "about me".
    - pictures : `List[string]` > User's profile pictures.
    - preferences: `UserPreferences` > User's profile preferences.
    - liked_users : `List[UUID4]` > User's liked users.
    - matched_users: `List[UUID4]` > User's matched users.
    """

    birthdate: date
    height: float
    location: Optional[Regions] = None
    relationship_goal: RelationshipGoal
    about_me: str = ""
    pictures: List[str] = []
    preference: UserPreferences
    liked_users: List[UUID4] = []
    matched_users: List[UUID4] = []

    @computed_field
    @property
    def age(self) -> int:
        """
        Computes user's age based on their birthdate
        """
        today = date.today()
        age = (
            today.year
            - self.birthdate.year
            - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        )

        return age
