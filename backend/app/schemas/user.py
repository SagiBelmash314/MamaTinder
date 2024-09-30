from pydantic import UUID4, BaseModel
from schemas import UserProfile

class User(BaseModel):
    """
    Defines the User model class.
    - uuid : UUID4 > User's unique ID
    - username: string > User's username
    - password: string > User's password
    - user_profile: `UserProfile` > User's Profile(class)
    """

    uuid: UUID4
    username: str
    password: str
    user_profile: UserProfile
