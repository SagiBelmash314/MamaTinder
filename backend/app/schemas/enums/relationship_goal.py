from enum import Enum

class RelationshipGoal(Enum):
    '''
    Describes Relationship goals for user profile and preferences
    '''
    CASUAL = "casual"
    SHORT_TERM = "short-term"
    LONG_TERM = "long-term"